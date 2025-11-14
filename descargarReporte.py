import customtkinter as ctk
import json, os
from config import usuarios

class DescargarReporte(ctk.CTkFrame):
  def __init__(self, parent, controller):
    self.controller = controller
    super().__init__(parent, fg_color="#2b303b")
    self.grid_columnconfigure(0, weight=1)

    ctk.CTkLabel(self, text="Descargar Reporte", font=("Arial", 24, "bold")).pack(pady=(20, 30))

    ctk.CTkButton(self, text="Descargar", width=200, corner_radius=10, command=lambda: self.generarArchivo()).pack(pady=10)
    self.resultadoDescargaLabel = ctk.CTkLabel(self, text="", font=("Arial", 16))
    self.resultadoDescargaLabel.pack(pady=10)

  def generarArchivo(self):
    rutaDescargas = os.path.join(os.path.expanduser("~"), "Downloads")
    nombreArchivo = "reporteUsuarios.txt"
    rutaCompleta = os.path.join(rutaDescargas, nombreArchivo)

    try:
      with open(rutaCompleta, 'w', encoding='utf-8') as archivo:
        archivo.write("\t\t--- REPORTE DE USUARIOS ---\n\n")
        archivo.write(f"\tTotal de usuarios registrados: {len(usuarios)}\n\n")
        for i, usuario in enumerate(usuarios):
          archivo.write(f"\tUsuario {i + 1}\n")
          archivo.write(f"\t     Nombre: {usuario['nombre']}\n")
          archivo.write(f"\t     Apellido: {usuario['apellido']}\n")
          archivo.write(f"\t     Cédula: {usuario['cedula']}\n")
          archivo.write(f"\t     Correo: {usuario['correo']}\n")
          archivo.write(f"\t     Teléfono: {usuario['telefono']}\n")
          archivo.write("\t" + "-" * 45 + "\n")
      print(f"Archivo generado exitosamente en: {rutaCompleta}")
      self.resultadoDescargaLabel.configure(text=f"Archivo generado exitosamente en la carpeta de Descargas.")
    except FileNotFoundError:
      print(f"Error: La carpeta de Descargas no fue encontrada. Asegúrate de que existe.")
      self.resultadoDescargaLabel.configure(text=f"Error: La carpeta de Descargas no fue encontrada.")
    except Exception as e:
      print(f"Ocurrió un error al escribir el archivo: {e}")
      self.resultadoDescargaLabel.configure(text=f"Ocurrió un error al escribir el archivo: {e}")