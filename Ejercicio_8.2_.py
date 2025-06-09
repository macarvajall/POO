import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    def __init__(self):
        self.listaNotas = [0.0] * 5

    def calcular_promedio(self):
        return sum(self.listaNotas) / len(self.listaNotas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = sum((nota - promedio) ** 2 for nota in self.listaNotas)
        return math.sqrt(suma / len(self.listaNotas))  

    def calcular_mayor(self):
        return max(self.listaNotas)

    def calcular_menor(self):
        return min(self.listaNotas)

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("300x380")
        self.root.resizable(False, False)

        self.nota_fields = []
        for i in range(5):
            label = tk.Label(root, text=f"Nota {i+1}:")
            label.place(x=20, y=20 + i*30)
            entry = tk.Entry(root)
            entry.place(x=100, y=20 + i*30, width=150)
            self.nota_fields.append(entry)

        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=40, y=180, width=100)

        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(x=160, y=180, width=100)

        self.label_promedio = tk.Label(root, text="Promedio = ")
        self.label_promedio.place(x=20, y=230)

        self.label_desviacion = tk.Label(root, text="Desviación estándar = ")
        self.label_desviacion.place(x=20, y=260)

        self.label_mayor = tk.Label(root, text="Nota mayor = ")
        self.label_mayor.place(x=20, y=290)

        self.label_menor = tk.Label(root, text="Nota menor = ")
        self.label_menor.place(x=20, y=320)

    def calcular(self):
        notas = Notas()
        try:
            for i in range(5):
                notas.listaNotas[i] = float(self.nota_fields[i].get())

            promedio = notas.calcular_promedio()
            desviacion = notas.calcular_desviacion()
            mayor = notas.calcular_mayor()
            menor = notas.calcular_menor()

            self.label_promedio.config(text=f"Promedio = {promedio:.2f}")
            self.label_desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
            self.label_mayor.config(text=f"Nota mayor = {mayor:.2f}")
            self.label_menor.config(text=f"Nota menor = {menor:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos en todas las notas.")

    def limpiar(self):
        for campo in self.nota_fields:
            campo.delete(0, tk.END)
        self.label_promedio.config(text="Promedio = ")
        self.label_desviacion.config(text="Desviación estándar = ")
        self.label_mayor.config(text="Nota mayor = ")
        self.label_menor.config(text="Nota menor = ")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
