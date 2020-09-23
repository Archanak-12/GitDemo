from selenium import webdriver
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)
# ActionChains
# driver.get("https://www.familysearch.org/en/")
# action = ActionChains(driver)
# action.move_to_element(driver.find_element_by_id("search")).perform()
#
# action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
text = alert.text
assert "You double clicked me!!!, You got to be kidding me" == text

alert.accept()