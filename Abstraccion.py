#Que es abstraccion?
"""
La abstracción en Python es el acto de crear una interfaz que oculta los detalles de implementación de un objeto. 
Esto permite a los usuarios interactuar con el objeto sin necesidad de saber cómo funciona. 
La abstracción se utiliza a menudo para crear bibliotecas y marcos de trabajo que pueden ser utilizados por otros desarrolladores.

Por ejemplo, la biblioteca `requests` proporciona una interfaz para hacer peticiones HTTP. 
Los usuarios pueden utilizar esta biblioteca para hacer peticiones a cualquier sitio web sin necesidad de saber cómo funciona el protocolo HTTP.

La abstracción es una herramienta poderosa que puede hacer que el código sea más fácil de leer, entender y mantener. 
También puede ayudar a reducir los errores y hacer que el código sea más reutilizable.
"""
class Auto():
    def __init__(self):
        self.__estado = "Apagado"  # Inicializamos el estado del auto como "Apagado"

    def encender(self):
        self.__estado = "Prendido"  # Cambiamos el estado a "Prendido"
        print("El auto está encendido")

    def conducir(self):
        if self.__estado == "Apagado":
            self.encender()  # Si el auto está apagado, lo encendemos llamando al método 'encender'
        print("Conduciendo el auto")  # Imprimimos un mensaje indicando que estamos conduciendo el auto

# Creamos una instancia de la clase Auto
mi_auto = Auto()

# Llamamos al método 'conducir' de la instancia 'mi_auto'
mi_auto.conducir()
