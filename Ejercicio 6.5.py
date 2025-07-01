
# Ejercicio página 406

import tkinter as tk
from tkinter import messagebox

class VendedorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vendedor")

        # Etiquetas
        tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Label(root, text="Apellidos:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Label(root, text="Edad:").grid(row=2, column=0, padx=10, pady=5, sticky="e")

        # Entradas
        self.nombre = tk.Entry(root)
        self.apellidos = tk.Entry(root)
        self.edad = tk.Entry(root)

        self.nombre.grid(row=0, column=1, padx=10, pady=5)
        self.apellidos.grid(row=1, column=1, padx=10, pady=5)
        self.edad.grid(row=2, column=1, padx=10, pady=5)

        # Botón
        tk.Button(root, text="Registrar", command=self.registrar).grid(row=3, column=0, columnspan=2, pady=10)

    def registrar(self):
        try:
            edad_valor = int(self.edad.get())
            if edad_valor < 18:
                raise ValueError("El vendedor debe ser mayor de 18 años.")
            if not (0 <= edad_valor <= 120):
                raise ValueError("La edad debe estar entre 0 y 120 años.")

            info = (
                f"Nombre: {self.nombre.get()}\n"
                f"Apellidos: {self.apellidos.get()}\n"
                f"Edad: {edad_valor} años"
            )
            messagebox.showinfo("Datos del Vendedor", info)

        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = VendedorApp(root)
    root.mainloop()