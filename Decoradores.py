def decorador(funcion):
    # Definimos el decorador, que toma una función 'funcion' como argumento
    def funcion_modificada():
        print("Antes de llamar a la función")  # Mensaje antes de llamar a la función
        funcion()  # Llamamos a la función original
        print("Después de llamar a la función")  # Mensaje después de llamar a la función

    return funcion_modificada  # Devolvemos la función modificada como resultado del decorador
"""
# Definimos una función 'saludo' que será decorada
def saludo():
    print("Hola")

# Aplicamos el decorador manualmente a la función 'saludo'
saludo_modificado = decorador(saludo)

# Llamamos a la versión modificada de la función 'saludo', que incluye mensajes del decorador
saludo_modificado()
"""
# Usamos el símbolo '@decorador' para decorar automáticamente la función 'saludo'
@decorador
def saludo():
    print("Hola")

# Llamamos a la función 'saludo' decorada utilizando el símbolo '@', que también muestra mensajes del decorador
saludo()
