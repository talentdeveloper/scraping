import csv
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

if __name__ == "__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    start_url = 'https://dacia.no/forhandlere'
    driver.get(start_url)
    time.sleep(5)

    zip_codes = driver.find_elements_by_css_selector('.county>ul>li')

    for zip in zip_codes:
        zip.click()
        time.sleep(5)
        name = driver.find_element_by_css_selector('.container.ng-scope>h2').text
        contents = driver.find_elements_by_css_selector('.container.ng-scope>ul>li')
        address = ""
        postaddress = ""
        email = ""
        phone = ""
        website = ""
        for j in contents:
            if "Adresse:" in j.get_attribute('innerHTML'):
                address = j.get_attribute('innerHTML').split("</span>")[1]
            if "Postnr" in j.get_attribute('innerHTML'):
                postaddress = j.get_attribute('innerHTML').split("</span>")[1]
            if "E-post" in j.get_attribute('innerHTML'):
                email = j.get_attribute('innerHTML').split("</span>")[1]
            if "Tlf" in j.get_attribute('innerHTML'):
                phone = j.get_attribute('innerHTML').split("</span>")[1].split('>')[1].split('<')[0]
            if "Nettside" in j.get_attribute('innerHTML'):
                website = j.get_attribute('innerHTML').split("</span>")[1].split('>')[1].split('<')[0]
        with open("Norway.csv", 'a', encoding='utf-8-sig', newline='') as fw:
            writer = csv.writer(fw, lineterminator='\n')
            temp = []
            temp.append(name)
            temp.append(address)
            temp.append(postaddress)
            temp.append(email)
            temp.append(phone)
            temp.append(website)
            writer.writerow(temp)