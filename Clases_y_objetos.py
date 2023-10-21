#celulares

celular_uno_marca = "Samsung"; 
celular_dos_marca = "Iphone"; 
celular_tres_marca = "Huawei"; 
celular_cuatro_marca = "Xiaomi"; 
celular_cinco_marca = "Oppo"; 

celular_uno_modelo = "S3"; 
celular_dos_modelo= "A10s"; 
celular_tres_modelo="P40 Pro"; 
celular_cuatro_modelo ="Mi A2 Lite"; 
celular_cinco_modelo ="Reno5"; 


celular_uno_camara_frontal = "48MP"; 
celular_dos_camara_frontal = "6.7MP"; 
celular_tres_camara_frontal = "12MP";    
celular_cuatro_camara_frontal = "12MP"; 
celular_cinco_camara_frontal = "11MP"; 

celular_uno_camara_trasera = "38MP"; 
celular_dos_camara_trasera = "8.7MP"; 
celular_tres_camara_trasera = "12MP";    
celular_cuatro_camara_trasera = "12MP"; 
celular_cinco_camara_trasera = "11MP"; 

#Que son las clases ?

"""
CLASES:
Las clases de Python son una forma de organizar el código en unidades reutilizables. 
Una clase define un conjunto de atributos y métodos que se pueden usar para crear objetos. 
Los objetos son instancias de una clase y tienen sus propios datos y comportamiento.

Las clases se definen usando la palabra clave `class`. El nombre de la clase debe comenzar con una letra mayúscula. 
El cuerpo de la clase contiene las definiciones de los atributos y métodos de la clase.

Los atributos son variables que pertenecen a una clase. 
Se pueden usar para almacenar datos sobre los objetos que se crean a partir de la clase. 
Los métodos son funciones que pertenecen a una clase. 
Se pueden usar para realizar operaciones en los objetos que se crean a partir de la clase.

Para crear un objeto a partir de una clase, se usa la palabra clave `new`. 
El objeto se crea llamando al constructor de la clase. 
El constructor es un método especial que se llama cuando se crea un objeto. 
El constructor puede tomar argumentos, que se usan para inicializar los atributos del objeto.

Una vez que se ha creado un objeto, se puede usar para acceder a sus atributos y métodos. 
Para acceder a un atributo, se usa el operador de punto (`.`). 
Para llamar a un método, se usa el operador de flecha (`->`).

Las clases de Python son una herramienta poderosa que se puede usar para organizar el código en unidades reutilizables. 
Las clases se pueden usar para crear objetos que tienen sus propios datos y comportamiento. 
Las clases se pueden usar para crear jerarquías de clases, lo que permite reutilizar código entre clases relacionadas.

###########

OBJETOS:
Los objetos son instancias de una clase. Tienen sus propios datos y comportamiento. 
Los objetos se crean usando la palabra clave `new`. El objeto se crea llamando al constructor de la clase. 
El constructor es un método especial que se llama cuando se crea un objeto. 
El constructor puede tomar argumentos, que se usan para inicializar los atributos del objeto.

Una vez que se ha creado un objeto, se puede usar para acceder a sus atributos y métodos. 
Para acceder a un atributo, se usa el operador de punto (`.`). 
Para llamar a un método, se usa el operador de flecha (`->`).
"""

# Creamos una clase
class NombreClase():
    
    #Colocamoso sus atributos estaticas
    propiedada_una = "valor_uno"; 
    propiedada_dos = "valor_dos"; 
    propiedada_tres = "valor_tres"; 
    
# Instancia nuestra clase con su nombre (creamos un objeto)
miObjeto_uno = NombreClase(); 

print(miObjeto_uno); 
print(type(miObjeto_uno)); 

print(miObjeto_uno.propiedada_una); 
print(type(miObjeto_uno.propiedada_una)); 

# Creamos una clase
class Celular:
    
    #Metodo constructor: self -> forma de hacer referencia asi mismo
    def __init__(self,marca,modelo,camara):
        
        #Definimos las propiedades (atributos)
        self.marca = marca; 
        self.modelo = modelo; 
        self.camara = camara; 
    
# Instancia nuestra clase con su nombre (creamos un objeto)
celular_uno = Celular(celular_uno_marca,celular_uno_modelo,celular_uno_camara_frontal); 
celular_dos = Celular(celular_dos_marca,celular_dos_modelo,celular_dos_camara_frontal); 

print(celular_uno); 
print(f"{type(celular_uno)}\n"); 

print(f"- Marca: {celular_uno.marca}.\n- Modelo: {celular_uno.modelo}.\n- Camara: {celular_uno.camara}.\n");
print(f"- Marca: {celular_dos.marca}.\n- Modelo: {celular_dos.modelo}.\n- Camara: {celular_dos.camara}.\n");  
print(type(celular_uno.marca)); 