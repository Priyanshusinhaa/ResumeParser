from pprint import pprint
from Format import ResumeFormat
from PdfFetcher import PdfFetcher
from re import *

class ResumeParser:
    def __init__(self, path) -> None:
        ResumeFormat()
        self.data = PdfFetcher(path)
        self.data = str(self.data)
    def getDict(self):
        objFormat = {'Name': None,
                    'Email': None,
                    'Address': None,
                    'PhoneNumber': None,
                    'DOB': None,
                    'Country': None,
                    'SocialMedia':{
                        'Twitter': None,
                        'LinkedIn': None,
                        'Github': None,
                        'YouTube': None,
                        'Instagram': None,
                        'Other': None
                    },
                    'Summary': None,
                    'Experience': None,
                    'Projects': None,
                    'Education': None,
                    'Skills': None,
                    'Achievements': [],
                    'Awards': [],
                    'Reference': [],
                    'Publication': []
                }
        obj = ResumeFormat(
                        name = self.__name(), 
                        email = self.__email(),
                        address = self.__address(),
                        phoneNumber = self.__phoneNumber(),
                        dob = self.__dob(),
                        country = self.__country(),
                        socialMedia = self.__socialMedia(),
                        summary = self.__summary(),
                        experience = self.__experience(),
                        projects = self.__projects(),
                        education = self.__education(),
                        skills = self.__skills(),
                        achievements = self.__achievements(),
                        awards = self.__awards(),
                        reference = self.__reference(),
                        publication = self.__publication()
                        )
        return vars(obj)

        
    def __name(self):
        namePattern = compile("name")
        name = namePattern.findall(self.data)
        if len(name) != 0:
            return name
        return None
    def __email(self):
        emailPattern = compile("")
        email = emailPattern.findall(self.data)
        if len(email) != 0:
            return email
        return None
    def __phoneNumber(self):
        phonePattern = compile("[6-9]\d{9}")
        phone = phonePattern.findall(self.data)
        if len(phone) != 0:
            return phone
        return None


    def __address(self):
        addressPattern = compile("address")
        address = addressPattern.findall(self.data)
        if len(address) != 0:
            return address
        return None

    def __dob(self):
        dobPattern = compile(r"\d{4}.\d{2}.\d{2}|\d{2}.[0-1]\d.\d{4}|[0-1]\d.\d{2}.\d{4}")
        dob = dobPattern.findall(self.data)
        if len(dob) != 0:
            return dob[0]
        return None
    
    def __country(self):
        countryPattern = compile("country")
        country = countryPattern.findall(self.data)
        if len(country) != 0:
            return country
        return None
    
    def __socialMedia(self):
        socialMediaPattern = compile("socialMedia")
        socialMedia = socialMediaPattern.findall(self.data)
        if len(socialMedia) != 0:
            return socialMedia
        return None

    def __summary(self):
        summaryPattern = compile("summary")
        summary = summaryPattern.findall(self.data)
        if len(summary) != 0:
            return summary
        return None
    
    def __experience(self):
        experiencePattern = compile("experience")
        experience = experiencePattern.findall(self.data)
        if len(experience) != 0:
            return experience
        return None
    def __projects(self):
        projectsPattern = compile("projects")
        project  = projectsPattern.findall(self.data)
        if len(project) != 0:
            return project
        return None
    def __education(self):
        educationPattern = compile("education")
        education = educationPattern.findall(self.data)
        if len(education) != 0:
            return education
        return None
    def __skills(self):
        skillsPattern = compile("skill")
        skills = skillsPattern.findall(self.data)
        if len(skills) != 0:
            return skills
        return None
    
    def __achievements(self):
        achievementsPattern = compile("achievements")
        achievements = achievementsPattern.findall(self.data)
        if len(achievements) != 0:
            return achievements
        return None
    
    def __awards(self):
        awardsPattern = compile("awards")
        awards = awardsPattern.findall(self.data)
        if len(awards) != 0:
            return awards
        return None
    
    def __reference(self):
        referencePattern = compile("reference")
        reference = referencePattern.findall(self.data)
        if len(reference) != 0:
            return reference
        return None
    
    def __publication(self):
        publicationPattern = compile("publication")
        publication = publicationPattern.findall(self.data)
        if len(publication) != 0:
            return publication
        return None
    

path = './PriyanshuSinhaResumev1.4.pdf'

resumeObj = ResumeParser(path)
pprint(vars(resumeObj))
pprint(resumeObj.getDict()) 