import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    def __init__(self, carpeta_datos: str = "datos") -> None:
        self.carpeta = Path(carpeta_datos)

        self.carpeta.mkdir(
            parents=True,
            exist_ok=True
        )

        self.archivo_productos = self.carpeta / "productos.json"
        self.archivo_usuarios = self.carpeta / "usuarios.json"
        self.archivo_ventas = self.carpeta / "ventas.json"

    # =====================================
    # PRODUCTOS
    # =====================================

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> None:

        datos = []

        for producto in productos:
            datos.append(producto.to_dict())

        try:
            with self.archivo_productos.open(
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print("No existen permisos para guardar productos.")

    def cargar_productos(self) -> list[Producto]:

        if not self.archivo_productos.exists():
            return []

        try:

            with self.archivo_productos.open(
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            productos = []

            for registro in datos:

                try:

                    producto = Producto(
                        registro["codigo"],
                        registro["nombre"],
                        registro["categoria"],
                        float(registro["precio"]),
                        int(registro["stock"])
                    )

                    productos.append(producto)

                except (KeyError, ValueError):

                    continue

            return productos

        except (
            FileNotFoundError,
            json.JSONDecodeError,
            PermissionError
        ):

            return []

    # =====================================
    # USUARIOS
    # =====================================

    def guardar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> None:

        datos = []

        for usuario in usuarios:
            datos.append(usuario.to_dict())

        try:

            with self.archivo_usuarios.open(
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:

            print("No existen permisos para guardar usuarios.")

    def cargar_usuarios(self) -> list[Usuario]:

        if not self.archivo_usuarios.exists():
            return []

        try:

            with self.archivo_usuarios.open(
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            usuarios = []

            for registro in datos:

                try:

                    usuario = Usuario(
                        registro["identificacion"],
                        registro["nombre"]
                    )

                    usuarios.append(usuario)

                except (KeyError, ValueError):

                    continue

            return usuarios

        except (
            FileNotFoundError,
            json.JSONDecodeError,
            PermissionError
        ):

            return []

    # =====================================
    # VENTAS
    # =====================================

    def guardar_ventas(
        self,
        ventas: list[Venta]
    ) -> bool:
 
        datos = []
 
        for venta in ventas:
            datos.append(venta.to_dict())
 
        try:
            with self.archivo_ventas.open(
                "w",
                encoding="utf-8"
            ) as archivo:
 
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )
 
            return True
 
        except PermissionError:
            print("No existen permisos para guardar ventas.")
            return False    

    def cargar_ventas(self) -> list[Venta]:

        if not self.archivo_ventas.exists():
            return []

        try:

            with self.archivo_ventas.open(
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            ventas = []

            for registro in datos:

                try:

                    venta = Venta(
                        registro["usuario_id"],
                        registro["producto_codigo"],
                        int(registro["cantidad"])
                    )

                    ventas.append(venta)

                except (KeyError, ValueError):

                    continue

            return ventas

        except (
            FileNotFoundError,
            json.JSONDecodeError,
            PermissionError
        ):

            return []