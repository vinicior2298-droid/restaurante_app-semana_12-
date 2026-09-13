# Restaurante App - "Sabor de Casa"

## Autor:
Richard Vinicio Morocho Torres 

## Propósito
Esta aplicación fue desarrollada como una base para gestionar un restaurante ficticio llamado **"Sabor de Casa"**.  
Su objetivo es permitir el registro de productos, usuarios y ventas, además de ofrecer un flujo de inicio de sesión seguro y una interfaz gráfica amigable.

## Estructura de carpetas y archivos
restaurante_app/
├── datos/
│   ├── usuarios.json      
│   ├── productos.json     
│   └── ventas.json        
├── modelos/
│   ├── usuario.py        
│   ├── producto.py       
│   └── venta.py           
├── servicios/
│   └── archivo_servicio.py 
├── ui/
│   ├── login_view.py      
│   └── main_view.py      
└── main.py       

## Flujo de la aplicación
1. El usuario abre la aplicación ejecutando `main.py`.  
2. Se muestra la **ventana de login** (`login_view.py`).  
3. Si las credenciales son correctas, la ventana de login se cierra y se abre la **ventana principal** (`main_view.py`).  
4. Desde la ventana principal se pueden realizar las siguientes acciones:
   - Registrar producto  
   - Registrar usuario  
   - Ver ventas  
   - Salir de la aplicación  

## Vistas implementadas
- **LoginView**:  
  - Fondo azul claro, campos para usuario y contraseña.  
  - Botón de inicio de sesión.  
  - Validación contra el archivo `usuarios.json`.

- **MainView**:  
  - Fondo verde claro, mensaje de bienvenida con el nombre del usuario.  
  - Botones en **horizontal** para las acciones principales.  
  - Botón rojo para salir.

## Pasos para ejecutar `main.py`
1. Asegúrate de tener instalado **Python 3.10+**.  
2. Verifica que los archivos `usuarios.json`, `productos.json` y `ventas.json` estén dentro de la carpeta `restaurante_app/datos`.  
3. Abre una terminal en la carpeta del proyecto.  
4. Ejecuta el comando:
   ```bash
   python restaurante_app/main.py 


