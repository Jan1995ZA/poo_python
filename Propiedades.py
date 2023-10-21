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

    @nombre.deleter
    def nombre(self):
        del self.__nombre
        # Método deleter para eliminar el valor del nombre

    @property
    def edad(self):
        return self.__edad
        # Método getter (propiedad) para obtener el valor de la edad

    @edad.setter
    def edad(self, new_edad):
        self.__edad = new_edad
        # Método setter para modificar el valor de la edad

    @edad.deleter
    def edad(self):
        del self.__edad
        # Método deleter para eliminar el valor de la edad

persona_uno = Persona("Juan", 28)  # Creación de una instancia de la clase Persona

nombre = persona_uno.nombre  # Llamamos al método getter para obtener el nombre de la persona
edad = persona_uno.edad  # Llamamos al método getter para obtener la edad de la persona

print(f"Nombre: {nombre}, Edad: {edad}")

persona_uno.nombre = "Pepe"  # Llamamos al método setter para modificar el nombre de la persona
persona_uno.edad = 30  # Llamamos al método setter para modificar la edad de la persona

nombre = persona_uno.nombre  # Llamamos nuevamente al método getter para obtener el nuevo nombre
edad = persona_uno.edad  # Llamamos nuevamente al método getter para obtener la nueva edad

print(f"Nuevo Nombre: {nombre}, Nueva Edad: {edad}")

# Ejemplo de uso de deleter para eliminar los atributos nombre y edad
del persona_uno.nombre  # Eliminamos el atributo nombre
del persona_uno.edad  # Eliminamos el atributo edad

# Intentar acceder a los atributos eliminados generará un error
# print(persona_uno.nombre)  # Generará un error al intentar acceder a nombre
# print(persona_uno.edad)  # Generará un error al intentar acceder a edad
