from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
validateText = "Option3"
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
# print(alert.text)
alertText = alert.text
assert validateText in alertText
alert.accept()

alert.dismiss()