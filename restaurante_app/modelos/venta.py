class Venta:
    def __init__(self, id_usuario, id_producto, cantidad: int = 1):
        self.id_usuario = id_usuario
        self.id_producto = id_producto  
        self.cantidad = cantidad
        
    @staticmethod
    def validar_numero_positivo(valor, nombre_campo="Valor"):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise TypeError(f"El valor de '{nombre_campo}' debe ser un número (int o float).")
        if valor <= 0:
            raise ValueError(f"El valor de '{nombre_campo}' debe ser mayor a cero.")
        return True

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self.validar_numero_positivo(valor, "Cantidad")
        if hasattr(self, 'producto') and self.producto and hasattr(self.producto, 'stock'):
            if valor > self.producto.stock:
                raise ValueError(
                    f"La cantidad solicitada ({valor}) supera el stock disponible ({self.producto.stock})."
                )
        
        self._cantidad = int(valor)

    @property
    def precio_unitario(self):
        return self._precio_unitario

    @precio_unitario.setter
    def precio_unitario(self, valor):
        self.validar_numero_positivo(valor, "Precio Unitario")
        self._precio_unitario = float(valor)

    def calcular_total(self):
        return self.cantidad * self.precio_unitario

    def a_diccionario(self):
        return {
            "usuario_id": str(self.id_usuario),
            "producto_codigo": str(self.id_producto),
            "cantidad": str(self.cantidad),
        }

    def to_dict(self):
        return self.a_diccionario()