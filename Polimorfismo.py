# Explicación del polimorfismo en Python
"""
El polimorfismo en Python es un concepto que permite que los objetos de diferentes clases respondan
al mismo mensaje de diferentes maneras. Esto se logra mediante el uso de métodos virtuales, que son 
métodos que se definen en una clase base y se anulan en las clases derivadas.
"""
"""
#Polimorfismo de subtipos (sus clases)
class Animal():
    #Sobre carga de metodos
    def sonido(self):
        pass
    def sonido(self,nombre):
        pass
    def sonido(self,nombre,edad):
        pass
   """ 
"""
# Definición de la clase Gato
class Gato(Animal):
    def sonido(self):
        return "Miau!"

# Definición de la clase Perro
class Perro(Animal):
    def sonido(self):
        return "Guao!"
"""
"""
# Función para hacer que un animal emita un sonido
def hacer_sonido(animal):
    print(animal.sonido())
"""
# Creación de instancias de Gato y Perro
"""
gato_uno = Gato()
perro_uno = Perro()
"""
# Llamadas a los métodos sonido() de las instancias (comentadas)
# print(gato_uno.sonido())
# print(perro_uno.sonido())

# Llamadas a la función hacer_sonido con instancias de Gato y Perro
#hacer_sonido(perro_uno)
#hacer_sonido(gato_uno)

# En este ejemplo, la función 'hacer_sonido' recibe como parámetro a un animal.
# Dependiendo de la clase del animal pasado como argumento, la función imprimirá
# el sonido correspondiente al tipo de animal.


#Tarea: Duck Typing ,Enlaces dinamicos y estaticos, Tipo real y declarado


#########################################################
# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
"""
    # Método base para acelerar (puede ser sobrecargado en las clases derivadas)
    def acelerar(self):
        pass

    # Método base para frenar (puede ser sobrecargado en las clases derivadas)
    def frenar(self):
        pass"""

# Clase derivada Coche
class Coche(Vehiculo):
    # Implementación específica para acelerar en un Coche
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelera rápidamente")

    # Implementación específica para frenar en un Coche
    def frenar(self):
        print(f"{self.marca} {self.modelo} frena con frenos de disco")

# Clase derivada Bicicleta
class Bicicleta(Vehiculo):
    # Implementación específica para acelerar en una Bicicleta
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelera pedaleando")

    # Implementación específica para frenar en una Bicicleta
    def frenar(self):
        print(f"{self.marca} {self.modelo} frena con frenos de mano")

# Función para mostrar el polimorfismo
def probar_vehiculo(vehiculo):
    # Llamamos al método acelerar del vehículo pasado como argumento
    vehiculo.acelerar()
    # Llamamos al método frenar del vehículo pasado como argumento
    vehiculo.frenar()

# Creación de objetos de Coche y Bicicleta
mi_coche = Coche("Toyota", "Camry")
mi_bicicleta = Bicicleta("Trek", "Mountain Bike")

# Probamos el polimorfismo
print("Probando mi coche:")
probar_vehiculo(mi_coche)

print("\nProbando mi bicicleta:")
probar_vehiculo(mi_bicicleta)
