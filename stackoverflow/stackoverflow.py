import requests, webbrowser
from bs4 import BeautifulSoup
import sys



def getQuestions(query):
    stacklink=r'https://stackoverflow.com'
    toQuery=lambda x:'/search?q='+'+'.join(x.split())

    # error='unicode error'

    url=stacklink+toQuery(query)
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    questionList=soup.find_all(class_='question-hyperlink')
    questionDict={}

    for question in questionList:
        if question.get('title'): # if it's not none
            questionDict[question.get('title')] = stacklink+question.get('href')
    return questionDict

# query = "python error"
query = sys.argv[1]
print(query)

for questionUrl in getQuestions(query).values():
    webbrowser.open_new_tab(questionUrl)