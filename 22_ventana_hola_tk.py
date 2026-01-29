import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("PRIMERA VENTANA CON TKINTER")

# Crear una etiqueta con la version de Tkinter
etiqueta = tk.Label(ventana, 
                    text=f"Versión de Tkinter: {tk.TkVersion}",
                    font=("Arial", 16),
                    fg="blue")
etiqueta.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()