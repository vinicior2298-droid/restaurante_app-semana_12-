from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Buscar usuario"),
    ("8", "Actualizar usuario"),
    ("9", "Eliminar usuario"),
    ("10", "Listar usuarios"),
    ("11", "Vender producto"),
    ("12", "Consultar ventas de usuario"),
    ("13", "Listar categorias unicas"),
    ("0", "Salir"),
)

# ==========================
# ENTRADAS POR CONSOLA
# ==========================

def pedir_texto(mensaje: str) -> str:
    return input(mensaje).strip()


def pedir_entero(
    mensaje: str,
    valor_por_defecto: int | None = None
) -> int:

    texto = pedir_texto(mensaje)

    if texto == "" and valor_por_defecto is not None:
        return valor_por_defecto

    return int(texto)


def pedir_float(mensaje: str) -> float:
    return float(pedir_texto(mensaje))


# ==========================
# MENU
# ==========================

def mostrar_menu() -> None:

    print("\n===== RESTAURANTE APP =====")

    print("\nGESTION DE PRODUCTOS")
    for numero, descripcion in OPCIONES_MENU[:5]:
        print(f"{numero}. {descripcion}")

    print("\nGESTION DE USUARIOS")
    for numero, descripcion in OPCIONES_MENU[5:10]:
        print(f"{numero}. {descripcion}")

    print("\nOPERACIONES")
    print(f"{OPCIONES_MENU[10][0]}. {OPCIONES_MENU[10][1]}")

    print("\nCONSULTAS")
    for numero, descripcion in OPCIONES_MENU[11:13]:
        print(f"{numero}. {descripcion}")

    print("\n0. Salir")


# ==========================
# GUARDADO
# ==========================

def guardar_productos(
    archivo_servicio: ArchivoServicio,
    restaurante: Restaurante
) -> None:

    archivo_servicio.guardar_productos(
        restaurante.listar_productos()
    )


def guardar_usuarios(
    archivo_servicio: ArchivoServicio,
    restaurante: Restaurante
) -> None:

    archivo_servicio.guardar_usuarios(
        restaurante.listar_usuarios()
    )


def guardar_ventas(
    archivo_servicio: ArchivoServicio,
    restaurante: Restaurante
) -> None:

    guardado = archivo_servicio.guardar_ventas(
        restaurante.listar_ventas()
    )

    if not guardado:
        print("Los cambios de ventas no pudieron guardarse.")


# ==========================
# PRODUCTOS
# ==========================

def registrar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- Registrar producto ---")

    codigo = pedir_texto("Codigo: ")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoria: ")

    try:
        precio = pedir_float("Precio: ")
        stock = pedir_entero("Stock: ")

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        registrado = restaurante.registrar_producto(
            producto
        )

        if registrado:
            print("Producto registrado correctamente.")
            guardar_productos(
                archivo_servicio,
                restaurante
            )
        else:
            print("El codigo ya se encuentra registrado.")

    except ValueError as error:
        print(error)


def buscar_producto(
    restaurante: Restaurante
) -> None:

    print("\n--- Buscar producto ---")

    codigo = pedir_texto(
        "Codigo del producto: "
    )

    producto = restaurante.buscar_producto(
        codigo
    )

    if producto is None:
        print("Producto no encontrado.")
    else:
        print(producto)


def actualizar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- Actualizar producto ---")

    codigo = pedir_texto(
        "Codigo del producto: "
    )

    if restaurante.buscar_producto(codigo) is None:
        print("Producto no encontrado.")
        return

    nombre = pedir_texto("Nuevo nombre: ")
    categoria = pedir_texto("Nueva categoria: ")

    try:
        precio = pedir_float("Nuevo precio: ")
        stock = pedir_entero("Nuevo stock: ")

        actualizado = restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        if actualizado:
            print("Producto actualizado correctamente.")
            guardar_productos(
                archivo_servicio,
                restaurante
            )
        else:
            print("No fue posible actualizar el producto.")

    except ValueError as error:
        print(error)


def eliminar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- Eliminar producto ---")

    codigo = pedir_texto(
        "Codigo del producto: "
    )

    eliminado = restaurante.eliminar_producto(
        codigo
    )

    if eliminado:
        print("Producto eliminado correctamente.")
        guardar_productos(
            archivo_servicio,
            restaurante
        )
    else:
        print("Producto no encontrado.")


def listar_productos(
    restaurante: Restaurante
) -> None:

    print("\n--- Lista de productos ---")

    productos = restaurante.listar_productos()

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for indice, producto in enumerate(productos):
        print(f"{indice + 1}. {producto}")

    print(
        f"\nTotal de productos: "
        f"{restaurante.contar_productos()}"
    )


# ==========================
# USUARIOS
# ==========================

def registrar_usuario(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- Registrar usuario ---")

    identificacion = pedir_texto(
        "Identificacion: "
    )

    nombre = pedir_texto(
        "Nombre: "
    )

    try:
        usuario = Usuario(
            identificacion,
            nombre
        )

        registrado = restaurante.registrar_usuario(
            usuario
        )

        if registrado:
            print("Usuario registrado correctamente.")
            guardar_usuarios(
                archivo_servicio,
                restaurante
            )
        else:
            print(
                "La identificacion ya se encuentra registrada."
            )

    except ValueError as error:
        print(error)


def buscar_usuario(
    restaurante: Restaurante
) -> None:

    print("\n--- Buscar usuario ---")

    identificacion = pedir_texto(
        "Identificacion del usuario: "
    )

    usuario = restaurante.buscar_usuario(
        identificacion
    )

    if usuario is None:
        print("Usuario no encontrado.")
    else:
        print(usuario)


def actualizar_usuario(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- Actualizar usuario ---")

    identificacion = pedir_texto(
        "Identificacion del usuario: "
    )

    if restaurante.buscar_usuario(
        identificacion
    ) is None:

        print("Usuario no encontrado.")
        return

    nuevo_nombre = pedir_texto(
        "Nuevo nombre: "
    )

    try:
        actualizado = restaurante.actualizar_usuario(
            identificacion,
            nuevo_nombre
        )

        if actualizado:
            print("Usuario actualizado correctamente.")
            guardar_usuarios(
                archivo_servicio,
                restaurante
            )
        else:
            print("Usuario no encontrado.")

    except ValueError as error:
        print(error)


def eliminar_usuario(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:

    print("\n--- Eliminar usuario ---")

    identificacion = pedir_texto(
        "Identificacion del usuario: "
    )

    eliminado = restaurante.eliminar_usuario(
        identificacion
    )

    if eliminado:
        print("Usuario eliminado correctamente.")
        guardar_usuarios(
            archivo_servicio,
            restaurante
        )
    else:
        print("Usuario no encontrado.")


def listar_usuarios(
    restaurante: Restaurante
) -> None:

    print("\n--- Lista de usuarios ---")

    usuarios = restaurante.listar_usuarios()

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    for indice, usuario in enumerate(usuarios):
        print(f"{indice + 1}. {usuario}")


# ==========================
# VENTAS
# ==========================

def vender_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    print("\n--- Vender producto ---")

    codigo_producto = pedir_texto(
        "Codigo del producto: "
    )

    identificacion_usuario = pedir_texto(
        "Identificacion del usuario: "
    )

    producto = restaurante.buscar_producto(
        codigo_producto
    )

    usuario = restaurante.buscar_usuario(
        identificacion_usuario
    )

    if usuario is None:
        print("Usuario no encontrado.")
        return

    if producto is None:
        print("Producto no encontrado.")
        return

    try:
        cantidad = pedir_entero(
            "Cantidad (Enter para 1): ",
            1
        )

        if cantidad <= 0:
            print(
                "La cantidad debe ser mayor que cero."
            )
            return

        if producto.stock < cantidad:
            print("No hay stock suficiente.")
            return

        vendido = restaurante.vender_producto(
            codigo_producto,
            identificacion_usuario,
            cantidad
        )

        if vendido:
            print(
                f"Venta registrada correctamente. "
                f"Stock actual: {producto.stock}"
            )

            guardar_ventas(
                archivo_servicio,
                restaurante
            )

            guardar_productos(
                archivo_servicio,
                restaurante
            )

        else:
            print(
                "No fue posible realizar la venta."
            )

    except ValueError as error:
        print(error)


def consultar_ventas_usuario(
    restaurante: Restaurante
) -> None:
    print("\n--- Ventas de usuario ---")

    identificacion = pedir_texto(
        "Identificacion del usuario: "
    )

    usuario = restaurante.buscar_usuario(
        identificacion
    )

    if usuario is None:
        print("Usuario no encontrado.")
        return

    ventas = restaurante.consultar_ventas_usuario(
        identificacion
    )

    print(f"\nUsuario: {usuario.nombre}")

    if len(ventas) == 0:
        print("Sin ventas registradas.")
        return

    print("\nVentas:")

    for venta in ventas:
        producto = restaurante.buscar_producto(
            venta.id_producto
        )

        nombre = (
            producto.nombre
            if producto is not None
            else "Producto no encontrado"
        )

        print(
            f"- {venta.id_producto} | "
            f"{nombre} | "
            f"Cantidad: {venta.cantidad}"
        )


# ==========================
# CATEGORIAS
# ==========================

def listar_categorias_unicas(
    restaurante: Restaurante
) -> None:

    print("\n--- Categorias unicas ---")

    categorias = restaurante.obtener_categorias_unicas()

    if len(categorias) == 0:
        print("No hay categorias registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")

    categoria_consultada = pedir_texto(
        "\nConsultar si existe una categoria "
        "(Enter para omitir): "
    )

    if categoria_consultada:

        if restaurante.existe_categoria(
            categoria_consultada
        ):
            print(
                "La categoria existe en el restaurante."
            )
        else:
            print(
                "La categoria no existe en el restaurante."
            )


# ==========================
# EJECUCION PRINCIPAL
# ==========================

def ejecutar_menu() -> None:

    ruta_datos = (
        Path(__file__).resolve().parent
        / "datos"
    )

    archivo_servicio = ArchivoServicio(
        str(ruta_datos)
    )

    restaurante = Restaurante(
        productos_iniciales=(
            archivo_servicio.cargar_productos()
        ),
        usuarios_iniciales=(
            archivo_servicio.cargar_usuarios()
        ),
        ventas_iniciales=(
            archivo_servicio.cargar_ventas()
        ),
    )

    opciones = {
        "1": lambda: registrar_producto(
            restaurante,
            archivo_servicio
        ),

        "2": lambda: buscar_producto(
            restaurante
        ),

        "3": lambda: actualizar_producto(
            restaurante,
            archivo_servicio
        ),

        "4": lambda: eliminar_producto(
            restaurante,
            archivo_servicio
        ),

        "5": lambda: listar_productos(
            restaurante
        ),

        "6": lambda: registrar_usuario(
            restaurante,
            archivo_servicio
        ),

        "7": lambda: buscar_usuario(
            restaurante
        ),

        "8": lambda: actualizar_usuario(
            restaurante,
            archivo_servicio
        ),

        "9": lambda: eliminar_usuario(
            restaurante,
            archivo_servicio
        ),

        "10": lambda: listar_usuarios(
            restaurante
        ),

        "11": lambda: vender_producto(
            restaurante,
            archivo_servicio
        ),

        "12": lambda: consultar_ventas_usuario(
            restaurante
        ),

        "13": lambda: listar_categorias_unicas(
            restaurante
        ),
    }

    while True:

        mostrar_menu()

        opcion = pedir_texto(
            "Seleccione una opcion: "
        )

        if opcion == "0":
            print(
                "Gracias por usar Restaurante App."
            )
            break

        accion = opciones.get(opcion)

        if accion is None:
            print("Opcion invalida.")
        else:
            accion()


if __name__ == "__main__":
    ejecutar_menu()