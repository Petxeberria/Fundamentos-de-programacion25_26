import tkinter as tk

def saludar():
    print("¡Hola!")

# Crear la ventana principal
root = tk.Tk()
root.geometry("200x100")
# Crear un botón y asignarle la función saludar al hacer clic
btn = tk.Button(root, text="Saludar", command=saludar)
btn.pack()

root.mainloop()
