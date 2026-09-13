import tkinter as tk
from tkinter import messagebox
from servicios.archivo_servicio import ArchivoServicio
from ui.main_view import MainView

class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurante 'Sabor de Casa'")
        self.geometry("400x250")
        self.configure(bg="#f0f8ff")  
        self.archivo_servicio = ArchivoServicio()
        
        tk.Label(self, text="Ingreso a la plataforma", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#333").pack(pady=10)

        tk.Label(self, text="Usuario", bg="#f0f8ff", fg="#333").pack()
        self.entry_usuario = tk.Entry(self, bg="#fff", fg="#000")
        self.entry_usuario.pack()

        tk.Label(self, text="Contraseña", bg="#f0f8ff", fg="#333").pack()
        self.entry_contraseña = tk.Entry(self, show="*", bg="#fff", fg="#000")
        self.entry_contraseña.pack()

        tk.Button(self, text="Iniciar sesión", bg="#4682b4", fg="white", font=("Arial", 10, "bold"),
                  command=self.iniciar_sesion).pack(pady=15)

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()

        usuario_validado = self.archivo_servicio.validar_acceso(usuario, contraseña)

        if usuario_validado:
            self.destroy()  
            MainView(usuario_validado).mainloop()  
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
