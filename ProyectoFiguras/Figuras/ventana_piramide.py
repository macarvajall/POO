import tkinter as tk
from tkinter import messagebox
from Figuras.piramide import Piramide

class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)
        self.inicializar_componentes()

    def inicializar_componentes(self):
        # Campo Base
        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.entry_base = tk.Entry(self)
        self.entry_base.place(x=120, y=20)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.entry_altura = tk.Entry(self)
        self.entry_altura.place(x=120, y=50)

        tk.Label(self, text="Apotema (cms):").place(x=20, y=80)
        self.entry_apotema = tk.Entry(self)
        self.entry_apotema.place(x=120, y=80)

        boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        boton_calcular.place(x=120, y=110)

        self.label_volumen = tk.Label(self, text="Volumen (cm³):")
        self.label_volumen.place(x=20, y=140)

        self.label_superficie = tk.Label(self, text="Superficie (cm²):")
        self.label_superficie.place(x=20, y=170)

    def calcular(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            apotema = float(self.entry_apotema.get())
            piramide = Piramide(base, altura, apotema)
            self.label_volumen.config(text=f"Volumen (cm³): {piramide.get_volumen():.2f}")
            self.label_superficie.config(text=f"Superficie (cm²): {piramide.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")