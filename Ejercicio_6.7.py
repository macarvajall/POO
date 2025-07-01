import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Clase Programador
# -----------------------------
class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

# -----------------------------
# Clase EquipoMaratonProgramacion
# -----------------------------
class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []

    def anadir_programador(self, programador):
        if len(self.programadores) >= 3:
            raise Exception("El equipo no puede tener más de 3 programadores.")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(texto):
        if any(char.isdigit() for char in texto):
            raise Exception("El campo no puede contener dígitos.")
        if len(texto) > 20:
            raise Exception("El campo no debe tener más de 20 caracteres.")

# -----------------------------
# Función para registrar el equipo
# -----------------------------
def registrar_equipo():
    try:
        nombre_equipo = entry_nombre_equipo.get().strip()
        universidad = entry_universidad.get().strip()
        lenguaje = entry_lenguaje.get().strip()

        if not nombre_equipo or not universidad or not lenguaje:
            raise Exception("Todos los campos del equipo son obligatorios.")

        equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje)

        # Capturar y validar los programadores
        programadores_validos = 0
        for i in range(3):
            nombre = entries_nombres[i].get().strip()
            apellidos = entries_apellidos[i].get().strip()

            if nombre and apellidos:
                EquipoMaratonProgramacion.validar_campo(nombre)
                EquipoMaratonProgramacion.validar_campo(apellidos)
                equipo.anadir_programador(Programador(nombre, apellidos))
                programadores_validos += 1
            elif nombre or apellidos:
                raise Exception(f"Debes completar nombre y apellidos del integrante {i+1} o dejar ambos en blanco.")

        if programadores_validos < 2:
            raise Exception("Debes registrar al menos 2 programadores.")

        messagebox.showinfo("Éxito", f"Equipo '{equipo.nombre_equipo}' registrado correctamente con {programadores_validos} integrantes.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# -----------------------------
# Interfaz gráfica
# -----------------------------
ventana = tk.Tk()
ventana.title("Ejercicio 6.7 - Registro de Equipo (mínimo 2 integrantes)")
ventana.geometry("550x600")

# Sección: Datos del equipo
tk.Label(ventana, text="--- Datos del Equipo ---", font=('Arial', 12, 'bold')).pack(pady=10)

tk.Label(ventana, text="Nombre del equipo:").pack()
entry_nombre_equipo = tk.Entry(ventana, width=40)
entry_nombre_equipo.pack()

tk.Label(ventana, text="Universidad:").pack()
entry_universidad = tk.Entry(ventana, width=40)
entry_universidad.pack()

tk.Label(ventana, text="Lenguaje de programación:").pack()
entry_lenguaje = tk.Entry(ventana, width=40)
entry_lenguaje.pack()

# Sección: Integrantes
tk.Label(ventana, text="--- Datos de los Programadores (mínimo 2) ---", font=('Arial', 12, 'bold')).pack(pady=10)

entries_nombres = []
entries_apellidos = []

for i in range(3):
    tk.Label(ventana, text=f"Integrante {i+1}").pack(pady=5)
    tk.Label(ventana, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana, width=40)
    entry_nombre.pack()
    entries_nombres.append(entry_nombre)

    tk.Label(ventana, text="Apellidos:").pack()
    entry_apellidos = tk.Entry(ventana, width=40)
    entry_apellidos.pack()
    entries_apellidos.append(entry_apellidos)

# Botón final
tk.Button(ventana, text="Registrar equipo", command=registrar_equipo, font=('Arial', 11)).pack(pady=20)

ventana.mainloop()