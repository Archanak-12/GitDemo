from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)

# tagemane - iframe, frameset, frame
driver.get("https://the-internet.herokuapp.com/iframe")
# frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
