from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"

driver.get(URL)


# id alapján megkeresem a mezőket, kitörlöm, majd kitöltöm. Utána megnyomom a gombot, az eredményt adja vissza a függvény
def fill_form(param_a, param_b):
    a = driver.find_element_by_id("a")
    b = driver.find_element_by_id("b")
    a.clear()
    a.send_keys(param_a)
    b.clear()
    b.send_keys(param_b)
    driver.find_element_by_id("submit").click()
    return driver.find_element_by_id("result").text


# TC01
assert fill_form("99", "12") == "222"
# TC02
assert fill_form("kiskutya", "12") == "NaN"
# TC03
assert fill_form("", "") == "NaN"

driver.close()
