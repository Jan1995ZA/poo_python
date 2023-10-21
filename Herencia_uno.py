#Que es la herencia?
"""
La herencia en Python es un mecanismo que permite a una clase heredar los atributos y métodos de otra clase. 
Esto permite reutilizar código y crear jerarquías de clases.

Cuando una clase hereda de otra, la clase hija adquiere los atributos y métodos de la clase padre. 
Además, la clase hija puede definir sus propios atributos y métodos, que no afectarán a la clase padre.

Para que una clase herede de otra, se utiliza la palabra clave `class` seguida del nombre de la clase hija, dos puntos y el nombre de la clase padre.

"""

class Persona:
    def __init__(self,nombre,edad,peso,altura):
        self.nombre =nombre; 
        self.edad= edad ; 
        self.peso= peso; 
        self.altura= altura


    def Caminar(self):
            print(f"{self.nombre} esta caminando.")
    def Correr(self):
            print(f"{self.nombre} esta corriendo.")

#persona_uno=Persona("Juan",27,110,189)

#print(f"""
      #DATOS DE LA PERSONA
      #- Nombre: {persona_uno.nombre}
      #- Edad: {persona_uno.edad}
      #- Peso: {persona_uno.peso}
      #- Altura: {persona_uno.altura}

      #""")
#persona_uno.Caminar()
#persona_uno.Correr()

class Estudiante(Persona):
    def __init__(self,nombre,edad,peso,altura,universidad,horario):
        super().__init__(nombre,edad,peso,altura)
        self.universidad=universidad; 
        self.horario= horario
    
    def Estudiando(self):
        print("Esta estudiando")

estudiante_uno = Estudiante("Juan",27,110,189,"EAFIT","La mañana")

print(f"""
      #DATOS DEL PROFESOR:
      #- Nombre: {estudiante_uno.nombre}
      #- Edad: {estudiante_uno.edad}
      #- Peso: {estudiante_uno.peso}
      #- Altura: {estudiante_uno.altura}
      #- Universidad: {estudiante_uno.universidad}
      #- Horario: {estudiante_uno.horario}
        """)

estudiante_uno.Caminar()
estudiante_uno.Correr()
estudiante_uno.Estudiando()

class Profesor(Persona):
    def __init__(self, nombre, edad, peso, altura , universidad,departamento,materias):
        super().__init__(nombre,edad,peso,altura); 
        self.universidad=universidad; 
        self.departamento=departamento; 
        self.materias=materias; 
    
    def dictandoMateria(self):
        print(f"{self.nombre} esta dictando la {self.materias}")
profesor_uno= Profesor("Pepe",50,75,180,"EAFIT","Ciencias Matematicas","Calculo Uno")
        

print(f"""
      #DATOS DEL ESTUDIANTE:
      #- Nombre: {profesor_uno.nombre}
      #- Edad: {profesor_uno.edad}
      #- Peso: {profesor_uno.peso}
      #- Altura: {profesor_uno.altura}
      #- Universidad: {profesor_uno.universidad}
      #- Departamento: {profesor_uno.departamento}
      #- Materia: {profesor_uno.materias}
        """)

profesor_uno.dictandoMateria()
profesor_uno.Caminar()
profesor_uno.Correr()
            
