from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests

def WebSearch(word):
    def Search(word):
        SearchURL = "https://www.google.co.kr/search?q=" + quote_plus(word)
        print(SearchURL)
        response = requests.get(SearchURL)

        if response.status_code == 200:
            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Edge(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.get(SearchURL)

            Result_html = driver.page_source
            soup = BeautifulSoup(Result_html,'html.parser')
            return soup

        else:
            print(response.status_code)
            print('Can\'t connect or search')

    def PrintURL(soup):
        result = soup.select_one(".yuRUbf") #구글의 검색결과의 div의 class의 선택자
        print(result.find("a")["href"])

    PrintURL(Search(word))

if __name__ == "__main__":
    SearchWord = input("검색어 : ")

    WebSearch(SearchWord)