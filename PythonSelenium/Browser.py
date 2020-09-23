from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")

print(driver.title)
print(driver.current_url)
driver.get("https://courses.rahulshettyacademy.com/courses")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()