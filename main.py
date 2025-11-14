# Realizar en python un sistema de registro de clientes

# En este sistema podras navegar por un menu y decidir:
# - Crear un usuario
# - Buscar en la lista de usuarios (Retornar varios segun lo que se busque)
# - Actualizar un usuario
# - Borrar un usuario

# Un usuario tiene:
# - Nombre
# - Apellido
# - Cedula
# - Correo
# - Numero de telefono

# Los usuarios deben de ser almacenados y leidos de un archivo .TXT

# Hay distintas cosas que puedes hacer con el archivo para lograr este ejercicio, como:
# - Guardar un .json dentro del .TXT o directamente crear un archivo JSON
# - Guardar un usuario por linea (asi cada linea es un usuario)

# Al registrar un usuario debes de enviarle un whatsapp de bienvenida.

# Opcional:
# - Enviar un correo electronico al usuario que se registra
# - Buscar alguna libreria para crear una interfaz grafica para el software
# - Crear un .exe del programa

# Nota: todos los datos ingresados por el usuario deben de estar validados con Regex.

# Fecha de entrega: 12/11/25

from interfaz import SistemaRegistro

if __name__ == "__main__":
  SistemaRegistro().ejecutar()