# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:02:47 2019

@author: mathe
"""


import csv
from selenium import webdriver
import time,re
from selenium.webdriver.common.keys import Keys 
import string
regex_web = '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
regex_email = '(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
regex_phone = '\+?\d[\d -]{8,12}\d'


def write_csv(pagedata):
    with open('Lithuania.csv', 'w',encoding='utf-8-sig', newline='') as csvFile:
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
    start_url = 'https://www.dacia.lt/dealerlocator.html'
    driver.get(start_url)
    
    while len(driver.find_elements_by_css_selector('.tab-content'))==0:
        print('Waiting..')
        time.sleep(0.3)
    
    tab=driver.find_elements_by_css_selector('.tab-content')[1]
    time.sleep(3)
    driver.find_elements_by_css_selector('.tab-header')[1].click()
    time.sleep(0.3)
           
    while len(tab.find_elements_by_css_selector('div.dealer-info'))==0:
        print('Waiting..')
        time.sleep(0.3)
        
    elems=tab.find_elements_by_css_selector('div.dealer-info')
    
    pagedata=[]
    
    for elem in elems:
        
        details=[]
        services=','.join ([e.get_attribute('data-original-title') for e in elem.find_elements_by_css_selector('.dealer-services .ServiceIcon')])
            
        carddetail={'name':elem.find_element_by_css_selector('.dealer-name').text,
                    'addressline1':'','addressline2':'','addressline3':'','addressline4':'','services':services,
                    'phone':elem.find_element_by_css_selector('.dealer-contact-data a span.phone-number').text,'fax':elem.find_elements_by_css_selector('.dealer-contact-data span.phone-number')[1].text if len(elem.find_elements_by_css_selector('.dealer-contact-data span.phone-number'))>1 else ''}
        
        address=elem.find_elements_by_css_selector('div.dealer-contact-data span:not([class])')
        
        for i in range(len(address)):
            carddetail['addressline'+str(i+1)]=address[i].text
        
        pagedata.append(carddetail)
    write_csv(pagedata)
    driver.quit()
            
            
            