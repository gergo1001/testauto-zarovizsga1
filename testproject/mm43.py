from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

driver.get(URL)


# visszaadja a hibaüzenetet, de csak akkor ha látszik. Ha nincs hibaüzenet, vagy nem látszik, akkor üressel tér vissza
def fill_email(email):
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("submit").click()
    validation_errors = driver.find_elements_by_class_name("validation-error")
    if len(validation_errors) < 1:
        return ""
    else:
        if validation_errors[0].is_enabled():
            return validation_errors[0].text
        else:
            return ""


# TC01
assert "" == fill_email("teszt@elek.hu")
# TC02
assert 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.' == fill_email("teszt@")
# TC03
assert 'Kérjük, töltse ki ezt a mezőt.' == fill_email("")

driver.close()
