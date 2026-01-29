import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Manager Place")
ventana.geometry("800x600")

# Crear un boton y posicionarlo usando place
boton = tk.Button(ventana, text="Botón Posicionado", font=("Arial", 24))
boton.place(x=200, y=150)


# Inicializamos el main loop
ventana.mainloop()