# Restaurante App - Semana 12

## 📌 Descripción de mejoras realizadas
En esta versión se optimizó el rendimiento de las búsquedas y consultas dentro de la aplicación **restaurante_app**, manteniendo la arquitectura modular y las funcionalidades de la Semana 11.  
Las mejoras principales fueron:
- Implementación de **índices en memoria** con `dict` para búsquedas rápidas de productos por código y usuarios por identificación.
- Optimización de la consulta de ventas por usuario, evitando recorrer toda la colección en cada consulta.
- Uso de `set` únicamente para validaciones de pertenencia y valores únicos.
- Sincronización automática de las estructuras auxiliares al registrar, modificar o eliminar datos.
- Reconstrucción de índices al iniciar el programa a partir de los objetos cargados desde los archivos JSON.

---

## 📂 Colecciones utilizadas
- **Listas (`list`)**:  
  - Conservadas como colecciones principales para almacenar y recorrer productos, usuarios y ventas.  
- **Diccionarios (`dict`)**:  
  - Índice de productos por código.  
  - Índice de usuarios por identificación.  
  - Índice de ventas por usuario.  
- **Conjuntos (`set`)**:  
  - Validaciones de unicidad y pertenencia en registros específicos.  

---

## ✅ Pruebas principales realizadas
1. Registro y carga de usuarios, productos y ventas desde JSON.
2. Búsqueda de un producto mediante su código utilizando el índice auxiliar.
3. Búsqueda de un usuario mediante su identificación.
4. Consulta de ventas relacionadas con un usuario sin recorrer toda la lista completa.
5. Realización de una venta y verificación de la actualización correcta del stock.
6. Comprobación de la coherencia entre listas principales e índices auxiliares después de modificar datos.
7. Cierre y nueva ejecución del programa para confirmar la reconstrucción de índices desde JSON.
