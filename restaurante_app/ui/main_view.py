import tkinter as tk

class MainView(tk.Tk):
    def __init__(self, usuario):
        super().__init__()
        self.title("Restaurante 'Sabor de Casa'")
        self.geometry("700x250")
        self.configure(bg="#e6ffe6")  

        tk.Label(self, text=f"Bienvenido {usuario.nombre}", font=("Arial", 14, "bold"),
                 bg="#e6ffe6", fg="#006400").pack(pady=10)

        frame_botones = tk.Frame(self, bg="#e6ffe6")
        frame_botones.pack(pady=20)

        btn_producto = tk.Button(frame_botones, text="Registrar producto", bg="#ffcc00", fg="black", width=18)
        btn_usuario = tk.Button(frame_botones, text="Registrar usuario", bg="#ffcc00", fg="black", width=18)
        btn_ventas = tk.Button(frame_botones, text="Ver ventas", bg="#ffcc00", fg="black", width=18)
        btn_salir = tk.Button(frame_botones, text="Salir", bg="#cc0000", fg="white", width=18, command=self.destroy)

        btn_producto.grid(row=0, column=0, padx=10)
        btn_usuario.grid(row=0, column=1, padx=10)
        btn_ventas.grid(row=0, column=2, padx=10)
        btn_salir.grid(row=0, column=3, padx=10)
