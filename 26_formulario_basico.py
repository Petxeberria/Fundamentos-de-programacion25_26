import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("REGISTRO DE USUARIOS")
ventana.geometry("300x400")

# Crear el formulario
l_nombre = tk.Label(ventana, text="Nombre:")
l_nombre.grid(row=0, column=0, padx=10, pady=10)
e_nombre = tk.Entry(ventana)
e_nombre.grid(row=0, column=1, padx=10, pady=10)

l_apellido = tk.Label(ventana, text="Apellido:")
l_apellido.grid(row=1, column=0, padx=10, pady=10)
e_apellido = tk.Entry(ventana)
e_apellido.grid(row=1, column=1, padx=10, pady=10)

l_edad = tk.Label(ventana, text="Edad:")
l_edad.grid(row=2, column=0, padx=10, pady=10)
e_edad = tk.Entry(ventana)
e_edad.grid(row=2, column=1, padx=10, pady=10)

# Boton de envío
b_submit = tk.Button(ventana, text="Enviar")
b_submit.grid(row=3, columnspan=2, pady=20)

# Inicio de ventana de formulario
ventana.mainloop()