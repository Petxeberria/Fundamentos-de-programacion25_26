import os
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import pandas as pd

from departamento import Departamento

# Lista global de objetos Departamento (se rellena desde CSV y/o desde la UI)
departamentos = []


# ==========================================================
# 1) CONFIGURACIÓN: lista fija de departamentos (ComboBox)
# ==========================================================
DEPARTAMENTOS_DISPONIBLES = [
    "Recursos Humanos",
    "Desarrollo",
    "Ventas",
    "Marketing",
    "IT",
    "Operaciones",
    "Finanzas",
]


# ==========================================================
# 2) CARGA INICIAL DESDE CSV
# ==========================================================
def cargar_departamentos_desde_csv(csv_filename="departamentos.csv"):
    """
    Carga datos iniciales desde un CSV y los mete en la lista global 'departamentos'.

    Espera columnas EXACTAS (en minúsculas o mayúsculas, da igual):
      id, nombre, empleados_necesarios, presupuesto, horas_disponibles
    """
    global departamentos

    # Ruta absoluta al CSV (mismo directorio que este .py)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, csv_filename)

    # Si no existe el CSV, avisamos al usuario
    if not os.path.exists(csv_path):
        messagebox.showwarning(
            "CSV no encontrado",
            f"No se encontró el archivo {csv_filename} en:\n{base_dir}\n\n"
            "Crea el CSV con el contenido que te he pasado."
        )
        return

    # Intentamos leer el CSV con pandas
    try:
        df = pd.read_csv(csv_path)
        # Normalizamos nombres de columnas: quitamos espacios, pasamos a minúsculas
        df.columns = df.columns.str.strip().str.lower()
    except Exception as e:
        messagebox.showerror("Error leyendo CSV", f"No se pudo leer el CSV:\n{e}")
        return

    # Comprobamos que el CSV tenga las columnas obligatorias
    required = {"id", "nombre", "empleados_necesarios", "presupuesto", "horas_disponibles"}
    if not required.issubset(set(df.columns)):
        messagebox.showerror(
            "CSV inválido",
            "El CSV no tiene las columnas necesarias.\n"
            "Debe tener: id,nombre,empleados_necesarios,presupuesto,horas_disponibles"
        )
        return

    # Vaciamos la lista y cargamos de nuevo
    departamentos.clear()

    for _, fila in df.iterrows():
        # Creamos un objeto Departamento con datos del CSV
        dep = Departamento(
            id=int(fila["id"]),
            nombre=str(fila["nombre"]),
            empleados_necesarios=int(fila["empleados_necesarios"]),
            presupuesto=float(fila["presupuesto"]),
            horas_disponibles=float(fila["horas_disponibles"])
        )
        departamentos.append(dep)


# ==========================================================
# 3) UTILIDADES: generar ID y convertir texto a número
# ==========================================================
def generate_id(e_id):
    """Genera un ID aleatorio de 4 dígitos y lo escribe en el Entry de ID."""
    e_id.delete(0, tk.END)
    e_id.insert(0, str(random.randint(1000, 9999)))


def _to_int(s, default=0):
    """Convierte un string a int si es numérico; si no, devuelve default."""
    s = str(s).strip()
    return int(s) if s.isdigit() else default


def _to_float(s, default=0.0):
    """Convierte un string a float (acepta coma o punto); si falla, default."""
    s = str(s).strip().replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return default


# ==========================================================
# 4) TREEVIEW: refrescar la tabla con la lista 'departamentos'
# ==========================================================
def update_treeview(tree):
    """Limpia y vuelve a cargar el Treeview con los departamentos actuales."""
    # 1) borrar filas actuales
    for item in tree.get_children():
        tree.delete(item)

    # 2) insertar filas desde la lista
    for d in departamentos:
        tree.insert(
            "",
            "end",
            values=(d.id, d.nombre, d.empleados_necesarios, d.presupuesto, d.horas_disponibles)
        )


# ==========================================================
# 5) CRUD: añadir, eliminar, seleccionar, actualizar
# ==========================================================
def add_departamento(tree, w):
    """
    Crea un Departamento a partir de los campos de la UI y lo añade a la lista.
    w es un diccionario con los widgets (Entry/Combobox).
    """
    o_dep = Departamento(
        id=_to_int(w["e_id"].get(), 0),
        # 👇 AHORA el nombre se elige en el combobox (no es Entry)
        nombre=w["c_departamento"].get(),
        empleados_necesarios=_to_int(w["e_necesarios"].get(), 0),
        presupuesto=_to_float(w["e_presupuesto"].get(), 0.0),
        horas_disponibles=_to_float(w["e_horas"].get(), 0.0)
    )

    # Validamos el objeto antes de guardar
    if not o_dep.es_valido():
        messagebox.showwarning("Datos inválidos", "Por favor, complete todos los campos correctamente.")
        return

    # Evitamos IDs duplicados
    if any(str(d.id) == str(o_dep.id) for d in departamentos):
        messagebox.showwarning("ID duplicado", "Ese ID ya existe. Genera otro o usa uno distinto.")
        return

    # Añadimos y refrescamos la tabla
    departamentos.append(o_dep)
    update_treeview(tree)


def delete_departamento(tree):
    """Elimina el departamento seleccionado en el Treeview y actualiza la tabla."""
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("Selecciona", "Selecciona una fila primero.")
        return

    # Obtenemos el item seleccionado y su ID (primera columna)
    iid = selected[0]
    values = tree.item(iid, "values")
    dep_id = values[0]

    # Borramos de la lista global
    global departamentos
    departamentos = [d for d in departamentos if str(d.id) != str(dep_id)]

    # Refrescamos tabla
    update_treeview(tree)


def on_tree_select(event, tree, w):
    """
    Cuando seleccionas una fila del Treeview, carga sus valores en los campos de la izquierda.
    """
    selected = tree.selection()
    if not selected:
        return

    iid = selected[0]
    values = tree.item(iid, "values")

    dep_id, nombre, necesarios, presupuesto, horas = values

    # Cargar ID en Entry
    w["e_id"].delete(0, tk.END)
    w["e_id"].insert(0, dep_id)

    # Cargar departamento en Combobox (si existe en la lista)
    if nombre in w["c_departamento"]["values"]:
        w["c_departamento"].set(nombre)
    else:
        w["c_departamento"].current(0)

    # Cargar empleados necesarios
    w["e_necesarios"].delete(0, tk.END)
    w["e_necesarios"].insert(0, necesarios)

    # Cargar presupuesto
    w["e_presupuesto"].delete(0, tk.END)
    w["e_presupuesto"].insert(0, presupuesto)

    # Cargar horas disponibles
    w["e_horas"].delete(0, tk.END)
    w["e_horas"].insert(0, horas)

    # Guardamos el ID seleccionado (para actualizar correctamente)
    w["selected_id"] = str(dep_id)


def update_departamento_from_fields(tree, w):
    """
    Actualiza el departamento seleccionado usando los campos de la izquierda.
    """
    selected_id = w.get("selected_id")
    if not selected_id:
        messagebox.showinfo("Selecciona", "Selecciona un departamento en la tabla antes de actualizar.")
        return

    # Leemos los nuevos valores desde los widgets
    new_id = _to_int(w["e_id"].get(), 0)
    # 👇 el nombre sale del combobox
    new_nombre = w["c_departamento"].get()
    new_necesarios = _to_int(w["e_necesarios"].get(), 0)
    new_presupuesto = _to_float(w["e_presupuesto"].get(), 0.0)
    new_horas = _to_float(w["e_horas"].get(), 0.0)

    # Validación de datos
    temp = Departamento(new_id, new_nombre, new_necesarios, new_presupuesto, new_horas)
    if not temp.es_valido():
        messagebox.showwarning("Datos inválidos", "Revisa los campos.")
        return

    # Si cambias el ID, aseguramos que no exista ya
    if str(new_id) != str(selected_id) and any(str(d.id) == str(new_id) for d in departamentos):
        messagebox.showwarning("ID duplicado", "No puedes actualizar: ese nuevo ID ya existe.")
        return

    # Actualizamos el objeto en la lista global
    for d in departamentos:
        if str(d.id) == str(selected_id):
            d.id = new_id
            d.nombre = new_nombre
            d.empleados_necesarios = new_necesarios
            d.presupuesto = new_presupuesto
            d.horas_disponibles = new_horas
            break

    # Actualizamos el ID seleccionado y refrescamos tabla
    w["selected_id"] = str(new_id)
    update_treeview(tree)


# ==========================================================
# 6) FUNCIÓN PRINCIPAL DE LA PESTAÑA "DEPARTAMENTOS"
# ==========================================================
def init_departamentos(pestanas):
    """
    Inicializa la pestaña de Departamentos (pestanas.tabs()[2]):
      - Carga datos desde CSV (si la lista está vacía)
      - Crea UI (izquierda: formulario / derecha: tabla)
      - Conecta botones y eventos
    """

    # Cargar datos iniciales del CSV solo si aún no hay departamentos
    if not departamentos:
        cargar_departamentos_desde_csv("departamentos.csv")

    # Estilos (Entry y Button)
    style = ttk.Style()
    style.configure("Tall.TEntry", padding=(6, 8, 6, 8))
    style.configure("Tall.TButton", padding=(6, 8, 6, 8))
    # 👇 añadimos estilo para el combobox grande
    style.configure("Tall.TCombobox", padding=(6, 8, 6, 8))

    # Contenedor de la pestaña 2 (Departamentos)
    contenedor = ttk.Frame(pestanas.nametowidget(pestanas.tabs()[2]))
    contenedor.pack(fill="both", expand=True)

    # Frame izquierda (formulario)
    frame_izquierda = tk.Frame(contenedor, padx=10, pady=10, borderwidth=2, relief="groove")
    frame_izquierda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Frame derecha (tabla)
    frame_derecha = tk.Frame(contenedor, padx=10, pady=10, borderwidth=2, relief="groove")
    frame_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # --------------------------
    # TREEVIEW (tabla derecha)
    # --------------------------
    columnas = ("ID", "Nombre", "Empleados necesarios", "Presupuesto", "Horas disponibles")
    tree = ttk.Treeview(frame_derecha, columns=columnas, show="headings")

    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=170, anchor=tk.CENTER)

    tree.pack(fill=tk.BOTH, expand=True)

    # Diccionario donde guardamos widgets del formulario
    w = {"selected_id": None}

    # --------------------------
    # FORMULARIO (izquierda)
    # --------------------------
    # ID
    ttk.Label(frame_izquierda, text="ID:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    w["e_id"] = ttk.Entry(frame_izquierda, width=30, style="Tall.TEntry")
    w["e_id"].grid(row=0, column=1, padx=10, pady=10)

    ttk.Button(
        frame_izquierda,
        text="Generar ID",
        command=lambda: generate_id(w["e_id"]),
        style="Tall.TButton"
    ).grid(row=0, column=2, padx=10, pady=10)

    # NOMBRE (cambiado a Combobox de departamentos)
    ttk.Label(frame_izquierda, text="Departamento:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    w["c_departamento"] = ttk.Combobox(
        frame_izquierda,
        values=DEPARTAMENTOS_DISPONIBLES,
        width=28,
        state="readonly",
        style="Tall.TCombobox"
    )
    w["c_departamento"].grid(row=1, column=1, padx=10, pady=10)
    w["c_departamento"].current(0)

    # Empleados necesarios
    ttk.Label(frame_izquierda, text="Empleados necesarios:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    w["e_necesarios"] = ttk.Entry(frame_izquierda, width=30, style="Tall.TEntry")
    w["e_necesarios"].grid(row=2, column=1, padx=10, pady=10)

    # Presupuesto
    ttk.Label(frame_izquierda, text="Presupuesto (€):").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    w["e_presupuesto"] = ttk.Entry(frame_izquierda, width=30, style="Tall.TEntry")
    w["e_presupuesto"].grid(row=3, column=1, padx=10, pady=10)

    # Horas disponibles
    ttk.Label(frame_izquierda, text="Horas disponibles:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
    w["e_horas"] = ttk.Entry(frame_izquierda, width=30, style="Tall.TEntry")
    w["e_horas"].grid(row=4, column=1, padx=10, pady=10)

    # --------------------------
    # BOTONES (CRUD)
    # --------------------------
    ttk.Button(
        frame_izquierda,
        text="Guardar Departamento",
        command=lambda: add_departamento(tree, w),
        style="Tall.TButton"
    ).grid(row=5, column=0, padx=10, pady=20)

    ttk.Button(
        frame_izquierda,
        text="Actualizar Departamento",
        command=lambda: update_departamento_from_fields(tree, w),
        style="Tall.TButton"
    ).grid(row=5, column=1, padx=10, pady=20)

    ttk.Button(
        frame_izquierda,
        text="Eliminar Departamento",
        command=lambda: delete_departamento(tree),
        style="Tall.TButton"
    ).grid(row=5, column=2, padx=10, pady=20)

    # Evento: al seleccionar una fila de la tabla, se cargan los datos en el formulario
    tree.bind("<<TreeviewSelect>>", lambda e: on_tree_select(e, tree, w))

    # Cargamos los datos en la tabla al abrir la pestaña
    update_treeview(tree)


