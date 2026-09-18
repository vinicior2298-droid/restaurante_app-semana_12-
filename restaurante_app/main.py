import os
import sys

# Asegurar que el directorio raíz del proyecto esté en el path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from modelos.usuario import Usuario
from ui.login_view import LoginView

def inicializar_datos_demo(archivo_servicio: ArchivoServicio):
    """Crea un usuario por defecto si la base de datos de usuarios está vacía."""
    usuarios = archivo_servicio.cargar_usuarios()
    if not usuarios:
        try:
            # Crea un usuario admin por defecto (Id: admin, Nombre: Administrador, Pass: admin123)
            user_demo = Usuario("admin", "Administrador", "admin123")
            archivo_servicio.guardar_usuarios([user_demo])
        except Exception as e:
            print(f"Nota: No se pudo crear el usuario demo automático: {e}")

def main():
    archivo_servicio = ArchivoServicio()
    
    # Asegurar que exista al menos un usuario para iniciar sesión
    inicializar_datos_demo(archivo_servicio)

    restaurante_servicio = RestauranteServicio(archivo_servicio)

    # Iniciar la ventana gráfica de login
    app = LoginView(restaurante_servicio)
    app.mainloop()

if __name__ == "__main__":
    main()