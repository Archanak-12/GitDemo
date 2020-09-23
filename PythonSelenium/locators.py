from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)

# driver = webdriver.Chrome(chrome_options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element_by_name("name").send_keys("Archana")
driver.find_element_by_css_selector("input[name='name']").send_keys("Archana")
driver.find_element_by_name("email").send_keys("Kumari")

# driver.findElementByName().send_keys  -send_keys (write in Java)
driver.find_element_by_id("exampleCheck1").click()

# select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value("M")

driver.find_element_by_xpath("//input[@type='submit']").click()
# print(driver.find_element_by_class_name("alert-success").text)
# //*[contains(@class,'alert-success')] - XPath
# [class*='alert-success']  - CSS
# //input[@class='btn btn-success']
message = driver.find_element_by_class_name("alert-success").text
assert "success" in message