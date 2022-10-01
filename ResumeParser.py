from pprint import pprint
from Format import ResumeFormat
from PdfFetcher import PdfFetcher
from re import *
from listOfCountries import countries
from listOfSkills import skillsList
from subTitleList import subTitleList
import nltk
from operator import itemgetter

class ResumeParser:
    def __init__(self, path) -> None:
        ResumeFormat()
        self.data = PdfFetcher(path).getStr()
        self.dataList = PdfFetcher(path).getList()
        self.searchList = self.search(subTitleList)

    def sortDict(self, myDict):
        myList = []
        for k,v in myDict.items():
            a, b = v
            myList.append([k, a, b])
        myList = sorted(myList, key=itemgetter(2))
        return myList

            

    def getDict(self):
        objFormat = {'Name': None,
                    'Email': None,
                    'Address': None,
                    'PhoneNumber': None,
                    'DOB': None,
                    'Country': None,
                    'Experience': None,
                    'Projects': None,
                    'Education': None,
                    'Skills': None,
                    'Achievements': [],
                    'Publication': []
                }
        obj = ResumeFormat(
                        name = self.__name(), 
                        email = self.__email(),
                        address = self.__address(),
                        phone = self.__phoneNumber(),
                        dob = self.__dob(),
                        country = self.__country(),
                        experience = self.__experience(),
                        projects = self.__projects(),
                        education = self.__education(),
                        skills = self.__skills(),
                        achievements = self.__achievements(),
                        publication = self.__publication()
                        )
        return obj
    def search(self, mySubTitleList):
        matchSet = set()
        matchDict = {}
        for i in mySubTitleList:
            ins = compile(i)
            searchList = ins.search(self.data)
            if searchList == None:
                pass
            else:
                matchSet.add(searchList)
        for i in list(matchSet):
            matchDict[i.group()] = i.span()
        if len(matchSet) != 0:
            return self.sortDict(matchDict)
        return None
  
    def __name(self):
        searchWithIn = 3
        dataList = self.dataList[:searchWithIn]
        data = []
        for i in dataList:
            a = i.split(' ')
            if (len(a) == 2) | (len(a) == 1) | (len(a) == 3):
                data.append(' '.join(a))
        if len(data) != 0:
            return data[0]
        return None
        
    def __email(self):
        emailPattern = compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        myStr = ' '.join(self.dataList)
        email = emailPattern.findall(myStr)
        if len(email) != 0:
            return email[0]
        return None
    def __phoneNumber(self):
        phonePattern = compile("\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}")
        phone = phonePattern.findall(self.data)
        if len(phone) != 0:
            return phone[0]
        return None

    def __address(self):
        addressPattern = compile("^(\\d{1,}) [a-zA-Z0-9\\s]+(\\,)? [a-zA-Z]+(\\,)? [A-Z]{2} [0-9]{5,6}$")
        address = addressPattern.findall(self.data)
        if address:
            return address
        return None

    def __dob(self):
        dobPattern = compile(r"\d{4}.\d{2}.\d{2}|\d{2}.[0-1]\d.\d{4}|[0-1]\d.\d{2}.\d{4}")
        dob = dobPattern.findall(self.data)
        if len(dob) != 0:
            return dob[0]
        return None
    
    def __country(self):
        indexes = [self.data.find(country) for country in countries]
        country = [(index, country) for index, country in zip(indexes, countries) 
                  if index != -1]
        if country:
            return country[0][1]
        return None
    def __experience(self):
        l, f = None, None
        for i in range(len(self.searchList)):
            if 'Experience' in self.searchList[i][0]:
                if self.searchList[i][0] == self.searchList[-1][0]:
                    f = len(self.data) -1
                else:
                    f = self.searchList[i+1][1] -1  
                l = self.searchList[i][2]
        if l != None and f != None:
            experience = self.data[l:f]
            return experience
        else:
            return None
    def __projects(self):
        l, f = None, None
        for i in range(len(self.searchList)):
            if 'Projects' in self.searchList[i][0]:
                if self.searchList[i][0] == self.searchList[-1][0]:
                    f = self.data[-1]
                else:
                    f = self.searchList[i+1][1] -1   
                l = self.searchList[i][2]
        if l != None and f != None:
            project = self.data[l:f]
            return project
        else:
            return None
    def __education(self):
        l, f = None, None
        for i in range(len(self.searchList)):
            if 'Education' in self.searchList[i][0]:
                if self.searchList[i][0] == self.searchList[-1][0]:
                    f = len(self.data) -1
                else:
                    f = self.searchList[i+1][1] -1   
                l = self.searchList[i][2]
        if (l != None) and (f != None):
            education = self.data[l:f]
            return education
        else:
            return None

    def __skills(self):
        stopWords = set(nltk.corpus.stopwords.words('english'))
        wordTokens = nltk.tokenize.word_tokenize(self.data)
        filter = [i for i in wordTokens if i not in stopWords]
        filter = [i for i in wordTokens if i.isalpha()]
        grams23 = list(map(' '.join, nltk.everygrams(filter, 2, 3)))
        skills = set()
        for token in filter:
            if token.lower() in skillsList:
                skills.add(token)
        for j in grams23:
            if j.lower() in skillsList:
                skills.add(j)

        return list(skills)
    
    def __achievements(self):
        l, f = None, None
        for i in range(len(self.searchList)):
            if 'Achievements' in self.searchList[i][0]:
                if self.searchList[i][0] == self.searchList[-1][0]:
                    f = len(self.data) -1
                else:
                    f = self.searchList[i+1][1] -1  
                l = self.searchList[i][2]
        if l != None and f != None:
            achievements = self.data[l:f]
            return achievements
        else:
            return None

    def __publication(self):
        l, f = None, None
        for i in range(len(self.searchList)):
            if 'Publication' in self.searchList[i][0]:
                if self.searchList[i][0] == self.searchList[-1][0]:
                    f = len(self.data) -1
                else:
                    f = self.searchList[i+1][1] -1  
                l = self.searchList[i][2]
        if l != None and f != None:
            publication = self.data[l:f]
            return publication
        else:
            return None   

path = './resume.pdf'

resumeObj = ResumeParser(path).dataList

a = ' '.join(resumeObj)
a = ResumeParser(path).getDict()
b = ResumeParser(path).search(subTitleList)
print(a)
