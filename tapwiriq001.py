from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()
browser.get('https://vol.az/')
print("Sehifeye ugurla girildi")
time.sleep(3)

browser.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/h2/a').click()
print('papulyara basildi')
time.sleep(3)
input()


# my_ul = browser.find_element(By.CLASS_NAME,'mp3ul')
#
# for i in my_ul.find_elements(By.TAG_NAME,'li'):
#     print(i.text[:-4])
#      time.sleep(5)
#     button = browser.find_element(by=By.LINK_TEXT,value=i.text)
#     button.click()
#     time.sleep(3)
#
#
# # element = browser.find_element(By.CSS_SELECTOR,'a')
# # href_value = [i.get_attribute('href') for i in element.get_attribute('a')]
# # print("Href value:", href_value)
#links = browser.find_elements(By.TAG_NAME,'a')
for i in browser.find_elements(By.XPATH,'/html/body/div[2]/div[1]/div[2]/ul'):
    print(i.text[:-4])
    i.click()
print('Cixildi')
browser.quit()
