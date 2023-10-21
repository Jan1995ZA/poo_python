# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre  # Nombre de la persona
        self.edad = edad  # Edad de la persona
        self.peso = peso  # Peso de la persona
        self.altura = altura  # Altura de la persona

    def Caminar(self):
        print(f"{self.nombre} está caminando.")  # Método que muestra un mensaje de caminar

    def Correr(self):
        print(f"{self.nombre} está corriendo.")  # Método que muestra un mensaje de correr

# Definición de la clase Artista
class Artista:
    def __init__(self, arte):
        self.arte = arte  # Tipo de arte que realiza el artista

    def practicando(self):
        print(f"El {self.arte} está practicando")  # Método que muestra un mensaje de práctica

# Definición de la clase Estudiante que hereda de Persona y Artista
class Estudiante(Persona, Artista):
    def __init__(self, nombre, edad, peso, altura, arte, universidad, horario):
        Persona.__init__(self, nombre, edad, peso, altura)  # Inicializa atributos heredados de Persona
        Artista.__init__(self, arte)  # Inicializa atributo heredado de Artista
        self.universidad = universidad  # Universidad a la que asiste el estudiante
        self.horario = horario  # Horario de clases del estudiante

    def Estudiando(self):
        print("Está estudiando")  # Método propio que muestra un mensaje de estudio

# Creación de una instancia de Estudiante
estudiante_uno = Estudiante("Juan", 27, 110, 189, "Cantante", "EAFIT", "La mañana")

# Imprime datos del estudiante
print(f"""
# DATOS DEL ESTUDIANTE:
# - Nombre: {estudiante_uno.nombre}
# - Edad: {estudiante_uno.edad}
# - Peso: {estudiante_uno.peso}
# - Altura: {estudiante_uno.altura}
# - Arte: {estudiante_uno.arte}
# - Universidad: {estudiante_uno.universidad}
# - Horario: {estudiante_uno.horario}
""")

# Llama a métodos del estudiante
estudiante_uno.Caminar()
estudiante_uno.Correr()
estudiante_uno.Estudiando()
estudiante_uno.practicando()

# Definición de la clase Profesor que hereda de Persona y Artista
class Profesor(Persona, Artista):
    def __init__(self, nombre, edad, peso, altura, arte, universidad, departamento, materias):
        Persona.__init__(self, nombre, edad, peso, altura)  # Inicializa atributos heredados de Persona
        Artista.__init__(self, arte)  # Inicializa atributo heredado de Artista
        self.universidad = universidad  # Universidad donde trabaja el profesor
        self.departamento = departamento  # Departamento al que pertenece el profesor
        self.materias = materias  # Materias que el profesor dicta

    def dictandoMateria(self):
        print(f"{self.nombre} está dictando la materia {self.materias}")  # Método propio que muestra la materia que dicta

# Creación de una instancia de Profesor
profesor_uno = Profesor("Pepe", 50, 75, 180, "Rapero", "EAFIT", "Ciencias Matemáticas", "Cálculo Uno")

# Imprime datos del profesor
print(f"""
# DATOS DEL PROFESOR:
# - Nombre: {profesor_uno.nombre}
# - Edad: {profesor_uno.edad}
# - Peso: {profesor_uno.peso}
# - Altura: {profesor_uno.altura}
# - Arte: {profesor_uno.arte}
# - Universidad: {profesor_uno.universidad}
# - Departamento: {profesor_uno.departamento}
# - Materia: {profesor_uno.materias}
""")

# Llama a métodos del profesor
profesor_uno.dictandoMateria()
profesor_uno.Caminar()
profesor_uno.Correr()
profesor_uno.practicando()


hereda =issubclass(Profesor,Artista)
print(hereda)

hereda =issubclass(Estudiante,Persona)
print(hereda)

instancia =isinstance(profesor_uno,Estudiante)
print(instancia)