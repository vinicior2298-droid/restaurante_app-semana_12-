from pathlib import Path
import json
from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta

class ArchivoServicio:

    def __init__(self, carpeta_datos: str = "restaurante_app/datos") -> None:
        self.carpeta = Path(carpeta_datos)

        self.carpeta.mkdir(
            parents=True,
            exist_ok=True
        )

        self.archivo_productos = self.carpeta / "productos.json"
        self.archivo_usuarios = self.carpeta / "usuarios.json"
        self.archivo_ventas = self.carpeta / "ventas.json"

    def cargar_usuarios(self) -> list[Usuario]:
        print("Ruta buscada:", self.archivo_usuarios)
        print("¿Existe el archivo?", self.archivo_usuarios.exists())

        if not self.archivo_usuarios.exists():
            return []

        try:
            with self.archivo_usuarios.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            print("Usuarios cargados:", datos)

            usuarios = []
            for registro in datos:
                try:
                    usuario = Usuario(
                        registro["identificacion"],
                        registro["nombre"],
                        registro["contraseña"]  # ojo: debe estar escrito con ñ en el JSON
                    )
                    usuarios.append(usuario)
                except (KeyError, ValueError) as e:
                    print("Error al procesar registro:", registro, e)
                    continue

            return usuarios

        except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
            print("Error al abrir archivo:", e)
            return []

    def validar_acceso(self, identificacion: str, contraseña: str) -> Usuario | None:
        usuarios = self.cargar_usuarios()

        for u in usuarios:
            print("Comparando con:", u.identificacion, u.contraseña)  # depuración
            if u.identificacion == identificacion and u.contraseña == contraseña:
                return u

        return None
