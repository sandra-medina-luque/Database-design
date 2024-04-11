from src.database.db_mysql import get_connection
from src.models.proveedorModel import Proveedor

class ProveedorService():

    @classmethod
    def get_proveedor(cls):
        try:
            connection=get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute("CALL sp_proveedor()")
                result= cursor.fetchall()
                print(result)
                connection.close()
                return 'lista actualizada'
               
        except Exception as ex: 
            print(ex)

    @classmethod
    def post_proveedor(cls, proveedor: Proveedor):
        try:
            connection=get_connection()
            print(connection)
        
            with connection.cursor() as cursor:
                id_proveedor = proveedor.id_proveedor
                nombre = proveedor.nombre
                direccion = proveedor.direccion
                telefono = proveedor.telefono
               

                cursor.execute('CALL sp_insert_proveedor(%s, %s, %s, %s)',(id_proveedor, nombre, direccion, telefono))
                connection.commit()
                connection.close()
                return 'Proveedor agregado correctamente'
               
        except Exception as ex: 
            print(ex)

    @classmethod
    def delete_proveedor(cls, id_proveedor):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("CALL sp_deleteproveedor(%s)",id_proveedor)
                connection.commit()
            connection.close()
            return 'Proveedor eliminado correctamente'
        except Exception as ex:
            print(ex)

    @classmethod
    def put_proveedor(cls, id_proveedor, proveedor: Proveedor):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                nombre = proveedor.nombre
                direccion = proveedor.direccion
                telefono = proveedor.telefono
                
                cursor.execute('CALL sp_update_proveedor(%s, %s, %s, %s)',(nombre, direccion, telefono, id_proveedor))
                connection.commit()
            connection.close()
            return 'Proveedor actualizado correctamente'
        except Exception as ex:
            print(ex)        