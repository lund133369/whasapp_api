from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')