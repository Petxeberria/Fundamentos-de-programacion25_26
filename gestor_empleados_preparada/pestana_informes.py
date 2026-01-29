import tkinter as tk
from tkinter import ttk, messagebox

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importamos la lista de empleados desde tu pestaña de empleados
# (asegúrate de que en pestana_empleado.py exista una lista global llamada empleados)
from pestana_empleado import empleados
from pestana_departamentos import departamentos


def _empleados_a_dataframe():
    """Convierte la lista de objetos Empleado a un DataFrame."""
    if not empleados:
        return pd.DataFrame(columns=["id", "nombre", "apellidos", "edad", "departamento"])

    data = []
    for e in empleados:
        data.append({
            "id": e.id,
            "nombre": e.nombre,
            "apellidos": e.apellidos,
            "edad": int(e.edad) if str(e.edad).isdigit() else 0,
            "departamento": e.departamento
        })
    return pd.DataFrame(data)


def informe_empleados_por_departamento():
    df = _empleados_a_dataframe()
    if df.empty:
        messagebox.showwarning("Sin datos", "No hay empleados cargados para generar el informe.")
        return

    conteo = df["departamento"].value_counts()

    plt.figure()
    wedges, texts, autotexts = plt.pie(
        conteo.values,
        labels=None,             # quitamos labels del propio gráfico
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Distribución de empleados por departamento")
    plt.axis("equal")

    # Leyenda aparte (queda limpio)
    plt.legend(
        wedges,
        conteo.index,
        title="Departamento",
        loc="center left",
        bbox_to_anchor=(1.0, 0.5)
    )

    plt.tight_layout()
    plt.show()



def informe_histograma_edades():
    df = _empleados_a_dataframe()
    if df.empty:
        messagebox.showwarning("Sin datos", "No hay empleados cargados para generar el informe.")
        return

    edades = df["edad"].astype(int)
    edades = edades[edades > 0]  # por si hay edades 0 por errores de entrada

    if edades.empty:
        messagebox.showwarning("Datos inválidos", "No hay edades válidas para generar el informe.")
        return

    plt.figure()
    plt.hist(edades, bins=10)  # no fijo colores (mejor práctica según tu entorno)
    plt.title("Distribución de edades")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

def informe_necesarios_vs_reales():
    if not departamentos:
        messagebox.showwarning("Sin datos", "No hay departamentos cargados.")
        return
    if not empleados:
        messagebox.showwarning("Sin datos", "No hay empleados cargados.")
        return

    # Reales por departamento (desde empleados)
    df_emp = pd.DataFrame([{
        "departamento": e.departamento
    } for e in empleados])

    reales = df_emp["departamento"].value_counts()

    # Necesarios por departamento (desde departamentos)
    df_dep = pd.DataFrame([{
        "departamento": d.nombre,
        "necesarios": d.empleados_necesarios
    } for d in departamentos])

    # Unimos en una tabla
    df = df_dep.copy()
    df["reales"] = df["departamento"].map(reales).fillna(0).astype(int)

    # Gráfico de barras comparativo
    x = range(len(df))
    plt.figure()
    plt.bar([i - 0.2 for i in x], df["necesarios"], width=0.4, label="Necesarios")
    plt.bar([i + 0.2 for i in x], df["reales"], width=0.4, label="Reales")

    plt.xticks(list(x), df["departamento"], rotation=30, ha="right")
    plt.title("Empleados necesarios vs empleados reales (por departamento)")
    plt.xlabel("Departamento")
    plt.ylabel("Cantidad")
    plt.legend()
    plt.tight_layout()
    plt.show()

def init_informes(pestanas):
    # pestaña 3 (índice 3): Informes
    contenedor = ttk.Frame(pestanas.nametowidget(pestanas.tabs()[3]))
    contenedor.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = ttk.Label(contenedor, text="Informes", font=("Arial", 18, "bold"))
    titulo.pack(anchor="w", pady=(0, 10))

    descripcion = ttk.Label(
        contenedor,
        text="Elige un informe y pulsa el botón para generar una gráfica (se abrirá en una ventana nueva).",
        font=("Arial", 11)
    )
    descripcion.pack(anchor="w", pady=(0, 20))

    # Selector de informes
    frame_selector = ttk.Frame(contenedor)
    frame_selector.pack(anchor="w", fill="x")

    ttk.Label(frame_selector, text="Selecciona informe:", font=("Arial", 12)).grid(row=0, column=0, padx=(0, 10))

    informes = [
        "Empleados por departamento (grafico circular)",
        "Distribución de edades (histograma)",
        "Necesarios vs reales por departamento (comparativo)",
    ]

    combo = ttk.Combobox(frame_selector, values=informes, state="readonly", width=45)
    combo.current(0)
    combo.grid(row=0, column=1, padx=(0, 10))

    def ejecutar_informe():
        seleccion = combo.get()
        if seleccion == informes[0]:
            informe_empleados_por_departamento()
        elif seleccion == informes[1]:
            informe_histograma_edades()
        elif seleccion == informes[2]:
            informe_necesarios_vs_reales()
        else:
            messagebox.showinfo("Info", "Selecciona un informe válido.")

    btn = ttk.Button(contenedor, text="Generar informe", command=ejecutar_informe)
    btn.pack(anchor="w", pady=20)
