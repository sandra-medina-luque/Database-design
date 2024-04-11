from src.database.db_mysql import get_connection
from src.models.proveedor_productoModel import Proveedor_producto

class ProveedorProductoService():

    @classmethod
    def get_proveedor_producto(cls):
        try:
            connection=get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute("CALL sp_proveedor_producto()")
                result= cursor.fetchall()
                print(result)
                connection.close()
                return 'lista actualizada'
               
        except Exception as ex: 
            print(ex)

    @classmethod
    def post_proveedor_producto(cls, proveedor_producto: Proveedor_producto):
        try:
            connection=get_connection()
            print(connection)
        
            with connection.cursor() as cursor:
                id_proveedor_producto = proveedor_producto.id_proveedor_producto
                id_proveedor = proveedor_producto.id_proveedor
                id_producto = proveedor_producto.id_producto
                
               

                cursor.execute('CALL sp_insert_proveedor_producto(%s, %s, %s)',(id_proveedor_producto, id_proveedor, id_producto))
                connection.commit()
                connection.close()
                return 'Detalle producto agregado correctamente'
               
        except Exception as ex: 
            print(ex)

    @classmethod
    def delete_proveedor_producto(cls, id_proveedor_producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("CALL sp_delete_proveedor_producto(%s)",id_proveedor_producto)
                connection.commit()
            connection.close()
            return 'Detalle producto eliminado correctamente'
        except Exception as ex:
            print(ex)

    @classmethod
    def put_proveedor_producto(cls, id_proveedor_producto, proveedor_producto: Proveedor_producto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                id_proveedor_producto = proveedor_producto.id_proveedor_producto
                id_proveedor = proveedor_producto.id_proveedor
                id_producto = proveedor_producto.id_producto
                
                cursor.execute('CALL sp_update_proveedor_producto(%s, %s, %s)',(id_proveedor_producto, id_proveedor, id_producto))
                connection.commit()
            connection.close()
            return 'Detalle producto actualizado correctamente'
        except Exception as ex:
            print(ex)        