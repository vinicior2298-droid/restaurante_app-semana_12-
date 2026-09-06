class Usuario:

    def __init__(self, identificacion: str, nombre: str) -> None:
        self.identificacion = self.validar_identificacion(identificacion)
        self.nombre = self.validar_nombre(nombre)

    @staticmethod
    def validar_identificacion(identificacion: str) -> str:
        identificacion = identificacion.strip()

        if not identificacion:
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        return identificacion

    @staticmethod
    def validar_nombre(nombre: str) -> str:
        nombre = nombre.strip()

        if not nombre:
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        return nombre.title()

    def to_dict(self) -> dict:
        """Convierte el objeto Usuario en un diccionario."""
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre
        }

    def mostrar_informacion(self) -> str:
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre}"
        )

    def __str__(self) -> str:
        return self.mostrar_informacion()