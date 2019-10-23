import requests, webbrowser
from bs4 import BeautifulSoup
import sys



def getQuestions(func):
    def wrapper():
        try:
            func()
        except Exception as e:
            query = f'{type(e).__name__} : {e.args[0]}' # a string with the name and description of the error
            print(f'Query is {query}')
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

            for questionUrl in questionDict.values():
                webbrowser.open_new_tab(questionUrl)
    return wrapper



@getQuestions
def divide():
    return 3/0

divide()