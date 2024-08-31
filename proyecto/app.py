from flask import Flask, jsonify, request,send_file
from flask_cors import CORS
import os
import time
from funciones import Whatsapp_web

app = Flask(__name__)

# Permite CORS para cualquier origen
CORS(app)

whatsapp_1 = Whatsapp_web()

contactos = []

# Ruta principal
@app.route('/api/', methods=['GET'])
def home():
    return jsonify({"mensaje": "Bienvenido a la API REST"}), 200

# Ruta para obtener una imagen
@app.route('/api/obtener_imagen', methods=['GET'])
def obtener_imagen():
    try:

        x = whatsapp_1.extract_qr_code("./barcode/barcode_1.png")

        print(x)

        # Especificar la ruta relativa de la imagen
        image_path = os.path.join('barcode', 'barcode_1.png')
        
        # Verificar si el archivo existe
        if not os.path.exists(image_path):
            return jsonify({"error": "Imagen no encontrada"}), 404

        # Devolver la imagen como respuesta
        return send_file(image_path, mimetype='image/png')
    except Exception as e:
        print(e , type(e))
        return "error " + e


# Ruta para listar contactos
@app.route('/api/listar_contactos/<string:string>', methods=['GET'])
def listar_contactos(string):
    try:

        contactos_final =  whatsapp_1.buscar_contacto(string)
      
        return jsonify(contactos_final), 200
    except Exception as e:
        print(e + type(e))
        return "error " +e 

# Ruta para enviar un mensaje a un contacto específico
@app.route('/api/enviar_mensaje_contacto', methods=['POST'])
def enviar_mensaje_contacto():
    try:
        data = request.get_json()
        contacto_id = data.get('contacto')
        mensaje = data.get('mensaje')
        print(contacto_id , mensaje)
        
        whatsapp_1.enviar_mensaje(contacto_id,mensaje)
    

        return jsonify({"mensaje": f"Mensaje enviado a {contacto_id}: {mensaje}"}), 200
    except Exception as e:
        print(e + type(e))
        return "error " + e

if __name__ == '__main__':
    app.run(debug=True)
