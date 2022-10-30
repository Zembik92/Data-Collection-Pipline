from selenium import webdriver
#from time import sleep, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import uuid
import os
import json

options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging']) #The above two code is to cater for the selenium error message
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()
URL = "https://www.agoda.com/en-gb/search?city=17193&checkIn=2023-03-03&los=14&rooms=1&adults=2&children=0&cid=1891458&locale=en-gb&ckuid=9cdf223f-a3ce-4890-965a-b2aab1ae50d6&prid=0&gclid=Cj0KCQjwqc6aBhC4ARIsAN06NmOZjaRodGcrUeKINOPnKgTZEfVb8z7hDSCrkddzvLoQZA07tdLlcnsaAg2qEALw_wcB&currency=GBP&correlationId=d880d555-ceda-41ba-b708-41c298e4db9b&pageTypeId=1&realLanguageId=16&languageId=1&origin=GB&tag=24bd4b3f-b6a1-50d5-e639-d9c49ca41c49&userId=9cdf223f-a3ce-4890-965a-b2aab1ae50d6&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=2&currencyCode=GBP&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=am-pc-4f-acm-web-user-7d974b9749-vw7ck&trafficGroupId=5&sessionId=ug4znrtc3dsxzbtr2i4zpami&trafficSubGroupId=122&aid=82361&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&checkOut=2023-03-17&priceCur=GBP&textToSearch=Bali&productType=-1&travellerType=1&familyMode=off"
driver.get(URL) 
  

class Scraper:
    '''create a scaper class with all methods used to scape the website'''  
    
    def __init__(self) -> None:
        self.link_list = []
        self.big_list = []
        self.dict_properties = {'ID': [],'Timestamp': [],'Description': [],'Price': [],'Location': [],'Rating/10': [],'Image URL': []}

       


    def accept_cookie(self):
        time.sleep(2)
        try:
            accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="consent-banner-container"]/div/div[2]/div/button[2]')
            accept_cookies_button.click()
        except:
            pass # If there is no cookies button, we won't find it, so we can pass


    # def close_rewards(self):
    #     time.sleep(2)
    #     try:
    #         close_rewards_button = driver.find_element(by=By.XPATH, value='/html/body/div[12]/div[2]/button')
    #         close_rewards_button.click()

    #     except:
    #         pass # If there is no cookies button, we won't find it, so we can pass


    # def search(self):
    #     time.sleep(2)
    #     search_bar = driver.find_element(by=By.XPATH, value='//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[1]/div/div/input')
    #     #search_bar.click()
    #     search_bar.send_keys("Bali")
    #     search_bar.send_keys(Keys.ARROW_DOWN)
    #     search_bar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#SearchBoxContainer > div.Box-sc-kv6pi1-0.cVUuHz.TabContent.OpaqueBackground > div > div.Box-sc-kv6pi1-0.hRUYUu > div > div > div.Popup__container.Popup__container--garage-door > div > div > ul > li:nth-child(1)')))
    #     search_bar.send_keys(Keys.RETURN)    

        

    def top_reviewed(self):
        time.sleep(2)
        review_bar = driver.find_element(by=By.XPATH, value='//*[@id="sort-bar"]/div/a[2]')
        review_bar.click() 
        time.sleep(2)   
         
# Extract all the links
# Iterate through the list, and for each iteration, visit the corresponding URL
# Sleep
# Extract the information of the property
# Visit the next URL      

    def scroller(self):
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(2)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


    def links_of_hotels(self):
        time.sleep(2)
        try:
            hotel_container = driver.find_element(by=By.XPATH, value='//*[@id="contentContainer"]') # XPath corresponding to the Container
            hotel_list = hotel_container.find_elements(by=By.XPATH, value='//li/div/a[contains(@class, "PropertyCard__Link")]')
            for hotel_link in hotel_list:
                time.sleep(10)
                links = hotel_link.get_attribute('href')
                self.link_list.append(links)  
            return self.link_list
        except:
            pass    


    def crawling(self):
        for page in range(2):
            time.sleep(2)
            self.big_list.extend(self.links_of_hotels())
            next_button = driver.find_element(by=By.XPATH, value='//*[@id="paginationNext"]')
            next_button.click() 
        return self.big_list 


    def get_info(self):
        for link in self.big_list[0:10]:
            driver.get(link)
            time.sleep(5)
            try:
                price = driver.find_element(by=By.XPATH, value= '//*[@id="hotelNavBar"]/div/div/div/span/div/span[5]').text
                self.dict_properties['Price'].append(price)
                description = driver.find_element(by=By.XPATH, value= '//*[@id="property-main-content"]/div[1]/div[2]/div[1]/h1').text
                self.dict_properties['Description'].append(description)
                location = driver.find_element(by=By.XPATH, value= '//*[@id="property-main-content"]/div[1]/div[2]/div[2]/span[1]').text
                self.dict_properties['Location'].append(location)
                rating = driver.find_element(by=By.XPATH, value= '//*[@id="property-critical-root"]/div/div[4]/div[2]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/h3').text
                self.dict_properties['Rating/10'].append(rating)
                time.sleep(2)
            except:
                pass    
        #print(self.dict_properties)
            #driver.quit() # Close the browser when you finish  
          

    def images(self):
        for link in self.big_list[0:10]:
            driver.get(link)
            time.sleep(5)
            try:
                see_all_photos = driver.find_element(by=By.XPATH, value='//*[@id="property-critical-root"]')
                time.sleep(5)
                image = see_all_photos.find_element(by=By.XPATH, value= '//div[contains(@class, "MosaicTilestyled__MosaicTileImageStyled-sc-1f7i82h-1 ctubJh")]')
                image = image.find_element(by=By.XPATH, value= '//img')
                img = image.get_attribute('src')
                self.dict_properties['Image URL'].append(img)
            except:
                pass
               

    def timestamp(self):
        for link in self.big_list[0:10]:
            driver.get(link)
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.dict_properties['Timestamp'].append(date)
         

    def unique_id(self):
        for link in self.big_list[0:10]:
            driver.get(link)
            id = str(uuid.uuid4()) 
            self.dict_properties['ID'].append(id)   
        #print(self.dict_properties)    


    def folders(self):
        newpath = r'C:\Users\kambo\Desktop\Data-Collection-Pipeline\raw_data\hotels'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    def file(self):
        with open(r'C:\Users\kambo\Desktop\Data-Collection-Pipeline\raw_data\hotels\data.json', 'w') as f:
            json.dump(self.dict_properties,f)

     
def info():     
    crawler = Scraper()
    crawler.accept_cookie()
    #rewards = crawler.close_rewards()
    #destination = crawler.search()
    crawler.top_reviewed()
    crawler.scroller()
    crawler.links_of_hotels()
    crawler.crawling()
    crawler.get_info()
    crawler.images()
    crawler.timestamp()
    crawler.unique_id()
    crawler.folders()
    crawler.file()
    

if __name__ == '__main__':
    info()
        
        
    




    


    
        


