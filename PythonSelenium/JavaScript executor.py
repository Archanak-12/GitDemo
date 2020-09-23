# Js DOM can access any elements on web page just like how selenium does
# selenium have a method to execute javascript code in it
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
# There are purely javascript
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
# arguments[0].click() - belongs to javascript DOM but not an selenium
driver.execute_script("arguments[0].click();", shopButton)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")