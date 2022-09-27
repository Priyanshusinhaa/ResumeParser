import textract
import re

path = './functionalsample.pdf'

class PdfFetcher:
    def __init__(self, path) -> None:
        self.path = path
        text = textract.process(self.path, 'UTF-8')
        self.myText = text.decode('UTF-8')
    def __str__(self) -> str:
        return str(self.myText)

    
# a = PdfFetcher(path)

# print(a) 

# a = str(a)

# Regex.Match(yourString,"(.+\n)+\d{5}.*").Value

# a = re.findall("(.+\n)+\d{5}.*", a)

# findall(), finditer(), match(), search()

# pattern = re.compile("Career Summary")
# text = pattern.finditer(a)

#group , start, end, span -- call values inside match object using these function
# for i in text:
#     print(i.span())
#     print(i.start(), i.end())
#     print(i.group())
#     print(i)
#     print('\n')

# print(text)


# print(a) 

        