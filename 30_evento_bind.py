import tkinter as tk
from tkinter import ttk

def click_label(event):
    print("Has hecho clic en la etiqueta")
    print("Coordenadas dentro del widget:", event.x, event.y)

# Crear la ventana principal
root = tk.Tk()

# Crear una etiqueta y vincular el evento de clic
label = ttk.Label(root, text="Haz clic aquí")
label.pack(padx=20, pady=20)

# Agregar el evento de clic a la etiqueta
label.bind("<Button-1>", click_label)  # Botón izquierdo

root.mainloop()
