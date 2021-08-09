from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"


def osszead(a, b):
    return a + b


def kivon(a, b):
    return a - b


def szoroz(a, b):
    return a * b


# a weboldal jelenleg nem tud osztani, de hátha fejlesztik:)
def oszt(a, b):
    if b != 0:
        return a / b
    else:
        return "Nan"


# beolvassa a weboldalt, kitölti a mezőket és kalkulál. az op mezőtöl függően elvégzi a számítást, és visszadja aszamolt, és a kiirt értéket, mindkettőt sztringként
def beolvas_es_szamol():
    driver.get(URL)
    muvelet = driver.find_element_by_id("op").text
    # azért int, mert intet generál a weboldal


num1 = int(driver.find_element_by_id("num1").text)
num2 = int(driver.find_element_by_id("num2").text)
eredmeny = 0
if (muvelet == "+"):
    eredmeny = osszead(num1, num2)
if (muvelet == "-"):
    eredmeny = kivon(num1, num2)
if (muvelet == "*"):
    eredmeny = szoroz(num1, num2)
if (muvelet == "/"):
    eredmeny = oszt(num1, num2)
driver.find_element_by_id("submit").click()
return str(eredmeny), driver.find_element_by_id("result").text

# TC01
szamolt, kiirt = beolvas_es_szamol()
assert szamolt == kiirt
