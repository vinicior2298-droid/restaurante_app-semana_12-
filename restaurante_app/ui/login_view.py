import tkinter as tk
from tkinter import messagebox
from ui.main_view import MainView

class LoginView(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio

        self.title("Acceso al Sistema - Restaurante")
        self.geometry("380x300")
        self.resizable(False, False)
        self.config(bg="#f4f6f7")

        self._crear_interfaz()

    def _crear_interfaz(self):
        lbl_titulo = tk.Label(
            self, text="INICIAR SESIÓN", font=("Arial", 14, "bold"), 
            bg="#f4f6f7", fg="#2c3e50"
        )
        lbl_titulo.pack(pady=15)

        frm_campos = tk.Frame(self, bg="#f4f6f7")
        frm_campos.pack(pady=10)

        tk.Label(frm_campos, text="Usuario:", font=("Arial", 10), bg="#f4f6f7").grid(row=0, column=0, sticky="e", pady=8)
        self.ent_usuario = tk.Entry(frm_campos, font=("Arial", 10))
        self.ent_usuario.grid(row=0, column=1, pady=8, padx=5)

        tk.Label(frm_campos, text="Contraseña:", font=("Arial", 10), bg="#f4f6f7").grid(row=1, column=0, sticky="e", pady=8)
        self.ent_clave = tk.Entry(frm_campos, show="*", font=("Arial", 10))
        self.ent_clave.grid(row=1, column=1, pady=8, padx=5)

        btn_ingresar = tk.Button(
            self, text="INGRESAR", command=self._validar_login, 
            bg="#2980b9", fg="white", font=("Arial", 10, "bold"), width=15, height=1
        )
        btn_ingresar.pack(pady=20)

    def _validar_login(self):
        usr = self.ent_usuario.get().strip()
        clv = self.ent_clave.get().strip()

        if not usr or not clv:
            messagebox.showwarning("Atención", "Ingrese usuario y contraseña.")
            return

        usuario_valido = self.servicio.autenticar(usr, clv)
        if usuario_valido:
            self.destroy()
            app_principal = MainView(self.servicio, usuario_valido)
            app_principal.mainloop()
        else:
            messagebox.showerror("Error de Acceso", "Credenciales incorrectas.")