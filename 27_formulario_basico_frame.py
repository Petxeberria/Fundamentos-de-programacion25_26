import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("REGISTRO DE USUARIOS CON FRAME")
ventana.geometry("300x400")

# Crear un frame para el formulario
frame_formulario = tk.Frame(ventana, padx=10, pady=10)
frame_formulario.pack(pady=20)

# Crear el formulario
l_nombre = tk.Label(frame_formulario, text="Nombre:")
l_nombre.grid(row=0, column=0, padx=10, pady=10)
e_nombre = tk.Entry(frame_formulario)
e_nombre.grid(row=0, column=1, padx=10, pady=10)

l_apellido = tk.Label(frame_formulario, text="Apellido:")
l_apellido.grid(row=1, column=0, padx=10, pady=10)
e_apellido = tk.Entry(frame_formulario)
e_apellido.grid(row=1, column=1, padx=10, pady=10)

l_edad = tk.Label(frame_formulario, text="Edad:")
l_edad.grid(row=2, column=0, padx=10, pady=10)
e_edad = tk.Entry(frame_formulario)
e_edad.grid(row=2, column=1, padx=10, pady=10)

# Boton de envío
b_submit = tk.Button(ventana, text="Enviar")
#_submit.grid(row=3, columnspan=2, pady=20)
b_submit.pack(pady=20)

# Inicio de ventana de formulario
ventana.mainloop()