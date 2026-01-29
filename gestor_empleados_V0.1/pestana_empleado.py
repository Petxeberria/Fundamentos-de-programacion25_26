import os
import random
import tkinter as tk
from tkinter import ttk

from Mi_repositorio.gestor_empleados_preparada.pestana_departamentos import update_treeview
from empleado import Empleado
import pandas as pd

#Leer datos de .csv
df = pd.read_csv('empleados.csv')


empleados = []
components = []





def generate_id(e_id):
    e_id.delete(0, tk.END)
    e_id.insert(0, str(random.randint(1000, 9999)))

def update_treeview(tree):
    # Limpiamos el treeview
    for item in tree.get_children():
        tree.delete(item)
    # Añadimos todos los empleados al treeview
    for emp in empleados:
        tree.insert("", "end", values=(emp.id, emp.nombre, emp.apellidos, emp.edad,emp.correo, emp.departamento))


def add_empleado(tree, e_id, e_nombre, e_apellido, e_edad, e_correo, c_departamento):
    o_empleado = Empleado(
        id=e_id.get(),
        nombre=e_nombre.get(),
        apellidos=e_apellido.get(),
        edad=int(e_edad.get()) if e_edad.get().isdigit() else 0,
        correo=e_correo.get(),
        departamento=c_departamento.get()
    )


    # Comprobamos si el empleado es válido antes de añadirlo en la lista
    # de empleados y actualizamos el treeview
    if o_empleado.es_valido():
        empleados.append(o_empleado)
        update_treeview(tree)
    else:
        print("Por favor, complete todos los campos correctamente.")
        return


def delete_empleado(tree):
    selected = tree.selection()
    if not selected:
        print("Selecciona una fila primero.")
        return

    iid = selected[0]
    values = tree.item(iid, "values")
    emp_id = values[0]  # primera columna (id)

    # borrar de la lista empleados
    global empleados
    empleados = [emp for emp in empleados if str(emp.id) != str(emp_id)]

    # refrescar tree
    update_treeview(tree)


    # id_emp = e_id.get()
    # nombre = e_nombre.get()
    #apellido = e_apellido.get()
    #edad = e_edad.get()
    #departamento = c_departamento.get()

    #if o_empleado.es_valido():
    #    tree.insert("", "end", values=(o_empleado.id, o_empleado.nombre, o_empleado.apellidos, o_empleado.edad, o_empleado.departamento))
    #    e_id.delete(0, tk.END)
    #    e_nombre.delete(0, tk.END)
    #    e_apellido.delete(0, tk.END)
    #    e_edad.delete(0, tk.END)
    #    c_departamento.current(0)
    #else:
    #    print("Por favor, complete todos los campos.")

# Bind treeview select
def on_tree_select(event):
    selected_item = components[0].selection()
    if selected_item:
        item = components[0].item(selected_item)
        emp_id, nombre, apellidos, edad,correo, departamento = item['values']
        components[1].delete(0, tk.END)
        components[1].insert(0, emp_id)
        components[2].delete(0, tk.END)
        components[2].insert(0, nombre)
        components[3].delete(0, tk.END)
        components[3].insert(0, apellidos)
        components[4].delete(0, tk.END)
        components[4].insert(0, edad)
        components[5].delete(0, tk.END)
        components[5].insert(0, correo)
        components[6].set(departamento)

# Actualizar un empleado de la lista a partir de los campos de entrada
def update_empleado_from_fields():
    #buscar el empleado en la lista por id
    e_id = components[1].get()
    for emp in empleados:
        if emp.id == e_id:
            emp.nombre = components[2].get()
            emp.apellidos = components[3].get()
            emp.edad = int(components[4].get()) if components[4].get().isdigit() else 0
            emp.correo = components[5].get()
            emp.departamento = components[6].get()
            break

    update_treeview(components[0])

def init_empleado(pestanas):

    style = ttk.Style()
    style.configure("Tall.TEntry", padding=(6, 8, 6, 8))  # left, top, right, bottom
    style.configure("Tall.TCombobox", padding=(6, 8, 6, 8))
    style.configure("Tall.TButton", padding=(6, 8, 6, 8))
            
    # Contenedor para Text + Scrollbar dentro de la pestaña
    contenedor = ttk.Frame(pestanas.nametowidget(pestanas.tabs()[1]))
    contenedor.pack(fill="both", expand=True)

    #Frame izquierda
    frame_izquierda = tk.Frame(contenedor, padx=10, pady=10, borderwidth=2, relief="groove")
    frame_izquierda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    #Frame derecha
    frame_derecha = tk.Frame(contenedor, padx=10, pady=10, borderwidth=2, relief="groove")
    frame_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # treeview para mostrar la lista de empleados
    columnas = ("ID", "Nombre", "Apellidos", "Edad","Correo", "Departamento")
    tree = ttk.Treeview(frame_derecha, columns=columnas, show="headings")
    components.append(tree)
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)
    tree.pack(fill=tk.BOTH, expand=True)
    for _, fila in df.iterrows():
        empleado = Empleado(
            id=int(fila['id']),
            nombre=fila['nombre'],
            apellidos=fila['apellidos'],
            edad=int(fila['edad']),
            correo=fila['correo'],
            departamento=fila['departamento']
        )
        empleados.append(empleado)
        update_treeview(tree)

    # Nueva etiqueta para la pestaña de Empleados
    # Campo entrada para la id del empleado
    l_id = ttk.Label(frame_izquierda, text="Id: ", justify=tk.LEFT)
    l_id.grid(row=0, column=0, padx=10, pady=10)
    e_id = ttk.Entry(frame_izquierda, width=30, style="Tall.TEntry")
    components.append(e_id)
    e_id.grid(row=0, column=1, padx=10, pady=10)
    b_id = ttk.Button(frame_izquierda, text="Generar Id", command=lambda: generate_id(e_id), style="Tall.TButton")
    b_id.grid(row=0, column=2, padx=10, pady=10)
    # Campo entrada para el nombre del empleado
    l_nombre = ttk.Label(frame_izquierda, text="Nombre: ", justify=tk.LEFT)
    l_nombre.grid(row=1, column=0, padx=10, pady=10)
    e_nombre = ttk.Entry(frame_izquierda, width=30, style="Tall.TEntry")
    components.append(e_nombre)
    e_nombre.grid(row=1, column=1, padx=10, pady=10)
    # Campo entrada para el apellido del empleado
    l_apellido = ttk.Label(frame_izquierda, text="Apellidos: ", justify=tk.LEFT)
    l_apellido.grid(row=2, column=0, padx=10, pady=10)
    e_apellido = ttk.Entry(frame_izquierda, width=30, style="Tall.TEntry")
    components.append(e_apellido)
    e_apellido.grid(row=2, column=1, padx=10, pady=10)
    # Campo entrada para la edad del empleado
    l_edad = ttk.Label(frame_izquierda, text="Edad: ", justify=tk.LEFT)
    l_edad.grid(row=3, column=0, padx=10, pady=10)
    e_edad = ttk.Entry(frame_izquierda, width=30, style="Tall.TEntry")
    components.append(e_edad)
    e_edad.grid(row=3, column=1, padx=10, pady=10)
    # Campo entrada para el correo del empleado
    l_correo = ttk.Label(frame_izquierda, text="Correo: ", justify=tk.LEFT)
    l_correo.grid(row=4, column=0, padx=10, pady=10)
    e_correo = ttk.Entry(frame_izquierda, width=30, style="Tall.TEntry")
    components.append(e_correo)
    e_correo.grid(row=4, column=1, padx=10, pady=10)
    # Campo entrada para el departamento del empleado
    l_departamento = ttk.Label(frame_izquierda, text="Departamento: ", justify=tk.LEFT)
    l_departamento.grid(row=5, column=0, padx=10, pady=10)
    c_departamento = ttk.Combobox(frame_izquierda, values=
                                  ["Recursos Humanos", "Desarrollo", "Ventas", "Marketing", "IT","Operaciones","Finanzas"],
                                  width=28, style="Tall.TCombobox")
    components.append(c_departamento)
    c_departamento.grid(row=5, column=1, padx=10, pady=10)
    c_departamento.current(0)  # Selecciona el primer departamento por defecto

    # Boton Guardar empleado
    b_guardar = ttk.Button(frame_izquierda, text="Guardar Empleado" , 
                           command=lambda: add_empleado(tree, e_id, e_nombre, e_apellido, e_edad,e_correo, c_departamento),
                           style="Tall.TButton")
    b_guardar.grid(row=6, column=0, padx=10, pady=20)
    # Boton Actualizar empleado
    b_actualizar = ttk.Button(frame_izquierda, text="Actualizar Empleado" , 
                           command=update_empleado_from_fields,
                           style="Tall.TButton")
    b_actualizar.grid(row=6, column=1, padx=10, pady=20)
    # Boton Eliminar empleado
    b_eliminar = ttk.Button(frame_izquierda, text="Eliminar Empleado",
                              command=lambda: delete_empleado(tree),
                              style="Tall.TButton")
    b_eliminar.grid(row=6, column=2, padx=10, pady=20)

    # Bind para seleccionar un empleado y cargar sus datos en los campos de entrada
    tree.bind("<<TreeviewSelect>>", on_tree_select) 
