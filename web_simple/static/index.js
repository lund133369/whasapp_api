function obtener_qr_whastapp() {
  try {
    const img_element = document.getElementById("mi_qr");

    if (!img_element) {
      throw new Error("no se pudo cargar la imagen");
    }

    img_element.src = "http://127.0.0.1:5000/api/obtener_imagen";
  } catch (error) {
    console.error("Error al asignar iamgen ", error);
  }
}

async function listar_contactos() {
  const lista_conctatos = document.getElementById("list_conctactos");

  lista_conctatos.innerHTML = " ";

  const palabra = document.getElementById("palabra");
  let url_api = "http://127.0.0.1:5000/api/listar_contactos/" + palabra.value;
  console.log(url_api);

  let response = await fetch(url_api);

  let data = await response.json();

  console.log(data);

  data.forEach((element) => {
    let option = document.createElement("option");

    option.textContent = element;
    option.value = element;

    lista_conctatos.appendChild(option);
  });
}

async function enviar_mensaje() {
  let contato_1 = document.getElementById("list_conctactos").value;
  let mensaje_1 = document.getElementById("mensaje").value;

  let url_api = "http://127.0.0.1:5000/api/enviar_mensaje_contacto";

  let response = await fetch(url_api, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"  // Especifica que el contenido es JSON
      },
    body: JSON.stringify({
      contacto: contato_1,
      mensaje: mensaje_1,
    }),
  });

  if (!response.ok) {
    throw new Error(`Error en la respuesta: ${response.status}`);
  }

  let data = response.json();

  console.log(data , " --- estatus " , response.status)

}
