# modules/interfaz.py

import tkinter as tk
from tkinter import messagebox

def preguntar_instalacion(programas):
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    for programa in programas:
        respuesta = messagebox.askyesno("Instalar Programa", f"¿Desea instalar {programa}?")
        if respuesta:
            return programa

    root.destroy()
    return None
