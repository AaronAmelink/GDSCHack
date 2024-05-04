from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

DRIVER_PATH = './chromedriver'


class chromeManager:
    def __init__(self):
        self.options = Options()
        self.options.headless = False
        path = os.path.dirname(os.getcwd())
        print(path)
        prefs = {'download.default_directory' : path+"\\GDSCHacksUnity\\Assets\\Art\\pictures\\"}
        self.options.add_experimental_option('prefs', prefs)
        self.options.add_argument("--window-size=1920,1200")
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options)
        self.actionChains = ActionChains(self.driver)

    def goToPage(self, url):
        self.url = url
        self.driver.get(url)

    def clickAtElement(self, element):
        self.actionChains.move_to_element(element).click().perform()

    def clickAtElementByXPATH(self, path):
        element = element = self.driver.find_element(By.XPATH, path)
        self.actionChains.move_to_element(element).click().perform()

    def exit(self):
        self.driver.quit()
    
    def clickByXPATH(self, XPATH):
        element = self.driver.find_element(By.XPATH, XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    
    def getElementsOfClass(self, className):
        return self.driver.find_elements(By.CLASS_NAME, className)
    
    def getElementById(self, id):
        return self.driver.find_element(By.ID, id)

    def getSubElementsByClass(self, element, className):
        return element.find_elements(By.CLASS_NAME, className)
    
    def getSubElementsByTag(self, e, tag):
        return e.find_elements(By.TAG_NAME, tag)
    
    def clickElement(self, e):
        self.driver.execute_script("arguments[0].scrollIntoView();", e)
        e.click()


    def getByXPATH(self, path):
        return self.driver.find_element(By.XPATH, path)