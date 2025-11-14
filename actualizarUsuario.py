from config import usuarios, regexUsuario
import customtkinter as ctk
import re, os

class ActualizarUsuario(ctk.CTkFrame):
  def __init__(self, parent, controller):
    self.controller = controller
    super().__init__(parent, fg_color="#2b303b")
    self.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(self, text="Actualizar Usuario", font=("Arial", 24, "bold")).pack(pady=(20, 30))

    frameActualizarUsuario = ctk.CTkFrame(self, fg_color="#2b303b")
    frameActualizarUsuario.pack(pady=10)
    self.cedulaActualizar = ctk.CTkEntry(frameActualizarUsuario, placeholder_text="Ingrese la cedula del usuario", width=200)
    self.cedulaActualizar.pack(side="left", padx=(0,10))
    ctk.CTkButton(frameActualizarUsuario, text="Buscar", width=100, corner_radius=10, command=lambda: self.actualizarDatosUsuario(self.cedulaActualizar.get())).pack(side="left")

    self.resultadoActualizar = ctk.CTkLabel(self, text="", font=("Arial", 16))
    self.resultadoActualizar.pack(pady=10)

  def actualizarDatosUsuario(self, cedula):
    os.system('cls')
    if cedula.strip() == "":
      self.resultadoActualizar.configure(text="Por favor ingrese una cédula.")
      print("Por favor ingrese una cédula.")
      return
    resultado = [usuario for usuario in usuarios if usuario["cedula"] == cedula]
    if resultado:
      for usuario in usuarios:
        if usuario["cedula"] == cedula:
          frameActualizarDatos = self.nuevoFrame(self.controller.frameInicio)
          ctk.CTkLabel(frameActualizarDatos, text="Actualizar Datos del Usuario", font=("Arial", 20)).pack(pady=10)

          nombre = ctk.CTkEntry(frameActualizarDatos, placeholder_text="Nombre", width=200)
          nombre.insert(0, usuario["nombre"])
          nombre.pack(pady=10)
          apellido = ctk.CTkEntry(frameActualizarDatos, placeholder_text="Apellido", width=200)
          apellido.insert(0, usuario["apellido"])
          apellido.pack(pady=10)
          correo = ctk.CTkEntry(frameActualizarDatos, placeholder_text="Correo", width=200)
          correo.insert(0, usuario["correo"])
          correo.pack(pady=10)
          telefono = ctk.CTkEntry(frameActualizarDatos, placeholder_text="Telefono", width=200)
          telefono.insert(0, usuario["telefono"])
          telefono.pack(pady=10)

          ctk.CTkButton(frameActualizarDatos, text="Guardar Cambios", width=200, corner_radius=10, command=lambda: self.guardarCambiosUsuario(usuario, nombre.get(), apellido.get(), correo.get(), telefono.get())).pack(pady=20)
          self.resultadoActualizarLabel = ctk.CTkLabel(frameActualizarDatos, text="", font=("Arial", 16))
          self.resultadoActualizarLabel.pack(pady=10)
          break
    else:
      self.resultadoActualizar.configure(text=f"No se encontró usuario con cédula {cedula}.")
      print(f"No se encontró usuario con cédula {cedula}.")

  def nuevoFrame(self, frame):
    for w in frame.winfo_children():
      w.destroy()
    frame = ctk.CTkFrame(frame, fg_color="#2b303b", corner_radius=0)
    frame.pack(fill="both", expand=True)
    return frame

  def guardarCambiosUsuario(self, usuario, nombre, apellido, correo, telefono):
    os.system('cls')
    if nombre and apellido and correo and telefono:
      if re.match(regexUsuario["nombre"], nombre) and re.match(regexUsuario["apellido"], apellido) and re.match(regexUsuario["correo"], correo) and re.match(regexUsuario["telefono"], telefono):
        usuario["nombre"] = nombre
        usuario["apellido"] = apellido
        usuario["correo"] = correo
        usuario["telefono"] = telefono
        self.controller.paginas(ActualizarUsuario)
      else:
        print("Datos invalidos")
        self.resultadoActualizarLabel.configure(text="Datos invalidos. Por favor verifique la informacion ingresada.")
    else:
      print("Por favor complete todos los campos")
      self.resultadoActualizarLabel.configure(text="Por favor complete todos los campos.")
