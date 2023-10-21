class Persona:
    
    def __init__(self, id,nombre,correo,contrasena):
        self.id = id
        self.nombre= nombre
        self.correo= correo
        self.contrasena = contrasena

    def verPersona(self):
        print(f"ID: {self.id}\n",f"Nombre: {self.nombre}\n",f"Correo: {self.correo}\n")



