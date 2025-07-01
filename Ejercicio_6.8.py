import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def leer_archivo():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]
    )

    if not ruta_archivo:
        return  

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            text_area.delete(1.0, tk.END)  
            text_area.insert(tk.END, contenido)
    except IOError:
        messagebox.showerror("Error", "No se pudo leer el archivo.")

ventana = tk.Tk()
ventana.title("Leer Archivo de Texto")
ventana.geometry("600x400")

btn_abrir = tk.Button(ventana, text="Abrir archivo .txt", command=leer_archivo)
btn_abrir.pack(pady=10)

text_area = scrolledtext.ScrolledText(ventana, width=70, height=20, wrap=tk.WORD)
text_area.pack(padx=10, pady=10)

ventana.mainloop()