import tkinter as tk
from tkinter import messagebox
from Figuras.esfera import Esfera

class VentanaEsfera(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)
        self.inicializar_componentes()

    def inicializar_componentes(self):
    
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.entry_radio = tk.Entry(self)
        self.entry_radio.place(x=100, y=20)

        boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        boton_calcular.place(x=100, y=50)

        self.label_volumen = tk.Label(self, text="Volumen (cm³):")
        self.label_volumen.place(x=20, y=90)

        self.label_superficie = tk.Label(self, text="Superficie (cm²):")
        self.label_superficie.place(x=20, y=120)

    def calcular(self):
        try:
            radio = float(self.entry_radio.get())
            esfera = Esfera(radio)
            self.label_volumen.config(text=f"Volumen (cm³): {esfera.get_volumen():.2f}")
            self.label_superficie.config(text=f"Superficie (cm²): {esfera.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")