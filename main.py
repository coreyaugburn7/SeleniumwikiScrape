from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/coreyaugburn/Desktop/CodeProjectspy/chromedriver")

driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

wiki_num = driver.find_element(By.ID, "articlecount")
print(wiki_num.text)
wiki_num.click()





driver.quit()























