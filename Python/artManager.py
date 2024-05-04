from venv import create

from matplotlib.image import thumbnail
from chromeManager import chromeManager
import time
from art import art
import json
import re
amountPerPage = 30
class artManager:
    def __init__(self):
        self.CM = chromeManager()
        self.filterButtonXPATH = "/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/button"
        self.filterMenuToggled = False
        self.filterTypes = dict()
        self.art = []
        self.amountOfArt = 30
        self.CM.goToPage('https://www.nga.gov/collection-search-result.html?sortOrder=DEFAULT&artobj_downloadable=Image_download_available&pageNumber=1&lastFacet=artobj_downloadable')

    def checkFilterMenuOn(self):
        if (self.filterMenuToggled == False):
            self.CM.clickByXPATH(self.filterButtonXPATH)
            time.sleep(0.5)
        
    def getFilterTypes(self):
        elements = self.CM.getElementsOfClass("drawer-toggle")
        content = self.CM.getElementsOfClass("drawer-content")
        for i in range(len(elements)):
            self.filterTypes[elements[i]] = self.CM.getSubElementsByTag(content[i], 'input')

    def changeAmountOfArt(self, amount): #this just breaks their website
        self.CM.clickAtElementByXPATH('/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]/select')
        time.sleep(0.1)
        if (amount == 60):
            self.amountOfArt = 60
            self.CM.clickByXPATH('/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]/select/option[2]')
        elif (amount == 90):
            self.amountOfArt = 90
            self.CM.clickByXPATH('/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]/select/option[3]')
        else:
            self.amountOfArt = 30
            self.CM.clickByXPATH('/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]/select/option[1]')
        time.sleep(500)

    def toggleFilter(self, name):
        for e, i in self.filterTypes.items():
            for x in i:
                if x.get_attribute("value") == name:
                    self.CM.clickElement(e)
                    time.sleep(0.1)
                    self.CM.clickAtElement(x)
                    time.sleep(0.1)
                    self.CM.clickElement(e)
                    time.sleep(0.1)

    def getArtSizingOff(self):
        artRef = self.CM.getElementsOfClass("art")
        for i in range(len(artRef)):
            artist = self.CM.getSubElementsByClass(artRef[i], 'artist')[0] .text
            title = self.CM.getSubElementsByTag(artRef[i], 'a')[2] .text
            created = self.CM.getSubElementsByClass(artRef[i], "created")[0].text
            download = self.CM.getSubElementsByClass(artRef[i], "tool-download")[0]
            self.CM.clickAtElement(download)
            downloadName = self.CM.getSubElementsByClass(artRef[i], "icon-helper")[1].get_attribute('href').split("filename=")[1].replace("%2C", "")
            newArt = art(0,0, artist, created, title, downloadName)
            self.art.append(newArt)
        data = {"art" : []}
        for i in self.art:
            data["art"].append({"artist": i.artist, "width" : 0, "height" : 0, "download" : i.fileName, "created" : i.created, "title" : i.name})
        
        with open('./../GDSCHacksUnity/Assets/Art/data.json', 'w') as f:
            json.dump(data, f)
        


    def getArtSizingOn(self):
        for i in range(amountPerPage):
            artRef = self.CM.getElementsOfClass("art")[i]
            artist = self.CM.getSubElementsByClass(artRef, 'artist')[0] .text
            title = self.CM.getSubElementsByTag(artRef, 'a')[2] .text
            created = self.CM.getSubElementsByClass(artRef, "created")[0].text
            download = self.CM.getSubElementsByClass(artRef, "tool-download")[0]
            self.CM.clickAtElement(download)
            downloadName = self.CM.getSubElementsByClass(artRef, "icon-helper")[1].get_attribute('href').split("filename=")[1]

            newUrl =self.CM.getSubElementsByTag(artRef, 'a')[2].get_attribute("href")
            self.CM.goToPage(newUrl)
            time.sleep(3)
            size = self.CM.getByXPATH('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/p[1]').text
            floats = re.findall(r"[-+]?\d*\.\d+|\d+", size)
            floats = [float(f) for f in floats[:2]]

            newArt = art(floats[0],floats[1], artist, created, title, downloadName)

            self.CM.driver.back()
            self.art.append(newArt)
            time.sleep(6)
        data = {"art" : []}
        for i in self.art:
            data["art"].append({"artist": i.artist, "width" : i.width, "height" : i.height, "download" : i.fileName, "created" : i.created, "title" : i.name})
        
        with open('./../GDSCHacksUnity/Assets/Art/data.json', 'w') as f:
            json.dump(data, f)

    def goNextPage(self):
        element = self.CM.getElementById("pageNext")
        self.CM.clickAtElement(element)
        time.sleep(5)


