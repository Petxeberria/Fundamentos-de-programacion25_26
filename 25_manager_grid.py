import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Layout GRID")
ventana.geometry("800x600")

# Crear 4 labels con diferentes colores de fondo
label1 = tk.Label(ventana, text="Label 1", font=("Arial", 24), bg="red", fg="white")
label1.grid(row=0, column=0)
label2 = tk.Label(ventana, text="Label 2", font=("Arial", 24), bg="green", fg="white")
label2.grid(row=0, column=1)
label3 = tk.Label(ventana, text="Label 3", font=("Arial", 24), bg="blue", fg="white")
label3.grid(row=1, column=0)
label4 = tk.Label(ventana, text="Label 4", font=("Arial", 24), bg="yellow", fg="black")
label4.grid(row=1, column=1)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()