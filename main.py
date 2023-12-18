from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://appbrewery.github.io/Zillow-Clone/")

address_list = []
data_address = driver.find_elements(By.TAG_NAME, value="address")
for x in range(len(data_address)):
    complete_address = data_address[x].text
    address_list.append(complete_address)

price_list = []
data_price = driver.find_elements(By.CLASS_NAME, value="PropertyCardWrapper__StyledPriceLine")
for x in range(len(data_price)):
    price_tag = data_price[x].text
    price_list.append(price_tag)

link_list = []
data_link = driver.find_elements(By.CLASS_NAME, value="StyledPropertyCardDataWrapper [href]")
for x in range(len(data_link)):
    link = data_link[x].get_attribute('href')
    link_list.append(link)

#input the data into google form
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(link_list)):
    driver.get("https://forms.gle/qtj8uRUDRxWZPcJaA")
    time.sleep(2)

    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(address_list[n])
    price.send_keys(price_list[n])
    link.send_keys(link_list[n])
    submit_button.click()
  


