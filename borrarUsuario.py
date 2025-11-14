import customtkinter as ctk
import os
from config import usuarios

class BorrarUsuario(ctk.CTkFrame):
  def __init__(self, parent, controller):
    self.controller = controller
    super().__init__(parent, fg_color="#2b303b")
    self.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(self, text="Borrar Usuario", font=("Arial", 24, "bold")).pack(pady=(20, 30))

    frameBorrarUsuario = ctk.CTkFrame(self, fg_color="#2b303b")
    frameBorrarUsuario.pack(pady=10)
    cedula =  ctk.CTkEntry(frameBorrarUsuario, placeholder_text="Ingrese la cedula del usuario", width=200)
    cedula.pack(side="left", padx=(0,10))
    ctk.CTkButton(frameBorrarUsuario, text="Borrar", width=100, corner_radius=10, command=lambda: self.eliminarUsuario(cedula.get())).pack(side="left")
    self.resultadoBorrarLabel = ctk.CTkLabel(self, text="", font=("Arial", 16))
    self.resultadoBorrarLabel.pack(pady=10)

  def eliminarUsuario(self, datoCedula):
    os.system('cls')
    if datoCedula.strip() == "":
      self.resultadoBorrarLabel.configure(text="Por favor ingrese un dato para buscar.")
    elif [usuario for usuario in usuarios if usuario["cedula"] == datoCedula] == []:
      self.resultadoBorrarLabel.configure(text=f"No se encontró usuario con cédula {datoCedula}.")
      print(f"No se encontró usuario con cédula {datoCedula}.")
    else:
      for usuario in usuarios:
        if usuario["cedula"] == datoCedula:
          usuarios.remove(usuario)
          self.resultadoBorrarLabel.configure(text=f"Usuario con cédula {datoCedula} eliminado.")
          print(f"Usuario con cédula {datoCedula} eliminado.")