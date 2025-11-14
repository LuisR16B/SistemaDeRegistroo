import customtkinter as ctk
import re, os
from usuario import Usuario
from config import usuarios, regexUsuario
import pywhatkit

class CrearUsuario(ctk.CTkFrame):
  def __init__(self, parent, controller):
    self.controller = controller
    super().__init__(parent, fg_color="#2b303b")
    self.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(self, text="Crear Nuevo Usuario", font=("Arial", 24, "bold")).pack(pady=(20, 30))

    self.nombre = ctk.CTkEntry(self, placeholder_text="Nombre (ej: Juan)", width=250, corner_radius=8)
    self.nombre.pack(pady=10)
    self.apellido = ctk.CTkEntry(self, placeholder_text="Apellido (ej: Perez)", width=250, corner_radius=8)
    self.apellido.pack(pady=10)
    self.cedula = ctk.CTkEntry(self, placeholder_text="Cédula (ej: 12345678)", width=250, corner_radius=8)
    self.cedula.pack(pady=10)
    self.correo = ctk.CTkEntry(self, placeholder_text="Correo (ej: ejemplo@dominio.com)", width=250, corner_radius=8)
    self.correo.pack(pady=10)
    self.telefono = ctk.CTkEntry(self, placeholder_text="Teléfono (ej: +1234567890)", width=250, corner_radius=8)
    self.telefono.pack(pady=10)
    ctk.CTkButton(self, text="Crear Usuario", width=250, height=40, corner_radius=10, command=self.guardarUsuario).pack(pady=20)

    self.resultadoLabel = ctk.CTkLabel(self, text="", font=("Arial", 16))
    self.resultadoLabel.pack(pady=10)

  def guardarUsuario(self):
    os.system('cls')
    nombre = self.nombre.get().strip()
    apellido = self.apellido.get().strip()
    cedula = self.cedula.get().strip()
    correo = self.correo.get().strip()
    telefono = self.telefono.get().strip()

    if nombre and apellido and cedula and correo and telefono:
      coincidencias = [usuario for usuario in usuarios if usuario['cedula'] == cedula]
      if coincidencias:
        print("La cedula ya esta registrada.")
        self.resultadoLabel.configure(text=f"Usuario con cédula {cedula} ya esta registrado.")
        return
      if re.match(regexUsuario["nombre"], nombre) and re.match(regexUsuario["apellido"], apellido) and re.match(regexUsuario["cedula"], cedula) and re.match(regexUsuario["correo"], correo) and re.match(regexUsuario["telefono"], telefono):
        usuarios.append(Usuario(nombre, apellido, cedula, correo, telefono).to_dict())
        self.nombre.delete(0, 'end')
        self.apellido.delete(0, 'end')
        self.cedula.delete(0, 'end')
        self.correo.delete(0, 'end')
        self.telefono.delete(0, 'end')
        print("Usuario creado exitosamente.")
        self.resultadoLabel.configure(text="Usuario creado exitosamente.")
        self.enviar_mensaje(nombre, telefono)
      else:
        print("Datos invalidos")
        self.resultadoLabel.configure(text="Datos invalidos. Por favor verifique la informacion ingresada.")
    else:
      print("Por favor complete todos los campos")
      self.resultadoLabel.configure(text="Por favor complete todos los campos.")

  def enviar_mensaje(self, nombre, numero):
    pywhatkit.sendwhatmsg_instantly(numero, f"Hola {nombre}, su registro en el sistema a sido con exito")