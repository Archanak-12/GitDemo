from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("Archana")
driver.find_element_by_css_selector(".password").send_keys("Kumari")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
# //tagname[text()='xxx']
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)