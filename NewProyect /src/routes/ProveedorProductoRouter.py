from flask import Blueprint, request
from src.services.ProveedorProductoService import ProveedorProductoService
from src.models.proveedor_productoModel import Proveedor_producto

main3 = Blueprint('proveedor_producto_blueprint',__name__)

@main3.route('/',methods=['GET', 'POST'])

def get_proveedor_producto():

    id_proveedor = request.json ['id_proveedor']
    id_producto = request.json ['id_producto']
    
    

    print(id_proveedor)
    print(id_producto)
    
    

    proveedor_producto= Proveedor_producto(0,id_proveedor, id_producto)

    if request.method == 'GET':
        get_proveedor_producto = ProveedorProductoService.get_proveedor_producto()
        if get_proveedor_producto:
            return 'Lista detalle producto actualizada'
        else:
            return 'No se pudo acualizar detalle producto'
        

    elif request.method == 'POST':
        post_proveedor_producto = ProveedorProductoService.post_proveedor_producto(proveedor_producto)
        if post_proveedor_producto:
            return 'Detalle producto agregado correctamente'
        else:
            return 'No se pudo agregar detalle producto'  

@main3.route('/', methods=['PUT', 'DELETE'])
def actualizar_eliminar_proveedor_producto():
    id_proveedor_producto = request.json['id_proveedor_producto']
    id_proveedor = request.json['id_proveedor']
    id_producto = request.json['id_producto']
    
     
    proveedor_producto = Proveedor_producto(id_proveedor_producto, id_proveedor, id_producto)
   
    if request.method == 'PUT':
       put_proveedor_producto = ProveedorProductoService.put_proveedor_producto(id_proveedor, proveedor_producto)
       if put_proveedor_producto:
           return 'Detalle producto editado correctamente'  
       else:
           return 'No se pudo editar detalle producto'
    
    elif request.method == 'DELETE':
        delete_proveedor_producto = ProveedorProductoService.delete_proveedor_producto(id_proveedor_producto)
        if delete_proveedor_producto:
            return 'Detalle producto eliminado correctamente'
        else:
            return 'No se pudo eliminar detalle producto'
