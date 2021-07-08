from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mail

def main():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    idElement = 'testId-ProductLandingContainer-totalResults'
    textChange = "Resultados (8)"

    try:
        driver.get("https://www.falabella.com.co/falabella-co/category/cat4920940/Computadores-Gaming")

        element = driver.find_element_by_id(idElement)

        print(f'Tracked id: {idElement} ')
        print(f'Tracked Text: {element.text} ')

    except Exception as e:
        print(f'An Error has occurred: \n {e} ')
    else:
        # If there is a change in the object
        if element.text != textChange:
            print("Good News")
            #mail.send()
        else:
            print("Bad News")
    finally:
        print("Program ending")

main()