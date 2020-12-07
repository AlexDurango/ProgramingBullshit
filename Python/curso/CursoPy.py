
#from (library) import*
"""
-----------------------------------------------------------------------------------------------------------------------------------------
OBJETOS: 
- Atributos: Las variables del objeto.
- Metodos: Las acciones que puede realizar el objeto. (Funciones).

class NombreDeLaClase:
    pass


-----------------------------------------------------------------------------------------------------------------------------------------
"""

"""
OBJECTS AND CLASES:

class NameOfTheClass:
    def __init__(self, atribute, atribute_1, atribute_2):    //Inicializa la clase con los atributos
        self.atribute = atribute
        self.atribute_1 = atribute_1
        self.atribute_2 = atribute_2

        ** Objects functions **

        def nameOfTheFunction(self, anotherParameter):
            instructions
            instructions
            return somthing


object_1 = NameOfTheClass(giveAtribute, giveAtribute_1, giveAtribute_2)  //Crear el objeto como tal

** To call the function **
object_1.nameOfTheFunction(anotherParameter)
**

"""

"""
INHERANCE (Usar los metodos de una clase en otra):

class NameClass1:
    def method1 (self):
        instruction
    def method2 (self):
        instruction

-- Crear una nueva clase con los mismos atributos que la anterior, pero que se puede agregar más ---
class NameClass2 (NameClass1):

    def newMethod (self):
        instruction


"""

"""
STRING FUNCTIONS: 

1) .upper
2) .lower
3 len(string)
4) .isupper = 0 || 1
5) .islower = 0 || 1
6) .index("Character or characters")
7) .replace(stringParametter, stringReplaced)

"""

""" 
NUMBER FUNCTIONS:

1). + || - || / || * || %
2). str(number)
3). absolute value: abs(number)
4). pow(number, exponent)
5). max(number 1, number 2) = gives the larger number
6). min(number1, nnumber2) = gives the smallest
7). round(decimalNumber)
---------- LIBRARY MATH --------
8). floor(decimalNumber) = gives the entire part of the number
9). ceil(decimalNumber) = gives the number rounded up
10) sqrt(number) 

"""

"""
LIST FUNCTIONS:

1). print(List[fromElement: toElement])
2). list1.extend(list2): 
ex :
    list1 = [1,2,3]
    list2 = ["alex", "santiago", "durango"]
    list1.extend(list2) = [1,2,3, "alex", "santiago", "durango"]

3). list.append(parameter) =        agregar un elemento a la lista
4). list.insert(indexToInsert, parameter) =    inserta un elemento en determinado index
5). list.remove(elementInTheList) =      eliminar un elemento de la lista
6). list.clear() =       elimina todos los datos de la lista
7). list.pop() =     elimina el ultimo elemento de la lista
8). list.index(parameter) =   da el index de cierto dato en la lista
9). list.count(parameter) =     dice cuantas veces se repite el mismo dato
---------
9.5)  another_list = sorted(list_1) ==  Deja la lista 1 en el orden dado pero "another_list" Si está ordenada con los datos de "List_1".
-------
10). list.sort() =    ORGANIZA LA LISTA YA SEA ALFABETICAMENTE O ALGEBRAICAMENTE DE MANERA ASCENDENTE
11). list.reverse() =  cambia el orden de la lista desde el ultimo al primero
     ex:
     list = [1,2,3,4,5]
     list.reverse()
     print(list) == [5,4,3,2,1]

12). list2 = list1.copy() = copia los elementos de una lista a otra

TUPLES:

1). tuple = (1,2,3,4,5,6)
    tuple[0] == 1

"""

"""
FUNCTIONS:
1).  def nameOfTheFunction (parameter):
        instructios
        instructions
        instructions
        return something
    nameOfTheFunction(parameter)

"""
"""
DICTIONARYS:

NameOfTheDictionary = {
    key: someData,
    key2: someData,
    key3: someData
}
"""
"""
WHILE AND FOR LOOPS:

while condition:
    instruction
    instruction


for index in varible/array:  //Empieza en 0 y va hasta n-1
    print(index)
"""

"""
ERRORS TRY/EXCEPT:
try:
    instruction

except typeOfError as variableError:
    print(variableError) 

"""

"""
READ FILES:

Open
1). variableName = open("filesName.txt", "r" or "w" or "a" or "r+")
2). variableName.close()
3). variableName.read()  //leer todo el archivo 
4). variableName.readable()  //Da un booleano, true si se puede leer
5). variableName.readline() //lee solo una linea del archivo
6). variableName.readlines()  //Crea en una lista todas las lineas del archivo

Write

1). variableName.write("Element or line") //using "a"
2). !!! USAR "W" borra todo lo que hay en el programa y lo remplaza por lo que uno digite !!!!
3). variableName.write("Element")

"""
"""

IMPORT SOMETHING FROM ANOTHER FILE:

File 1 (Name: operation.py): 
def add(num1, num2):
    return num1 + num2
----------------------------------------
File 2 (Name: index.py):
import add  \\or\\ from operation import add      //first line of code

print(operation.add(1,2)) //Console: 3;

"""
"""
THIS IS A NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE
 NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE
  NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE
   NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE
    NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE
     NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE
      NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE
       NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMAR

"""


