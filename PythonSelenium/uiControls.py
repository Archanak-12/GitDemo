from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    # checkbox.click()
    # assert checkbox.is_selected()
    # print(checkbox.get_attribute("value"))
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# print(driver.find_element_by_id("displayed-text").is_displayed())
assert driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()

# print(driver.find_element_by_id("displayed-text").is_displayed())
assert not driver.find_element_by_id("displayed-text").is_displayed()

