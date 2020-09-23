from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
# driver.window_handles[1]
childwindow = driver.window_handles[1]
# ("parentid", "childid")
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
parentwindow = driver.window_handles[0]
driver.switch_to.window(parentwindow)

# print(driver.find_element_by_tag_name("h3").text)
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text

