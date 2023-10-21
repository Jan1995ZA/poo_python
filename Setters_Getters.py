#Que es Setters y Getters?
"""
Setters y getters son métodos especiales que se utilizan para establecer y obtener el valor de una propiedad privada en una clase de Python.

Los setters se utilizan para establecer el valor de una propiedad privada, mientras que los getters se utilizan para obtener el valor de una propiedad privada.

Los setters y getters se utilizan a menudo para encapsular los datos de una clase y evitar que sean accedidos directamente desde fuera de la clase.

Esto ayuda a proteger los datos de la clase y a garantizar que sólo se puedan acceder a ellos a través de los métodos públicos de la clase.

Por ejemplo, si tenemos una clase llamada `Persona` que tiene una propiedad privada llamada `nombre`, podríamos crear un setter y un getter para esta propiedad de la siguiente manera:
"""
"""
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre
        
"""
"""
El setter `set_nombre()` se utiliza para establecer el valor de la propiedad `nombre`, mientras que el getter `get_nombre()` se utiliza para obtener el valor de la propiedad `nombre`.

Los setters y getters se pueden utilizar para cualquier tipo de propiedad privada, incluidos los números, las cadenas y los objetos.
"""
"""
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Declaración de una variable de instancia privada
        self.__edad = edad  # Declaración de una variable de instancia privada

    def get_persona(self):
        return self.__nombre, self.__edad
        # Método para obtener los datos de la persona (nombre y edad)

    def set_persona(self, new_nombre, new_edad):
        self.__nombre = new_nombre
        self.__edad = new_edad
        # Método para modificar los datos de la persona (nombre y edad)
   
persona_uno = Persona("Juan", 28)  # Creación de una instancia de la clase Persona

persona = persona_uno.get_persona()  # Llamamos al método para obtener los datos de la persona
print(persona)  # Imprimimos los datos de la persona (nombre y edad)

persona_uno.set_persona("Josue", 89)  # Llamamos al método para modificar los datos de la persona
persona = persona_uno.get_persona()  # Llamamos nuevamente al método para obtener los nuevos datos de la persona

print(persona)  # Imprimimos los nuevos datos de la persona

"""
