import tkinter as tk
from tkinter import messagebox

def ejecutar_prueba_excepciones():
    resultado = ""
    
    try:
        resultado += "Ingresando al primer try\n"
        cociente = 10000 / 0
        resultado += "Después de la división\n"
    except ZeroDivisionError:
        resultado += "División por cero\n"
    finally:
        resultado += "Ingresando al primer finally\n"

    try:
        resultado += "Ingresando al segundo try\n"
        objeto = None
        objeto.toString()
        resultado += "Imprimiendo objeto\n"
    except ArithmeticError:
        resultado += "División por cero\n"
    except Exception:
        resultado += "Ocurrió una excepción\n"
    finally:
        resultado += "Ingresando al segundo finally\n"

    messagebox.showinfo("Resultado", resultado)

# Crear ventana
ventana = tk.Tk()
ventana.title("Ejercicio 6.4 - Manejo de Excepciones")
ventana.geometry("400x200")

btn_ejecutar = tk.Button(ventana, text="Ejecutar Prueba de Excepciones", command=ejecutar_prueba_excepciones)
btn_ejecutar.pack(pady=50)

ventana.mainloop()