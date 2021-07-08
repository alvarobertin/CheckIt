#$$("#search_numResults")[0].textContent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.falabella.com.co/falabella-co/category/cat4920940/Computadores-Gaming")



try:
    element = driver.find_element_by_id('testId-ProductLandingContainer-totalResults')
    print(element.text)
except Exception as e:
    print(e)