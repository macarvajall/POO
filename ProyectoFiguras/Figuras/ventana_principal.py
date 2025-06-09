import tkinter as tk
from Figuras.ventana_cilindro import VentanaCilindro
from Figuras.ventana_esfera import VentanaEsfera
from Figuras.ventana_piramide import VentanaPiramide

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)
        self.inicializar_componentes()

    def inicializar_componentes(self):
        boton_cilindro = tk.Button(self, text="Cilindro", width=10, command=self.abrir_cilindro)
        boton_cilindro.place(x=20, y=50)

        boton_esfera = tk.Button(self, text="Esfera", width=10, command=self.abrir_esfera)
        boton_esfera.place(x=125, y=50)

        boton_piramide = tk.Button(self, text="Pirámide", width=10, command=self.abrir_piramide)
        boton_piramide.place(x=230, y=50)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)