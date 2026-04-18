import csv
import os
import random

# Función para cargar ejercicios desde el CSV
def cargar_ejercicios(archivo_csv):
    ejercicios = {}
    with open(archivo_csv, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar encabezado
        for row in reader:
            ejercicio, grupo, tiempo = row
            tiempo = int(tiempo)
            if grupo not in ejercicios:
                ejercicios[grupo] = []
            ejercicios[grupo].append((ejercicio, tiempo))
    return ejercicios

# Función para crear una nueva rutina
def crear_rutina(ejercicios, dias, tiempo):
    grupos = list(ejercicios.keys())
    random.shuffle(grupos)
    rutina = {}
    # Distribuir grupos en días usando round-robin
    for i in range(len(grupos)):
        dia = (i % dias) + 1
        if dia not in rutina:
            rutina[dia] = []
        rutina[dia].append(grupos[i])
    # Para cada día, seleccionar ejercicios y calcular tiempo
    rutina_completa = {}
    tiempos_dia = {}
    for dia, grupos_dia in rutina.items():
        rutina_completa[dia] = []
        tiempo_dia = 0
        for grupo in grupos_dia:
            # Seleccionar 1-2 ejercicios por grupo
            num_ej = random.randint(1, 2)
            seleccionados = random.sample(ejercicios[grupo], num_ej)
            rutina_completa[dia].extend(seleccionados)
            tiempo_dia += sum(tiempo for ej, tiempo in seleccionados)
        # Intentar llenar el tiempo agregando más ejercicios si es posible
        while tiempo_dia < tiempo:
            # Elegir un grupo aleatorio del día que tenga ejercicios disponibles no seleccionados
            grupos_disponibles = [g for g in grupos_dia if len([ej for ej, t in ejercicios[g] if (ej, t) not in rutina_completa[dia]]) > 0]
            if not grupos_disponibles:
                break  # No hay más ejercicios disponibles en los grupos de este día
            grupo = random.choice(grupos_disponibles)
            ejercicios_disponibles = [(ej, t) for ej, t in ejercicios[grupo] if (ej, t) not in rutina_completa[dia]]
            if ejercicios_disponibles:
                ej_seleccionado = random.choice(ejercicios_disponibles)
                rutina_completa[dia].append(ej_seleccionado)
                tiempo_dia += ej_seleccionado[1]
            else:
                break
        tiempos_dia[dia] = tiempo_dia
        # Si excede, reducir ejercicios (quitar el de mayor tiempo)
        while tiempo_dia > tiempo and len(rutina_completa[dia]) > len(grupos_dia):  # Mantener al menos uno por grupo
            # Encontrar el ejercicio con mayor tiempo
            max_tiempo = max(tiempo for ej, tiempo in rutina_completa[dia])
            for i, (ej, t) in enumerate(rutina_completa[dia]):
                if t == max_tiempo:
                    rutina_completa[dia].pop(i)
                    tiempo_dia -= t
                    break
        tiempos_dia[dia] = tiempo_dia
    return rutina_completa, tiempos_dia

# Función para guardar rutina
def guardar_rutina(rutina, tiempos, nombre):
    rutinas_dir = os.path.join(os.path.dirname(__file__), 'rutinas')
    if not os.path.exists(rutinas_dir):
        os.makedirs(rutinas_dir)
    with open(os.path.join(rutinas_dir, f'{nombre}.txt'), 'w', encoding='utf-8') as file:
        for dia, ej_list in rutina.items():
            tiempo_dia = tiempos[dia]
            file.write(f'Día {dia} (Tiempo estimado: {tiempo_dia} min):\n')
            for ej, t in ej_list:
                file.write(f'- {ej}\n')
            file.write('\n')

# Función para cargar rutina
def cargar_rutina():
    rutinas_dir = os.path.join(os.path.dirname(__file__), 'rutinas')
    if not os.path.exists(rutinas_dir):
        print("No hay rutinas guardadas.")
        return
    archivos = [f for f in os.listdir(rutinas_dir) if f.endswith('.txt')]
    if not archivos:
        print("No hay rutinas guardadas.")
        return
    print("Rutinas guardadas:")
    for i, arch in enumerate(archivos, 1):
        print(f"{i}. {arch[:-4]}")  # Sin .txt
    try:
        opcion = int(input("Elige el número de la rutina: "))
        if 1 <= opcion <= len(archivos):
            with open(os.path.join(rutinas_dir, archivos[opcion-1]), 'r', encoding='utf-8') as file:
                print(file.read())
        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada inválida.")

# Función principal del menú
def menu():
    archivo_csv = os.path.join(os.path.dirname(__file__), 'ejercicios.csv')
    ejercicios = cargar_ejercicios(archivo_csv)
    while True:
        print("\nMenú:")
        print("1. Crear nueva rutina")
        print("2. Cargar rutina guardada")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            try:
                dias = int(input("Cuántos días a la semana vas a entrenar (3-5): "))
                if not 3 <= dias <= 5:
                    print("Debe ser entre 3 y 5.")
                    continue
                tiempo = int(input("Cuánto tiempo por sesión en minutos (45-90): "))
                if not 45 <= tiempo <= 90:
                    print("Debe ser entre 45 y 90.")
                    continue
                rutina, tiempos = crear_rutina(ejercicios, dias, tiempo)
                print("Rutina generada:")
                for dia, ej_list in rutina.items():
                    tiempo_dia = tiempos[dia]
                    ejercicios_str = ', '.join(ej for ej, t in ej_list)
                    print(f"Día {dia}: {ejercicios_str} - Tiempo estimado: {tiempo_dia} min")
                    if tiempo_dia > tiempo:
                        print(f"  Advertencia: Excede el tiempo por sesión ({tiempo} min)")
                nombre = input("Nombre para guardar la rutina: ")
                guardar_rutina(rutina, tiempos, nombre)
                print("Rutina guardada.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == '2':
            cargar_rutina()
        elif opcion == '3':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()