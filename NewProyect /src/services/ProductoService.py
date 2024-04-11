from src.database.db_mysql import get_connection
from src.models.productoModel import Producto

class ProductoService():

    @classmethod
    def get_producto(cls):
        try:
            connection=get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM producto')
                result= cursor.fetchall()
                print(result)
                connection.close()
                return 'lista actualizada'
               
        except Exception as ex: 
            print(ex)

    @classmethod
    def post_producto(cls, producto: Producto):
        try:
            connection=get_connection()
            print(connection)
        
            with connection.cursor() as cursor:
                id_producto = producto.id_producto
                nombre = producto.nombre
                descripcion = producto.descripcion
                marca = producto.marca
                stock = producto.stock
                precio_unitario = producto.precio_unitario

                cursor.execute("INSERT INTO producto (id_producto, nombre, descripcion, marca, stock, precio_unitario) VALUES ('{0}', '{1}', '{2} ', '{3}', '{4}', '{5}');".format(id_producto, nombre, descripcion, marca, stock, precio_unitario))
                connection.commit()
                connection.close()
                return 'Producto agregado correctamente'
               
        except Exception as ex: 
            print(ex)

    @classmethod
    def delete_producto(cls, id_producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM producto WHERE id_producto = %s;", (id_producto))
                connection.commit()
            connection.close()
            return 'Producto eliminado correctamente'
        except Exception as ex:
            print(ex)

    @classmethod
    def put_producto(cls, id_producto, producto: Producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                nombre = producto.nombre
                descripcion = producto.descripcion
                marca = producto.marca
                stock = producto.stock
                precio_unitario = producto.precio_unitario
                cursor.execute("UPDATE producto SET nombre = %s, descripcion = %s, marca = %s, stock = %s, precio_unitario = %s WHERE id_producto = %s;", (nombre, descripcion, marca, stock, precio_unitario, id_producto))
                connection.commit()
            connection.close()
            return 'Producto actualizado correctamente'
        except Exception as ex:
            print(ex)        