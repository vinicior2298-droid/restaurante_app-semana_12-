# Sistema de Gestión de Restaurante - POO & Tkinter

# Autor: Richard Vinicio Morocho Torres 

Este proyecto es una aplicación de escritorio desarrollada en **Python** empleando la librería gráfica **Tkinter**. Aplica principios de **Programación Orientada a Objetos (POO)** y la separación de responsabilidades mediante una arquitectura por capas (Modelos, Servicios e Interfaz de Usuario).


## Características Principales

* **Autenticación de Usuarios:** Sistema de inicio de sesión con validación de credenciales.
* **Gestión de Productos (CRUD):** 
  * Registro de nuevos productos.
  * Consulta y búsqueda por código.
  * Actualización de información (nombre, categoría, precio).
  * Eliminación de productos.
* **Persistencia de Datos:** Lectura y escritura en archivos JSON para mantener la información guardada localmente.
* **Control e Interfaz Gráfica:**
  * Uso de componentes Tkinter y `ttk.Treeview` para tablas interactivas.
  * Validaciones de entradas de datos (precios positivos, textos no vacíos, formatos válidos).



## Estructura del Proyecto

proyecto_restaurante/
│
├── datos/                  
│   ├── productos.json      
│   └── usuarios.json      
│
├── modelos/                
│   ├── producto.py         
│   ├── usuario.py         
│   └── venta.py            
│
├── servicios/              
│   ├── archivo_servicio.py     
│   └── restaurante_servicio.py 
│
├── ui/                     
│   ├── login_view.py       
│   └── main_view.py        
│
├── main.py                
└── README.md               

# Arquitectura y Patrones Aplicados

* **Encapsulamiento y Validaciones:** Métodos estáticos @staticmethod dentro de las clases modelo para garantizar que ningún dato corrupto o inválido sea instanciado.

* **Inyección de Dependencias:** El servicio de persistencia ArchivoServicio se inyecta en RestauranteServicio, permitiendo desacoplar el almacenamiento de la lógica del negocio.

* **Model-View Pattern:** La capa de presentación (ui) interactúa únicamente con la capa de servicios (servicios), manteniendo el código limpio y mantenible.