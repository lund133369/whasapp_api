from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import base64
import time
import os

class Whatsapp:

    def __init__(self):

        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--blink-settings=imagesEnabled=true")
        options.add_argument("--disable-blink-features=AutomationControlled")
      


        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)

        self.first_message = True

    def extract_qr_code(self):
        self.driver.get("https://web.whatsapp.com/")
        qr_element = WebDriverWait(self.driver,60).until(
            EC.presence_of_element_located((By.TAG_NAME,'canvas'))
        )
        qr_canvas = self.driver.find_element(By.TAG_NAME,'canvas')
        qr_base64 = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(22);",qr_canvas)
        qr_file_path = 'barcode_whatsapp.png'
        with open(qr_file_path,'wb') as qr_file:
            qr_file.write(base64.b64decode(qr_base64))

    def buscar_contacto(self,contact,message):
        try:
            if self.first_message:
                self.first_message = False
                time.sleep(10)

            search_box = WebDriverWait(self.driver , 60).until(
                EC.presence_of_element_located((By.XPATH,"//div[@contenteditable='true'][@data-tab='3']"))
            )
            search_box.clear()
            search_box.send_keys(contact)
            search_box.send_keys(u'\ue007')

        except Exception  as e:
            self.driver.save_screenshot('error.png')
            print(f"Error: {e}")


    # esto no es nesesario si el contacto es unico
    # pero si son varios se debe colocar el nombre exacto 
    def darle_click_al_contacto(self,contact_name,message):
        try:
            contact_xpath = f"//span[@title='{contact_name}']"
            contact = WebDriverWait(self.driver , 60).until(
                EC.presence_of_element_located((By.XPATH,contact_xpath))
            )

            contact.click() #click 
        except Exception  as e:
            self.driver.save_screenshot('error.png')
            print(f"Error: {e}")

    def enviar_mensaje(self,contact,message):
        try:
            message_box = WebDriverWait(self.driver , 60).until(
                EC.presence_of_element_located((By.XPATH,"//div[@contenteditable='true'][@data-tab='10']"))
            )
     
            message_box.send_keys(message) #escribir mensaje
            message_box.send_keys(u'\ue007') #dar enter
        except Exception  as e:
            self.driver.save_screenshot('error.png')
            print(f"Error: {e}")
      

if __name__ == '__main__':
    whatsapp = Whatsapp()
    whatsapp.extract_qr_code()
    
    whatsapp.buscar_contacto("you" , " test ")
    whatsapp.darle_click_al_contacto("you" , " test ")
    whatsapp.enviar_mensaje("you" , " test ")


