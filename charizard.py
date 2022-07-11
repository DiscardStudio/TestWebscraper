# Switch to chromedriver if you use chrome. You gotta install that if you want to use it tho.
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import random

days_in_months = {\
    "Jan": 31,\
    "Feb": 28,\
    "Mar": 31,\
    "Apr": 30,\
    "Jun": 30,\
    "Jul": 31,\
    "Aug": 31,\
    "Sep": 30,\
    "Oct": 31,\
    "Nov": 30,\
    "Dec": 31
}

months = ["Jan", "Feb", "Mar","Apr","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

month = random.randint(0,11)

options = FirefoxOptions()

#comment this out if you wanna see the browser
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
driver.get("https://pokemon-sdchpromotion.promo.eprize.com/#/register")

#Edit the first 3 if you want to. idk. I dont think theyll check anything other than email.
driver.find_element("xpath",'//*[@id="first_name"]').send_keys("test")

driver.find_element("xpath",'//*[@id="last_name"]').send_keys("test again")

driver.find_element("xpath",'//*[@id="email"]').send_keys("test@testagain.test")

#Birthday is completely randomized already
driver.find_element("xpath",'//*[@id="age_day"]').send_keys(str(random.randint(0,days_in_months[month])))

driver.find_element("xpath",'//*[@id="age_month"]').send_keys(month)

driver.find_element("xpath",'//*[@id="age_year"]').send_keys(str(random.randint(1980,2002)))


#You can figure out how you want to do the city and address, thats a little much tbh
driver.find_element("xpath",'//*[@id="address1"]').send_keys("test again")

driver.find_element("xpath",'//*[@id="city"]').send_keys("Hoboken")

driver.find_element("xpath",'//*[@id="zip"]').send_keys("07030")

driver.find_element("xpath",'//*[@id="state"]').send_keys("New Jersey")

#Didnt solve the recaptcha, thats all thats left


driver.close()