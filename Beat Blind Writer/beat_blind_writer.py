from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


driver_path = 'C:\\Users\\lenovo\\Desktop\\ahmet\\Python\\CromeDriver\\chromedriver.exe'
serv_obj = Service(driver_path)

# this option code is needed to disable info part
ch_options = webdriver.ChromeOptions()
ch_options.add_experimental_option("useAutomationExtension", False)
ch_options.add_experimental_option(
    'excludeSwitches', ['enable-logging', 'enable-automation'])
driver = webdriver.Chrome(service=serv_obj, options=ch_options)

driver.maximize_window()
# insert blind Writer Page into there to be able to run program
# driver.get('')
driver.implicitly_wait(10)

typeBox = driver.find_element("xpath", '//*[@id="typeBox"]')


words = driver.find_elements(By.CLASS_NAME, "wordBox")

for i in words:
    if i.text == "":
        sleep(2)
    typeBox.send_keys(i.text + " ")
