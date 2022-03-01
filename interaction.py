from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



service = Service("/Users/coreyaugburn/Desktop/CodeProjectspy/chromedriver")

driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

wiki_num = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(wiki_num.text)

# wiki_num.click()

# to click links
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# typing into search bar
search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)





# driver.quit()