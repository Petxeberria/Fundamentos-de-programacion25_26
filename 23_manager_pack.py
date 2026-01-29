import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("EJEMPLO PACK MANAGER")
ventana.geometry("800x600")

# Etiquetas para distribuir
etiqueta_arribar = tk.Label(ventana, text="Etiqueta Arriba", font=("Arial", 32), bg="lightblue")
etiqueta_arribar.pack(side=tk.TOP, fill=tk.X)

etiqueta_abajo = tk.Label(ventana, text="Etiqueta Abajo", font=("Arial", 32), bg="lightgreen")
etiqueta_abajo.pack(side=tk.BOTTOM, fill=tk.X)


etiqueta_izquierda = tk.Label(ventana, text="Izquierda", font=("Arial", 16), bg="lightyellow")
etiqueta_izquierda.pack(side=tk.LEFT, fill=tk.Y)

etiqueta_derecha = tk.Label(ventana, text="Derecha", font=("Arial", 16), bg="lightcoral")
etiqueta_derecha.pack(side=tk.RIGHT, fill=tk.Y)

etiqueta_centro = tk.Label(ventana, text="Centro", font=("Arial", 16), bg="lightgray")
etiqueta_centro.pack(expand=True, fill=tk.BOTH)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()