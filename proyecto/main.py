#
#       ESTE PYTHON NO FUNCIONA TODAVIA , EL OTRO MAIN.IPYNB SI
#


from helper.correo import *
from helper.whastapp import *
from helper.linux import *
import time

email = EmailSender()
linux = Linux()
whatsapp = Whatsapp()

whatsapp.extract_qr_code()

email.enviar_correo('ehuamani17@autonoma.edu.pe','Envio QR', 'este es tu qr dura menos de 1 minutos' ,'barcode_whatsapp.png' )

while True:
    time.sleep(10)
    estado_memoria = linux.get_memory_status()
    estado_disco = linux.get_disk_status()
    estado_process = linux.get_processes_list()

    whatsapp.send_message('you',"hola test")
    time.sleep(10)