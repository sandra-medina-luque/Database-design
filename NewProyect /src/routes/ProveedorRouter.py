from flask import Blueprint, request
from src.services.ProveedorService import ProveedorService
from src.models.proveedorModel import Proveedor

main2 = Blueprint('proveedor_blueprint',__name__)

@main2.route('/',methods=['GET', 'POST'])

def get_proveedor():

    nombre = request.json ['nombre']
    direccion = request.json ['direccion']
    telefono = request.json ['telefono']
    

    print(nombre)
    print(direccion)
    print(telefono)
    

    proveedor= Proveedor(0,nombre,direccion, telefono)

    if request.method == 'GET':
        get_proveedor = ProveedorService.get_proveedor()
        if get_proveedor:
            return 'Lista proveedores actualizada'
        else:
            return 'No se pudo acualizar los proveedores'
        

    elif request.method == 'POST':
        post_proveedor = ProveedorService.post_proveedor(proveedor)
        if post_proveedor:
            return 'Proveedor agregado correctamente'
        else:
            return 'No se pudo agregar el proveedor'  

@main2.route('/', methods=['PUT', 'DELETE'])
def actualizar_eliminar_proveedor():
    id_proveedor = request.json['id_proveedor']
    nombre = request.json['nombre']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    
        
    proveedor = Proveedor(id_proveedor, nombre, direccion, telefono)
   
    if request.method == 'PUT':
       put_proveedor = ProveedorService.put_proveedor(id_proveedor, proveedor)
       if put_proveedor:
           return 'Proveedor editado correctamente'  
       else:
           return 'No se pudo editar el proveedor'
    
    elif request.method == 'DELETE':
        delete_proveedor = ProveedorService.delete_proveedor(id_proveedor)
        if delete_proveedor:
            return 'Proveedor eliminado correctamente'
        else:
            return 'No se pudo eliminar el proveedor'
