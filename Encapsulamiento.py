#Que es encapsulamiento?
"""
El encapsulamiento es un concepto de programación orientada a objetos que se refiere a la agrupación de datos y métodos relacionados en una sola unidad, llamada clase. Esto permite ocultar los detalles de implementación de una clase a otras clases, lo que mejora la seguridad y la mantenibilidad del código.

En Python, el encapsulamiento se logra mediante el uso de modificadores de acceso. Los modificadores de acceso son palabras clave que se utilizan para controlar el nivel de acceso a los miembros de una clase. Hay tres modificadores de acceso en Python:

* `public`: Los miembros públicos son accesibles desde cualquier lugar del programa.
* `protected`: Los miembros protegidos son accesibles desde la clase en la que se definen y desde las subclases de esa clase.
* `private`: Los miembros privados son accesibles solo desde la clase en la que se definen.

Por ejemplo, el siguiente código define una clase llamada `Persona` con dos atributos privados, `nombre` y `edad`:
"""
"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

"""

class MiClass:
    def __init__(self):
        self.__mi_variable_privada = "Valor"  # Declaración de una variable de instancia privada

    def __hablar(self):
        print("Hola, ¿cómo estás?")  # Declaración de un método privado

object = MiClass()  # Creación de una instancia de la clase MiClass

# Intentamos acceder a la variable de instancia privada, pero esto no es la forma recomendada
#print(object.__mi_variable_privada)

# Intentamos llamar al método privado, lo cual generará un error
#print(object.__hablar())



