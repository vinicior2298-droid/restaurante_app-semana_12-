from modelos.producto import Producto
from modelos.usuario import Usuario

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()

    def autenticar(self, identificacion, contraseña):
        return self.archivo_servicio.validar_acceso(identificacion, contraseña)

    def listar_productos(self):
        return self.productos

    def listar_usuarios(self):
        return self.usuarios

    def obtener_producto_por_id(self, codigo):
        for p in self.productos:
            if str(p.codigo) == str(codigo).strip().upper():
                return p
        return None

    def registrar_producto(self, codigo, nombre, categoria, precio, stock=0):
        if self.obtener_producto_por_id(codigo):
            return False, f"El código {codigo} ya está registrado."
        try:
            nuevo_p = Producto(codigo, nombre, categoria, precio, stock)
            self.productos.append(nuevo_p)
            self.archivo_servicio.guardar_productos(self.productos)
            return True, "Producto registrado correctamente."
        except ValueError as e:
            return False, str(e)

    def actualizar_producto(self, codigo, nombre, categoria, precio):
        prod = self.obtener_producto_por_id(codigo)
        if not prod:
            return False, "El producto a actualizar no existe."
        try:
            prod.nombre = Producto.validar_nombre(nombre)
            prod.categoria = Producto.validar_categoria(categoria)
            prod.precio = Producto.validar_precio(precio)
            self.archivo_servicio.guardar_productos(self.productos)
            return True, "Producto actualizado correctamente."
        except ValueError as e:
            return False, str(e)

    def eliminar_producto(self, codigo):
        prod = self.obtener_producto_por_id(codigo)
        if not prod:
            return False, "El producto a eliminar no existe."

        self.productos.remove(prod)
        self.archivo_servicio.guardar_productos(self.productos)
        return True, "Producto eliminado correctamente."