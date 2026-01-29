import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo doble formulario")

#Frame izquierda
frame_izquierda = tk.Frame(root, padx=10, pady=10, borderwidth=2, relief="groove")
frame_izquierda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
#Frame derecha
frame_derecha = tk.Frame(root, padx=10, pady=10, borderwidth=2, relief="groove")
frame_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
# root.geometry("300x200")

# Crear inputs de texto y labels en un grid
label1 = tk.Label(frame_izquierda, text="Nombre:")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry1 = tk.Entry(frame_izquierda)
entry1.grid(row=0, column=1, padx=10, pady=10)
label2 = tk.Label(frame_izquierda, text="Apellido:")
label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry2 = tk.Entry(frame_izquierda)
entry2.grid(row=1, column=1, padx=10, pady=10)
label3 = tk.Label(frame_izquierda, text="Edad:")
label3.grid(row=2, column=0, padx=10, pady=10)
entry3 = tk.Entry(frame_izquierda)
entry3.grid(row=2, column=1, padx=10, pady=10)
# Botón para enviar los datos
submit_button = tk.Button(frame_izquierda, text="Enviar")
submit_button.grid(row=3, columnspan=2, pady=20)


label4 = tk.Label(frame_derecha, text="Usuario:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry4 =tk.Entry(frame_derecha).grid(row=0, column=1, padx=5, pady=5)

label5 = tk.Label(frame_derecha, text="Contraseña:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry5 = tk.Entry(frame_derecha, show="*").grid(row=1, column=1, padx=5, pady=5)
btn_login = tk.Button(frame_derecha, text="Entrar")
btn_login.grid(row=2, columnspan=2, pady=20)
# Iniciar el bucle principal de la aplicación
root.mainloop()
