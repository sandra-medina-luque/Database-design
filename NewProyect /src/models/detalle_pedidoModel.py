class Detalle_pedido():
    def __init__(self, id_detalle_pedido, id_pedido, id_producto, precio_total, cantidad) -> None:
       self.id_detalle_pedido=id_detalle_pedido
       self.id_pedido=id_pedido
       self.id_producto=id_producto
       self.precio_total=precio_total
       self.cantidad=cantidad
       
       