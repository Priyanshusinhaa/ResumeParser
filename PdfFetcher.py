import textract
import re

class PdfFetcher:
    def __init__(self, path) -> None:
        self.path = path
        self.text = textract.process(self.path, 'UTF-8')
    def __str__(self) -> str:
        return str(self.myText)
    def getByte(self):
        return self.text
    def getStr(self):
        return self.text.decode('UTF-8')
    def getList(self):
        myStr = self.getStr()
        myStr = myStr.replace('\r', '')
        myStr = myStr.replace('\f', '')
        dataList = myStr.split('\n')
        dataList = [value for value in dataList if value != ""]
        dataList = [value for value in dataList if len(value) != 1]
        return dataList