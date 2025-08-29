from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



chrome_driver_path= r"C:\development\chromedriver-win64\chromedriver.exe"
service= Service(chrome_driver_path)

options= Options()
options.add_experimental_option("detach", True)


driver= webdriver.Chrome(service= service, options= options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
voters= driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[1]/a')
print(voters.text)