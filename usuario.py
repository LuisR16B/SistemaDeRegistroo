class Usuario:
  def __init__(self, nombre, apellido, cedula, correo, telefono):
    self.nombre = nombre
    self.apellido = apellido
    self.cedula = cedula
    self.correo = correo
    self.telefono = telefono
  def to_dict(self):
    return {"nombre": self.nombre, "apellido": self.apellido, "cedula": self.cedula, "correo": self.correo, "telefono": self.telefono }