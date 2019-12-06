import requests
from bs4 import BeautifulSoup as Scraper

class Website(object):

    def __init__(self):
        self._url = "https://www.bbc.com/"
        self._titleList = self._getHeadlines()
        self._subtitleList = self._getSubtitles()
        self._linkList = self._getLinks()
        self._counter =  0

    def __str__(self):
        return self._url

    def _getPageSource(self, url): #Return the Page Source HTML as text
        webPage = requests.get(url).text
        page = Scraper(webPage, "html.parser")
        return page
    
    def _getHeadlines(self): #Return headline of articles, starting from top to bottom
        headlineSource = self._getPageSource(self._url)
        titleSource = headlineSource.find_all('div', class_="media__content")
        titles = []
        for title in titleSource:
            titles.append(title.h3.text.lstrip().rstrip())
        return titles

    def printHeadline(self):
        try:
            self._title = self._titleList[self._counter]
            print(self._title)
        except IndexError:
            print("There are no more articles ")
            self.goBack()

    def _getSubtitles(self): #Return the quick summary underneath the title
        subtitleSource = self._getPageSource(self._url)
        subtitles = subtitleSource.find_all('div', class_="media__content")
        return subtitles
    
    def printSubtitles(self):

        subtitle = self._subtitleList[self._counter].find('p', class_="media__summary")
        if subtitle != None:
            print(subtitle.text.lstrip().rstrip())
        else:
            print('No summary')
    
    def _getLinks(self):
        linkSource = self._getPageSource(self._url)
        links = linkSource.find_all('div', class_="media__content")
        return links
    
    def getArticlePage(self):
        link = self._linkList[self._counter].find('a', class_="media__link")
        url = (link['href'])
        if 'bbc' in url:
            pageSource = self._getPageSource(url)
        else:
            pageSource = self._getPageSource('https://www.bbc.com' + url)
        try:
            body = pageSource.find("div", class_="story-body__inner")
            paragraphList = body.find_all('p')
            for paragraph in paragraphList:
                print(paragraph.text)
        except AttributeError:
            print("Unable to read specified page ")


    def goBack(self): #Go back one article
        self._counter -= 1

    def goForward(self):
        self._counter += 1