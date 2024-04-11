from flask import Blueprint, request
from src.services.ProductoService import ProductoService
from src.models.productoModel import Producto

main = Blueprint('producto_blueprint',__name__)

@main.route('/',methods=['GET', 'POST'])

def get_producto():

    nombre = request.json ['nombre']
    descripcion = request.json ['descripcion']
    marca = request.json ['marca']
    stock = request.json ['stock']
    precio_unitario = request.json ['precio_unitario']

    print(nombre)
    print(descripcion)
    print(marca)
    print(stock)
    print(precio_unitario)

    producto= Producto(0,nombre,descripcion,marca,stock,precio_unitario)

    if request.method == 'GET':
        get_producto = ProductoService.get_producto()
        if get_producto:
            return 'Lista productos actualizada'
        else:
            return 'No se pudo acualizar los productos'
        

    elif request.method == 'POST':
        post_producto = ProductoService.post_producto(producto)
        if post_producto:
            return 'Producto agregado correctamente'
        else:
            return 'No se pudo agregar el producto'  

@main.route('/', methods=['PUT', 'DELETE'])
def actualizar_eliminar_producto():
    id_producto = request.json['id_producto']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    marca = request.json['marca']
    stock = request.json['stock']
    precio_unitario = request.json['precio_unitario']
        
    producto = Producto(id_producto, nombre, descripcion, marca, stock, precio_unitario)
   
    if request.method == 'PUT':
       put_producto = ProductoService.put_producto(id_producto, producto)
       if put_producto:
           return 'Producto editado correctamente'  
       else:
           return 'No se pudo editar el producto'
    
    elif request.method == 'DELETE':
        delete_producto = ProductoService.delete_producto(id_producto)
        if delete_producto:
            return 'Producto eliminado correctamente'
        else:
            return 'No se pudo eliminar el producto'
