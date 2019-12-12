# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:24:30 2019

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
    with open('Finland.csv', 'w',encoding='utf-8-sig', newline='') as csvFile:
        fields = pagedata[0].keys()
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        for data in pagedata:
            writer.writerow(data)
    csvFile.close()
if __name__ == "__main__":
    options=webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    # driver = webdriver.Chrome(chrome_options=options,executable_path='C:/Users/mathe/.spyder-py3/chromedriver.exe')
    driver = webdriver.Chrome('./chromedriver.exe')
    start_url = 'https://www.dacia.fi/jalleenmyyjat/'
    driver.get(start_url)
    
    while len(driver.find_elements_by_css_selector('iframe'))==0:
        print('Waiting..')
    
    map_url=None
    for elem in driver.find_elements_by_css_selector('iframe'):
        if 'map.' in elem.get_attribute('src'):
            driver.get(elem.get_attribute('src'))
            break
        
    while len(driver.find_elements_by_css_selector('ul#placesList li.place'))==0:
        print('Waiting..')
    time.sleep(2)
        
    for i in range(20):
        driver.find_elements_by_css_selector('.gmnoprint .gm-control-active')[1].click()
        time.sleep(0.2)
    
    elems=driver.find_elements_by_css_selector('ul#placesList li.place')
    
    pagedata=[]
    
    for elem in elems:
        elem.click()
        time.sleep(0.2)
        details=[]
        for card in driver.find_elements_by_css_selector('#placeDetails h6'):
            row=''.join([i for i in card.text if i in string.printable])
            if len(row.strip())>0:
                details.append(row)
                
        carddetail={'name':details[0],'addressline1':details[1],'addressline2':details[2],'addressline3':'','addressline4':''}
        idx='addressline'
        for i in range(3,len(details)):
            idx='website' if re.search(regex_web,details[i]) else idx
            idx='Automyynti' if 'Automyynti' in details[i] else idx
            idx='Huolto_ja_varaosat' if 'varaosat' in details[i] else idx
            idx=idx+'email'if re.search(regex_email,details[i]) and 'email' not in idx else idx
            idx=idx+'phone'if re.search(regex_phone,details[i]) and 'phone' not in idx else idx
            idx=idx+str(i) if 'address' in idx else idx
            carddetail[idx]=details[i]
        pagedata.append(carddetail)
    write_csv(pagedata)
    driver.quit()
            
            
            