class Usuario:

    def __init__(self, identificacion: str, nombre: str, contraseña: str) -> None:
        self.identificacion = self.validar_identificacion(identificacion)
        self.nombre = self.validar_nombre(nombre)
        self.contraseña = self.validar_contraseña(contraseña)

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

    @staticmethod
    def validar_contraseña(contraseña: str) ->str:
        contraseña = contraseña.strip()
        if len (contraseña) <8:
            raise ValueError("La contraseña debe tener 8 caracteres.")
        if not any(c.isalpha() for c in contraseña):
            raise ValueError("La contraseña debe tener al menos una letra.")
        if not any(c.isdigit() for c in contraseña):
            raise ValueError("La contraseña debe tener al menos un número.")
        return contraseña 

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "contraseña": self.contraseña
        }

    def mostrar_informacion(self) -> str:
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Contraseña: {self.contraseña}"
        )

    def __str__(self) -> str:
        return self.mostrar_informacion()