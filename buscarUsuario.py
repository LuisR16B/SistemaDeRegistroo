import customtkinter as ctk
import os
from config import usuarios

class BuscarUsuario(ctk.CTkFrame):
  def __init__(self, parent, controller):
    self.controller = controller
    super().__init__(parent, fg_color="#2b303b")
    self.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(self, text="Buscar Usuario", font=("Arial", 24, "bold")).pack(pady=(20, 30))

    frameBuscarUsuario = ctk.CTkFrame(self, fg_color="#2b303b")
    frameBuscarUsuario.pack(pady=10)
    buscandoUsuario = ctk.CTkEntry(frameBuscarUsuario, placeholder_text="Ingrese nombre, apellido o cedula", width=200)
    buscandoUsuario.pack(side="left", padx=(0,10))
    ctk.CTkButton(frameBuscarUsuario, text="Buscar", width=100, corner_radius=10, command=lambda: self.realizandobusqueda(buscandoUsuario.get())).pack(side="left")

    self.mostrarResultadosFrame = ctk.CTkScrollableFrame(self, fg_color="#2b303b", width=400, height=300)
    self.mostrarResultadosFrame.pack(pady=10, fill="x", padx=20)

  def realizandobusqueda(self, datoBusqueda):
    os.system('cls')
    for widget in self.mostrarResultadosFrame.winfo_children():
      widget.destroy()
    if datoBusqueda.strip() == "":
      ctk.CTkLabel(self.mostrarResultadosFrame, text="Por favor ingrese un dato para buscar.", font=("Arial", 16, "bold")).pack(pady=20)
      return
    resultados = [usuario for usuario in usuarios if usuario["nombre"].lower().startswith(datoBusqueda.lower().strip()) or usuario["apellido"].lower().startswith(datoBusqueda.lower().strip()) or usuario["cedula"].lower().startswith(datoBusqueda.lower().strip())]

    if resultados:
      ctk.CTkLabel(self.mostrarResultadosFrame, text=f"Se encontraron {len(resultados)} usuario(s):", font=("Arial", 16, "bold")).pack(pady=10)
      for usuario in resultados:
        frameUsuario = ctk.CTkFrame(self.mostrarResultadosFrame, fg_color="#3c414c")
        frameUsuario.pack(fill="x", pady=5, padx=10)
        ctk.CTkLabel(frameUsuario, text=f"Nombre: {usuario['nombre']} {usuario['apellido']}", font=("Arial", 14)).pack(anchor="w", padx=10, pady=(5, 2))
        ctk.CTkLabel(frameUsuario, text=f"Cédula: {usuario['cedula']}", font=("Arial", 14)).pack(anchor="w", padx=10, pady=2)
        ctk.CTkLabel(frameUsuario, text=f"Correo: {usuario['correo']}", font=("Arial", 14)).pack(anchor="w", padx=10, pady=2)
        ctk.CTkLabel(frameUsuario, text=f"Teléfono: {usuario['telefono']}", font=("Arial", 14)).pack(anchor="w", padx=10, pady=(2, 5))
      print(f"Se encontraron {len(resultados)} usuario(s).")
    else:
      ctk.CTkLabel(self.mostrarResultadosFrame, text="No se encontraron usuarios que coincidan con la búsqueda.", font=("Arial", 16, "bold")).pack(pady=20)
      print("Usuarios no encontrados.")