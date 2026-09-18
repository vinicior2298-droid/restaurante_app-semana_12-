import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Tk):
    def __init__(self, servicio, usuario_actual):
        super().__init__()
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        self.title(f"Sistema Restaurante - Usuario: {self.usuario_actual.nombre}")
        self.geometry("900x550")
        self.minsize(800, 500)

        self._crear_interfaz()

    def _crear_interfaz(self):
        self.frame_menu = tk.Frame(self, bg="#2c3e50", width=200)
        self.frame_menu.pack(side="left", fill="y")

        self.frame_contenido = tk.Frame(self, bg="#ecf0f1")
        self.frame_contenido.pack(side="right", expand=True, fill="both")

        lbl_titulo = tk.Label(
            self.frame_menu, text="MENÚ", bg="#2c3e50", fg="white", 
            font=("Arial", 14, "bold")
        )
        lbl_titulo.pack(pady=20)

        btn_productos = tk.Button(
            self.frame_menu, text="Gestión de Productos", 
            command=self.mostrar_productos, width=18, bg="#34495e", fg="white"
        )
        btn_productos.pack(pady=10)

        btn_usuarios = tk.Button(
            self.frame_menu, text="Consulta de Usuarios", 
            command=self.mostrar_usuarios, width=18, bg="#34495e", fg="white"
        )
        btn_usuarios.pack(pady=10)

        btn_salir = tk.Button(
            self.frame_menu, text="Cerrar Sesión", 
            command=self.destroy, width=18, bg="#c0392b", fg="white"
        )
        btn_salir.pack(side="bottom", pady=20)

        self.mostrar_productos()

    def _limpiar_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    # ==================== SECCIÓN DE PRODUCTOS ====================
    def mostrar_productos(self):
        self._limpiar_contenido()

        lbl_sec = tk.Label(
            self.frame_contenido, text="GESTIÓN DE PRODUCTOS", 
            font=("Arial", 16, "bold"), bg="#ecf0f1"
        )
        lbl_sec.pack(pady=10)

        frm_form = tk.LabelFrame(
            self.frame_contenido, text=" Datos del Producto ", 
            font=("Arial", 11, "bold"), bg="#ecf0f1", padx=10, pady=10
        )
        frm_form.pack(fill="x", padx=15, pady=5)

        tk.Label(frm_form, text="Código:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.ent_id = tk.Entry(frm_form)
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frm_form, text="Nombre:", bg="#ecf0f1").grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.ent_nombre = tk.Entry(frm_form)
        self.ent_nombre.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frm_form, text="Categoría:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.cmb_categoria = ttk.Combobox(
            frm_form, values=["Platos", "Bebidas", "Postres", "Entradas"], state="readonly"
        )
        self.cmb_categoria.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frm_form, text="Precio ($):", bg="#ecf0f1").grid(row=1, column=2, sticky="e", padx=5, pady=5)
        self.ent_precio = tk.Entry(frm_form)
        self.ent_precio.grid(row=1, column=3, padx=5, pady=5)

        frm_botones = tk.Frame(self.frame_contenido, bg="#ecf0f1")
        frm_botones.pack(fill="x", padx=15, pady=5)

        tk.Button(
            frm_botones, text="Registrar", command=self._registrar_producto, 
            bg="#2ecc71", fg="white", width=12
        ).pack(side="left", padx=5)

        tk.Button(
            frm_botones, text="Cargar/Buscar", command=self._consultar_producto, 
            bg="#3498db", fg="white", width=12
        ).pack(side="left", padx=5)

        tk.Button(
            frm_botones, text="Actualizar", command=self._actualizar_producto, 
            bg="#f39c12", fg="white", width=12
        ).pack(side="left", padx=5)

        tk.Button(
            frm_botones, text="Eliminar", command=self._eliminar_producto, 
            bg="#e74c3c", fg="white", width=12
        ).pack(side="left", padx=5)

        tk.Button(
            frm_botones, text="Limpiar", command=self._limpiar_formulario, 
            bg="#95a5a6", fg="white", width=10
        ).pack(side="right", padx=5)

        frm_tabla = tk.LabelFrame(
            self.frame_contenido, text=" Listado de Productos ", 
            font=("Arial", 11, "bold"), bg="#ecf0f1", padx=5, pady=5
        )
        frm_tabla.pack(fill="both", expand=True, padx=15, pady=10)

        scroll = ttk.Scrollbar(frm_tabla, orient="vertical")
        scroll.pack(side="right", fill="y")

        self.tree_prod = ttk.Treeview(
            frm_tabla, columns=("codigo", "nombre", "categoria", "precio", "stock"), 
            show="headings", yscrollcommand=scroll.set
        )
        scroll.config(command=self.tree_prod.yview)

        self.tree_prod.heading("codigo", text="Código")
        self.tree_prod.heading("nombre", text="Nombre")
        self.tree_prod.heading("categoria", text="Categoría")
        self.tree_prod.heading("precio", text="Precio ($)")
        self.tree_prod.heading("stock", text="Stock")

        self.tree_prod.column("codigo", width=80, anchor="center")
        self.tree_prod.column("nombre", width=200)
        self.tree_prod.column("categoria", width=120)
        self.tree_prod.column("precio", width=90, anchor="e")
        self.tree_prod.column("stock", width=70, anchor="center")

        self.tree_prod.pack(fill="both", expand=True)

        self._cargar_tabla_productos()

    def _cargar_tabla_productos(self):
        for item in self.tree_prod.get_children():
            self.tree_prod.delete(item)

        productos = self.servicio.listar_productos()
        for p in productos:
            self.tree_prod.insert("", "end", values=(p.codigo, p.nombre, p.categoria, f"{p.precio:.2f}", p.stock))

    def _limpiar_formulario(self):
        self.ent_id.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.cmb_categoria.set("")
        self.ent_precio.delete(0, tk.END)

    def _registrar_producto(self):
        id_p = self.ent_id.get().strip()
        nom = self.ent_nombre.get().strip()
        cat = self.cmb_categoria.get().strip()
        pre = self.ent_precio.get().strip()

        if not id_p or not nom or not cat or not pre:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
            return

        try:
            precio_val = float(pre)
            exito, msj = self.servicio.registrar_producto(id_p, nom, cat, precio_val)
            if exito:
                messagebox.showinfo("Éxito", msj)
                self._limpiar_formulario()
                self._cargar_tabla_productos()
            else:
                messagebox.showerror("Error", msj)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido.")

    def _consultar_producto(self):
        id_p = self.ent_id.get().strip()
        if not id_p:
            messagebox.showwarning("Atención", "Ingrese el código del producto a consultar.")
            return

        prod = self.servicio.obtener_producto_por_id(id_p)
        if prod:
            self.ent_nombre.delete(0, tk.END)
            self.ent_nombre.insert(0, prod.nombre)
            self.cmb_categoria.set(prod.categoria)
            self.ent_precio.delete(0, tk.END)
            self.ent_precio.insert(0, str(prod.precio))
            messagebox.showinfo("Cargado", f"Producto '{prod.nombre}' cargado en el formulario.")
        else:
            messagebox.showerror("Error", "Producto no encontrado.")

    def _actualizar_producto(self):
        id_p = self.ent_id.get().strip()
        nom = self.ent_nombre.get().strip()
        cat = self.cmb_categoria.get().strip()
        pre = self.ent_precio.get().strip()

        if not id_p or not nom or not cat or not pre:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
            return

        try:
            precio_val = float(pre)
            exito, msj = self.servicio.actualizar_producto(id_p, nom, cat, precio_val)
            if exito:
                messagebox.showinfo("Éxito", msj)
                self._limpiar_formulario()
                self._cargar_tabla_productos()
            else:
                messagebox.showerror("Error", msj)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un valor numérico.")

    def _eliminar_producto(self):
        id_p = self.ent_id.get().strip()
        if not id_p:
            messagebox.showwarning("Atención", "Ingrese el código del producto a eliminar.")
            return

        if messagebox.askyesno("Confirmar", f"¿Desea eliminar el producto con código {id_p}?"):
            exito, msj = self.servicio.eliminar_producto(id_p)
            if exito:
                messagebox.showinfo("Éxito", msj)
                self._limpiar_formulario()
                self._cargar_tabla_productos()
            else:
                messagebox.showerror("Error", msj)

    # ==================== SECCIÓN DE USUARIOS ====================
    def mostrar_usuarios(self):
        self._limpiar_contenido()

        lbl_sec = tk.Label(
            self.frame_contenido, text="CONSULTA DE USUARIOS", 
            font=("Arial", 16, "bold"), bg="#ecf0f1"
        )
        lbl_sec.pack(pady=15)

        frm_tabla = tk.LabelFrame(
            self.frame_contenido, text=" Usuarios del Sistema ", 
            font=("Arial", 11, "bold"), bg="#ecf0f1", padx=10, pady=10
        )
        frm_tabla.pack(fill="both", expand=True, padx=20, pady=10)

        scroll = ttk.Scrollbar(frm_tabla, orient="vertical")
        scroll.pack(side="right", fill="y")

        tree_usr = ttk.Treeview(
            frm_tabla, columns=("identificacion", "nombre"), 
            show="headings", yscrollcommand=scroll.set
        )
        scroll.config(command=tree_usr.yview)

        tree_usr.heading("identificacion", text="Identificación")
        tree_usr.heading("nombre", text="Nombre")

        tree_usr.column("identificacion", width=150, anchor="center")
        tree_usr.column("nombre", width=300)

        tree_usr.pack(fill="both", expand=True)

        usuarios = self.servicio.listar_usuarios()
        for u in usuarios:
            tree_usr.insert("", "end", values=(u.identificacion, u.nombre))