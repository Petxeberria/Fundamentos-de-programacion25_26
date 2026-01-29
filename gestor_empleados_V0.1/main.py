import os
import tkinter as tk
from tkinter import ttk
from pestana_empleado import init_empleado
from pestana_departamentos import init_departamentos
from pestana_informes import init_informes


# Obtenemos la ruta actual del archivo
ruta = os.getcwd()

def ventana_principal(root):
    root.title("Gestor de Empleados") # Titulo de la ventana
    root.geometry("1280x720") # Tamaño de la ventana
    root.resizable(0, 0) # Bloqueamos la escalabilidad de la ventana
    root.icono = tk.PhotoImage(file=f"{ruta}\\iconos\\pfizer.png") # Icono de la app


def crear_pestanas(root):
    style = ttk.Style(root) # Creamos un nuevo estilo
    style.configure("MiNotebook.TNotebook.Tab", font=("Arial", 14, "bold"))
    pestanas = ttk.Notebook(root, style="MiNotebook.TNotebook") # Creamos el contenedor de pestañas
    pestanas.pack(fill="both", expand="yes")
    # Creamos las pestañas
    pestana_inicio = ttk.Frame(pestanas)
    pestana_empleados = ttk.Frame(pestanas)
    pestana_departamentos = ttk.Frame(pestanas)
    pestana_informes = ttk.Frame(pestanas)
    # Añadimos las pestañas al contenedor
    pestanas.add(pestana_inicio, text=" Inicio ")
    pestanas.add(pestana_empleados, text=" Empleados ")
    pestanas.add(pestana_departamentos, text=" Departamentos ")
    pestanas.add(pestana_informes, text=" Informes")

    return pestanas

def init_inicio(pestanas):
    # Contenedor para Text + Scrollbar dentro de la pestaña
    contenedor = ttk.Frame(pestanas.nametowidget(pestanas.tabs()[0]))
    contenedor.pack(fill="both", expand=True)
    scroll_y = ttk.Scrollbar(contenedor, orient="vertical")
    scroll_y.pack(side="right", fill="y")

    text_widget = tk.Text(contenedor, wrap="word", yscrollcommand=scroll_y.set)
    text_widget.pack(side="left", fill="both", expand=True)

    scroll_y.config(command=text_widget.yview)

    # Insertar texto largo
    texto_largo = (
        "Bienvenido a la pestaña de inicio.\n\n"
        "Aquí puedes poner explicaciones, ayuda, instrucciones, etc.\n\n"
        + ("Esto es una línea de ejemplo para que haya mucho texto.\n" * 200)
    )

    text_widget.insert("1.0", texto_largo)
    # Si solo quieres mostrar (no editar):
    text_widget.config(state="disabled")



def main():
    root = tk.Tk()
    # Lanzamos la ventana principal de la aplicación
    ventana_principal(root)
    # Creamos las pestañas de la aplicación
    pestanas = crear_pestanas(root)
    # Añadimos contenido a la pestaña de inicio
    init_inicio(pestanas)
    # Añadimos contenido a la pestaña de empleados
    init_empleado(pestanas)
    # Añadimos contenido a la pestaña de departamentos
    init_departamentos(pestanas)
    # Añadimos contenido a la pestaña de informes
    init_informes(pestanas)

    root.mainloop()


if __name__ == "__main__":
    main()
