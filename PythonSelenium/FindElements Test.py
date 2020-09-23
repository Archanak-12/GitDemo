import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)
# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.find_element_by_id("autosuggest").send_keys("ind")
# time.sleep(2)
# # li[class='ui-menu-item'] a  use for css
# countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
# print(len(countries))
# for country in countries:
#     if country.text == "India":
#         country.click()
#         break
# print(driver.find_element_by_id("autosuggest").text)
# assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"


driver.get("https://www.makemytrip.com/")
# driver.find_element_by_id("fromCity").click()
# driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
time.sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text == "Del Rio, United States":
        city.click()
        break
driver.find_element_by_xpath("//p[text()='Delhi, India']").click()

