import customtkinter as ctk
import json, os
from config import usuarios, regexUsuario
from crearUsuario import CrearUsuario
from buscarUsuario import BuscarUsuario
from actualizarUsuario import ActualizarUsuario
from borrarUsuario import BorrarUsuario
from descargarReporte import DescargarReporte

class SistemaRegistro:
  def __init__(self):
    self.app = ctk.CTk()
    self.app.title("Sistema de registro")
    self.app.geometry("800x500+350+180")
    self.app.resizable(False, False)

    self.app.grid_rowconfigure(0, weight=1)
    self.app.grid_columnconfigure(0, weight=0)
    self.app.grid_columnconfigure(1, weight=1)

    self.frameMenu = ctk.CTkFrame(self.app, fg_color="#5e47d1", corner_radius=0)
    self.frameMenu.grid(row=0, column=0, sticky="nsew")

    ctk.CTkLabel(self.frameMenu, text="Sistema de registro", font=("Arial", 15 ,"bold"), width=250).pack(pady=15)

    self.frameInicio = ctk.CTkFrame(self.app, fg_color="#2b303b", corner_radius=0)
    self.frameInicio.grid(row=0, column=1, sticky="nsew")

    ctk.CTkButton(self.frameMenu, text="Crear", height=40, width=190, corner_radius=5, command=lambda: self.paginas(CrearUsuario)).pack(pady=10)
    ctk.CTkButton(self.frameMenu, text="Buscar", height=40, width=190, corner_radius=5, command=lambda: self.paginas(BuscarUsuario)).pack(pady=10)
    ctk.CTkButton(self.frameMenu, text="Actualizar", height=40, width=190, corner_radius=5, command=lambda: self.paginas(ActualizarUsuario)).pack(pady=10)
    ctk.CTkButton(self.frameMenu, text="Borrar", height=40, width=190, corner_radius=5, command=lambda: self.paginas(BorrarUsuario)).pack(pady=10)
    ctk.CTkButton(self.frameMenu, text="Descargar Reporte", height=40, width=190, corner_radius=5, command=lambda: self.paginas(DescargarReporte)).pack(pady=10)
    ctk.CTkButton(self.frameMenu, text="Salir", height=40, width=190, corner_radius=5, command=self.salir).pack(pady=10)

    self.app.protocol("WM_DELETE_WINDOW", self.salir)
    self.paginas(CrearUsuario)

  def paginas(self, FrameClass):
    os.system('cls')
    for widget in self.frameInicio.winfo_children():
      widget.destroy()
    try:
      new_frame = FrameClass(self.frameInicio, self)
      new_frame.pack(fill="both", expand=True)
    except Exception as e:
      print(f"Error al cargar la página: {e}")

  def salir(self):
    os.system('cls')
    try:
      with open("usuariosGuardados.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)
        print("Usuarios guardados correctamente.")
    except Exception as e:
      print(f"Error al guardar usuarios: {e}")
    self.app.destroy()

  def ejecutar(self):
    self.app.mainloop()