# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:11:21 2019

@author: mathe
"""



import csv
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

def write_csv(pagedata):
    with open('UK.csv', 'w',encoding='utf-8-sig', newline='') as csvFile:
        fields = pagedata[0].keys()
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        for data in pagedata:
            writer.writerow(data)
    csvFile.close()
if __name__ == "__main__":
    options=webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(chrome_options=options,executable_path='C:/Users/mathe/.spyder-py3/chromedriver.exe')
    start_url = 'https://www.dacia.co.uk/find-a-dealer/find-a-dealer-listing.html'
    pagedata=[]
    driver.get(start_url)
    nextpage= True
    while nextpage:
        while len(driver.find_elements_by_css_selector('.DynamicDealerList__Dealer .DynamicDealerList__DealerName'))==0 or len(driver.find_elements_by_css_selector('.LoaderBar.is-visible'))>0:
            print('Waiting..')
            time.sleep(0.3)
           
        elems=driver.find_elements_by_css_selector('div.DynamicDealerList__Dealer')
        
        
        
        for elem in elems:
                        
            carddetail={'name':elem.find_element_by_css_selector('.DynamicDealerList__DealerName').text,
                        'address':elem.find_element_by_css_selector('.DynamicDealerList__DealerAdress').text,
                        'city':elem.find_element_by_css_selector('.DynamicDealerList__DealerCity').text,
                        'phone':elem.find_element_by_css_selector('.DynamicDealerList__DealerPhone').text}
            
            
            pagedata.append(carddetail)
            
        nextpage=len(driver.find_elements_by_css_selector('.rc-pagination-next'))>0 and len(driver.find_elements_by_css_selector('.rc-pagination-disabled.rc-pagination-next'))==0
        if nextpage:
            driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element_by_css_selector('.rc-pagination-next'))
            time.sleep(0.2)

            driver.find_element_by_css_selector('.rc-pagination-next').click()
            time.sleep(0.2)
    write_csv(pagedata)
    driver.quit()
            
