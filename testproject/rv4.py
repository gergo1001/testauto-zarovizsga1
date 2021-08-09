from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"

driver.get(URL)


# visszaadja a 2 lista különbségét. A városokonál " jelek szerepelnek, ezért azzal kiegészíti a generáltat
def kulonbseg(generalt_varosok, varosok):
    for varos in varosok:
        volt = False
        for gvaros in generalt_varosok:
            if varos.replace('"', '') == gvaros.text:
                volt = True
                break
        if not volt:
            return varos.replace('"', '')
    return ""


# lekerdezi a 2 listát
varosok = driver.find_element_by_id("cites").text.split(', ')
generalt_varosok = driver.find_elements_by_tag_name("li")

hianyzo = kulonbseg(generalt_varosok, varosok)
# a hianyzó város nevét megadja, majd gombot nyom
driver.find_element_by_id("missingCity").send_keys(hianyzo)
driver.find_element_by_id("submit").click()

# TC01
assert "Eltaláltad." == driver.find_element_by_id("result").text
driver.close()
