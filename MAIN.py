from ResumeParser import ResumeParser

def main():
    path = '' #put your path here
    resume = ResumeParser(path).getDict()
    print(resume)
    pass


if __name__ == '__main__':
    main()