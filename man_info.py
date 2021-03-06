import csv
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

if __name__ == "__main__":
    driver = webdriver.Chrome('chromedriver.exe')
    start_url = 'https://fr.dacia.be/trouvez-votre-concessionnaire.html'
    driver.get(start_url)
    time.sleep(5)

    zip_codes = ['Knokke-Heist','Bruges','Ostend','De panne','Ghent','Kortrijk','Brussels','Leuven','Mons','charleroi','Namur','Arlon','Bastogne','Rochefort','Malmedy','Genk']
    # with open("zip_code_swi_all.csv", 'r', encoding='utf-8-sig') as fr:
    #     reader = csv.reader(fr)
    #     for row in reader:
    #         zip_codes.append(row[0])

    for zip in zip_codes:
        driver.find_element_by_css_selector('#textfield').clear()
        driver.find_element_by_css_selector('#textfield').send_keys(zip)
        time.sleep(5)
        try:
            driver.find_elements_by_css_selector('.TextFieldCombo__itemButton')[0].click()
            time.sleep(5)
        except:
            time.sleep(3)
        # time.sleep(10)
        # driver.find_element_by_css_selector('.search-cta').click()
        # time.sleep(3)
        try:
            points = driver.find_elements_by_css_selector('.DealerList__address.DealerList__name.is-clickable')
        except:
            time.sleep(5)
        print(len(points))
        for i in points:
            i.click()
            time.sleep(5)
            position_title = driver.find_element_by_css_selector(".DealerDetails__name").text
            address1 = driver.find_elements_by_css_selector('.DealerDetails__address')[0].text
            address2 = driver.find_elements_by_css_selector('.DealerDetails__address')[1].text
            address = address1 + "  " + address2
            try:
                phone = driver.find_element_by_css_selector('.DealerDetails__link.DealerDetails__phone.DealerDetails__phoneNumber').get_attribute('href')
            except:
                phone = ""
            services = []
            service_elements = driver.find_elements_by_css_selector('.DealerDetails__service')
            for j in service_elements:
                services.append(j.text)
            driver.find_element_by_css_selector('.DealerDetails__header').click()
            time.sleep(2)
            # if position_title == "":
            #     position_title = i.get_attribute("title")
            # if len(position_title) < 3:
            #     continue
            with open("Belgium.csv", 'a', encoding='utf-8-sig', newline='') as fw:
                writer = csv.writer(fw, lineterminator='\n')
                temp = []
                temp.append(position_title)
                temp.append(address)
                temp.append(phone)
                for k in services:
                    temp.append(k)
                writer.writerow(temp)