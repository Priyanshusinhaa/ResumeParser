import re
from PdfFetcher import PdfFetcher


a = PdfFetcher('./PriyanshuSinhaResumev1.4.pdf')
a = str(a)
# print(str(a), type(a))

pattern = re.compile(r"\d\d\d\d.\d\d\.\d\d|\d\d.[0-1]\d.\d\d\d\d|[0-1]\d.\d\d.\d\d\d\d")

text = pattern.findall(a)

print(text)