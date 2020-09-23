from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension('c:/chromedriver_win32/extension_6_1_7_0.crx')
options.add_argument("--start-maximized")
options.add_argument("headless")
options.add_argument("ignore-certificate-errors")
driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\\chromedriver.exe", options=options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)