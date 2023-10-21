class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Declaración de una variable de instancia privada
        self.__edad = edad  # Declaración de una variable de instancia privada

    @property
    def nombre(self):
        return self.__nombre
        # Método getter (propiedad) para obtener el valor del nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        # Método setter para modificar el valor del nombre

    @property
    def edad(self):
        return self.__edad
        # Método getter (propiedad) para obtener el valor de la edad

    @edad.setter
    def edad(self, new_edad):
        self.__edad = new_edad
        # Método setter para modificar el valor de la edad

nombre = input("Insegresa el nombre: ")
edad = int(input("Ingresa la edad: "))
persona = Persona(nombre,edad)  # Creación de una instancia de la clase Persona

nombre = persona.nombre  # Llamamos al método getter para obtener el nombre de la persona
edad = persona.edad  # Llamamos al método getter para obtener la edad de la persona

print(f"Nombre: {nombre}, Edad: {edad}")

persona.nombre =  input("Insegresa el nombre de la nueva persona: ") # Llamamos al método setter para modificar el nombre de la persona
persona.edad = int(input("Ingresa la edad de la nueva persona: "))  # Llamamos al método setter para modificar la edad de la persona

nombre = persona.nombre  # Llamamos nuevamente al método getter para obtener el nuevo nombre
edad = persona.edad  # Llamamos nuevamente al método getter para obtener la nueva edad

print(f"Nuevo Nombre: {nombre}, Nueva Edad: {edad}")
