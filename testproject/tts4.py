from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"
driver.get(URL)


# time.sleep(5)
# dobok, és az utolsó dobás eredményét nézem
def dobas():
    driver.find_element_by_id("submit").click()
    return driver.find_element_by_id("lastResult").text


# tc01
# Százszor dobok, és számolom, hogy hány fej lett. Az életben valószínűleg azt is ellenőrizni kellene, hogy legalább 30 irás is legyen, de itt nem volt ez a feladat, ezért arra nincs vizsgálat
fej_db = 0
for i in range(100):
    if dobas() == "fej":
        fej_db += 1

assert fej_db >= 30

driver.close()
