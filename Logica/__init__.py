# Aqui se encuentra logica como la de objetos colisionando
# Y la que nos permite acceder a otros niveles

import os #usada por leerSave()

def collide(obj1, obj2):
    """
    Chequea los bordes de los objetos para asi encontrar la colision
    """
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def leerSave():
    """
    utiliza el context manager para asi leer el archivo y encontrar los datos guardados
    """
    pass


if __name__ == "__main__":
    print("Estas en modo debug para chequear el funcionamiento")
    print("Estas visitando los siguientes paths para los juegos guardados")

    pathSave = os.path.join()