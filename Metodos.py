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

# para que sirven los metodos?

"""
Los métodos Python son funciones que pertenecen a una clase. 
Se utilizan para definir el comportamiento de los objetos de 
esa clase.
"""
# Creamos una clase
class Celular:
    
    #Metodo constructor: self -> forma de hacer referencia asi mismo
    def __init__(self,marca,modelo,camara):
        
        #Definimos las propiedades (atributos)
        self.marca = marca; 
        self.modelo = modelo; 
        self.camara = camara; 
    
    #Metodo llamar
    def llamada(self):
        print(f"Estas haciendo un llamado...  desde un {self.modelo}")
    
    #Metodo cortar
    def cortar(self):
        print(f"Estas cortaste la llamada... desde un {self.modelo}")
    

    
# Instancia nuestra clase con su nombre (creamos un objeto)
celular_uno = Celular(celular_uno_marca,celular_uno_modelo,celular_uno_camara_frontal); 
celular_dos = Celular(celular_dos_marca,celular_dos_modelo,celular_dos_camara_frontal); 

print(celular_uno); 
print(f"{type(celular_uno)}\n"); 

print(f"- Marca: {celular_uno.marca}.\n- Modelo: {celular_uno.modelo}.\n- Camara: {celular_uno.camara}.\n");
print(f"- Marca: {celular_dos.marca}.\n- Modelo: {celular_dos.modelo}.\n- Camara: {celular_dos.camara}.\n");  
print(f"\n{type(celular_uno.marca)}\n"); 

celular_uno.llamada(); 
celular_uno.cortar(); 

"39:33 / 4:14:12"