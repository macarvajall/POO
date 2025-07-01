# Ejercicio página 412

import tkinter as tk
from tkinter import messagebox
import math

class CalculosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos Numéricos")

        # Etiqueta e input
        tk.Label(root, text="Ingrese un número positivo:").pack(pady=10)
        self.valor_entry = tk.Entry(root, width=30)
        self.valor_entry.pack(pady=5)

        # Botón
        tk.Button(root, text="Calcular", command=self.calcular).pack(pady=10)

    def calcular(self):
        errores = []
        try:
            valor = float(self.valor_entry.get())

            # Verificación de valor negativo
            if valor < 0:
                errores.append("Error: El valor debe ser un número positivo para calcular el logaritmo")
                errores.append("Error: El valor debe ser un número positivo para calcular la raíz cuadrada")
            else:
                # Cálculo si es válido
                ln_val = math.log(valor)
                sqrt_val = math.sqrt(valor)

                resultado = (
                    f"ln({valor}) = {ln_val:.4f}\n"
                    f" √{valor} = {sqrt_val:.4f}"
                )
                messagebox.showinfo("Resultados", resultado)

        except ValueError:
            errores.append("Error: El valor debe ser numérico")

        # Mostrar errores si hay
        if errores:
            messagebox.showerror("Errores encontrados", "\n".join(errores))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculosApp(root)
    root.mainloop()
