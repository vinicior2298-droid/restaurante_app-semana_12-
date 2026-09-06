class Producto:

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> None:
        self.codigo = self.validar_codigo(codigo)
        self.nombre = self.validar_nombre(nombre)
        self.categoria = self.validar_categoria(categoria)
        self.precio = self.validar_precio(precio)
        self.stock = self.validar_stock(stock)

    @staticmethod
    def validar_codigo(codigo: str) -> str:
        codigo = codigo.strip()

        if not codigo:
            raise ValueError("El código no puede estar vacío.")

        return codigo.upper()

    @staticmethod
    def validar_nombre(nombre: str) -> str:
        nombre = nombre.strip()

        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        return nombre.title()

    @staticmethod
    def validar_categoria(categoria: str) -> str:
        categoria = categoria.strip()

        if not categoria:
            raise ValueError("La categoría no puede estar vacía.")

        return categoria.title()

    @staticmethod
    def validar_precio(precio: float) -> float:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        return precio

    @staticmethod
    def validar_stock(stock: int) -> int:
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        return stock

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.stock:
            raise ValueError("Stock insuficiente.")

        self.stock -= cantidad

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def __str__(self) -> str:
        return self.mostrar_informacion()