# Definición de la clase Estudiante
class Estudiante:
    # Constructor de la clase que inicializa los atributos nombre, edad y grado
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre  # Asigna el valor de nombre al atributo self.nombre
        self.edad = edad      # Asigna el valor de edad al atributo self.edad
        self.grado = grado    # Asigna el valor de grado al atributo self.grado
    
    # Método de la clase que imprime un mensaje de que el estudiante está estudiando
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")

nombre = input("Nombre del estudiante: ")
edad =int(input("Edad del estudiante: "))
grado = int(input("Grado del estudiante: "))
# Crear una instancia de la clase Estudiante llamada estudiante_uno
estudiante_uno = Estudiante(nombre, edad, grado)
print(f"""
      DATOS DEL ESTUDIANTE:\n
      - El nomre es:{estudiante_uno.nombre}
      - La edad es: {estudiante_uno.edad}
      - El grado es: {estudiante_uno.grado}
      """)

# Llamar al método "estudiar" de la instancia estudiante_uno
while True:
    estudiar =input()
    if (estudiar.lower()=="estudiar"):
        estudiante_uno.estudiar()
        break
    else :
        print("El nombre estudiar no es correcto")
    
