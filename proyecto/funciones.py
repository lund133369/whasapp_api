from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import base64
import time
import os

class Whatsapp_web:


    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--blink-settings=imagesEnabled=true")
        options.add_argument("--disable-blink-features=AutomationControlled")
      
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)
        self.first_message = True

    def extract_qr_code(self,name_barcode="./barcode/barcode_1.png"):
        try:
            self.driver.get("https://web.whatsapp.com/")
            qr_element = WebDriverWait(self.driver,60).until(
                EC.presence_of_element_located((By.TAG_NAME,'canvas'))
            )
            qr_canvas = self.driver.find_element(By.TAG_NAME,'canvas')
            qr_base64 = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(22);",qr_canvas)
            qr_file_path = name_barcode
            with open(qr_file_path,'wb') as qr_file:
                qr_file.write(base64.b64decode(qr_base64))

            return True
            
        except Exception  as e:
            self.driver.save_screenshot('./barcode/error_buscar_contacto.png')
            print(f"Error: {e}")
            return e

    def buscar_contacto(self,contact):
        try:

            print("")
            time.sleep(2)

            search_box = WebDriverWait(self.driver , 60).until(
                EC.presence_of_element_located((By.XPATH,"//div[@contenteditable='true'][@data-tab='3']"))
            )

            # Hace clic en el campo de búsqueda para enfocarlo.
            search_box.click()
            # Selecciona todo el texto dentro del campo de búsqueda usando Ctrl + A.
            search_box.send_keys(Keys.CONTROL + "a")
            # Borra el texto seleccionado enviando la tecla de retroceso (Backspace).
            search_box.send_keys(Keys.BACKSPACE)
            
            search_box.send_keys(contact)
            search_box.send_keys(u'\ue007')

     
            time.sleep(5)

            spans = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//span[@dir="auto" and @title]'))
            )


            # Construir una lista con el formato deseado
            formatted_spans = [f'{span.get_attribute("title")}' for span in spans]

            print(formatted_spans)

            return formatted_spans
          
        except Exception  as e:
            self.driver.save_screenshot('./barcode/error_buscar_contacto.png')
            print(f"Error: {e}")
            return e


    # esto no es nesesario si el contacto es unico
    # pero si son varios se debe colocar el nombre exacto 
    def enviar_mensaje(self,contact_name,message,delay_minutes=0):
        try:
            contact_xpath = f"//span[@title='{contact_name}']"
            contact = WebDriverWait(self.driver , 60).until(
                EC.presence_of_element_located((By.XPATH,contact_xpath))
            )
            print(1)
            contact.click() #click 

            time.sleep(2)
            print(2)
            message_box = WebDriverWait(self.driver , 60).until(
                EC.presence_of_element_located((By.XPATH,"//div[@contenteditable='true'][@data-tab='10']"))
            )
            print(3)
            # Introduce un retraso en minutos
            if delay_minutes > 0:
                print(f"Esperando {delay_minutes} minutos antes de enviar el mensaje...")
                time.sleep(delay_minutes * 60)  # Convierte minutos a segundos
            print(4)       
            message_box.send_keys(message) #escribir mensaje
            print(5)
            message_box.send_keys(u'\ue007') #dar enter

            return True
        except Exception  as e:
            self.driver.save_screenshot('./barcode/error_enviar_mensaje.png')
            print(f"Error: {e} ")
            print(type(e))
            return False