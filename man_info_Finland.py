import csv
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

if __name__ == "__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    start_url = 'https://www.dacia.fi/jalleenmyyjat/'
    driver.get(start_url)
    time.sleep(35)

    elements = driver.find_elements_by_css_selector('li.place.clearfix')
    print(len(elements))
    names = driver.find_elements_by_css_selector('li.place.clearfix>div.placeMeta>h6>strong')
    addresses1 = driver.find_elements_by_css_selector('li.place.clearfix>div.placeMeta>h6:nth-child(2)')
    addresses2 = driver.find_elements_by_css_selector('li.place.clearfix>div.placeMeta>h6:nth-child(3)')

    for i in range(0, len(elements)):
        name = names[i].text
        address1 = addresses1[i].text
        address2 = addresses2[i].text
        names[i].click()

        contents = driver.find_element_by_css_selector('#placeDetails>div').text
        print(contents)

        
        # for j in contents:
        #     if "Adresse:" in j.get_attribute('innerHTML'):
        #         address = j.get_attribute('innerHTML').split("</span>")[1]
        #     if "Postnr" in j.get_attribute('innerHTML'):
        #         postaddress = j.get_attribute('innerHTML').split("</span>")[1]
        #     if "E-post" in j.get_attribute('innerHTML'):
        #         email = j.get_attribute('innerHTML').split("</span>")[1]
        #     if "Tlf" in j.get_attribute('innerHTML'):
        #         phone = j.get_attribute('innerHTML').split("</span>")[1].split('>')[1].split('<')[0]
        #     if "Nettside" in j.get_attribute('innerHTML'):
        #         website = j.get_attribute('innerHTML').split("</span>")[1].split('>')[1].split('<')[0]
        # with open("Norway.csv", 'a', encoding='utf-8-sig', newline='') as fw:
        #     writer = csv.writer(fw, lineterminator='\n')
        #     temp = []
        #     temp.append(name)
        #     temp.append(address)
        #     temp.append(postaddress)
        #     temp.append(email)
        #     temp.append(phone)
        #     temp.append(website)
        #     writer.writerow(temp)