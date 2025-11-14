import json

regexUsuario = {
  "nombre": r"^[A-Za-z]{2,25}$",
  "apellido": r"^[A-Za-z]{2,25}$",
  "cedula": r"^\d{7,10}$",
  "correo": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
  "telefono": r"^\+?\d{10,15}$"
}

try:
  with open("usuariosGuardados.json", "r") as archivo:
    usuarios = json.load(archivo)
except FileNotFoundError:
  usuarios = []