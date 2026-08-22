"""
SISTEMA DE GESTION ACADEMICA - DISEÑO TOP-DOWN (REFINAMIENTO PROGRESIVO)
=========================================================================
NIVEL 0: función main()
-> Llama a los 3 grandes bloques del NIVEL 1
NIVEL 1: registrar_alumnos / procesar_notas / mostrar_listado_final
NIVEL 2: cada bloque del Nivel 1 se refina en funciones más pequeñas
y específicas (las mismas ramas "->" y "L" del diseño original)
=========================================================================
"""


# =========================================================================
# NIVEL 1 -> "Registro de alumnos"
# =========================================================================
def registrar_alumnos(n):
    nombres = []
    areas = []
    carreras = []
    notas = []

    for i in range(n):
        print(f"\n--- Registrando al estudiante N°{i + 1} ---")
        # NIVEL 2 -> "Información base: Nombre, área y carrera"
        nombre, area, carrera = registrar_informacion_base()
        nombres.append(nombre)
        areas.append(area)
        carreras.append(carrera)

    asignaturas = registrar_asignaturas()

    for i in range(n):
        print(f"\n--- Registrando notas del estudiante: {nombres[i]} ---")
        notas_alumno = registrar_notas(asignaturas)
        notas.append(notas_alumno)

    return nombres, areas, carreras, asignaturas, notas


# NIVEL 2 (refinamiento de registrar_alumnos)
def registrar_informacion_base():
    nombre = input("Nombre del estudiante: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del estudiante: ").strip()

    areas_disponibles = {
        1: "Ciencias y Tecnología",
        2: "Salud",
        3: "Humanidades",
    }
    print("Área (1-Ciencias y Tecnología, 2-Salud, 3-Humanidades):")
    while True:
        try:
            opcion = int(input("Opción: "))
            if opcion in areas_disponibles:
                break
            print("Seleccione una opción entre 1 y 3.")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
    area = areas_disponibles.get(opcion, "No definida")

    carrera = input("Carrera: ").strip()
    while not carrera:
        print("La carrera no puede estar vacía.")
        carrera = input("Carrera: ").strip()

    return nombre, area, carrera


# NIVEL 2 (refinamiento de registrar_alumnos)
def registrar_notas(asignaturas):
    notas_alumno = []
    for asignatura in asignaturas:
        while True:
            try:
                nota = float(input(f"Nota de {asignatura} (rango 0 - 100): "))
                if 0 <= nota <= 100:
                    break
                print("Valor fuera de rango. Debe ingresar una nota entre 0 y 100.")
            except ValueError:
                print("Ingrese una nota numérica válida.")
        notas_alumno.append(nota)
    return notas_alumno


def registrar_asignaturas():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de asignaturas a evaluar por estudiante (rango 5 - 7): "))
            if 5 <= cantidad <= 7:
                break
            print("Debe ingresar entre 5 y 7 asignaturas.")
        except ValueError:
            print("Ingrese una cantidad numérica válida.")

    asignaturas = []
    for i in range(cantidad):
        nombre = input(f"Nombre de la asignatura {i + 1}: ").strip()
        while not nombre:
            print("El nombre de la asignatura no puede estar vacío.")
            nombre = input(f"Nombre de la asignatura {i + 1}: ").strip()
        asignaturas.append(nombre)
    return asignaturas


# =========================================================================
# NIVEL 1 -> "Cálculos y procesamiento de notas"
# =========================================================================
def procesar_notas(notas):
    # NIVEL 2 -> "Cálculo de promedio individual (por alumno)"
    promedios_individuales = calcular_promedios_individuales(notas)

    # NIVEL 2 -> "Cálculo de promedio por grupo"
    promedio_grupal = calcular_promedio_grupal(promedios_individuales)

    # NIVEL 2 -> "Identificación de notas máximas y mínimas del grupo"
    nota_max, nota_min = identificar_notas_extremas(notas)

    # NIVEL 2 -> "Identificador de promedio más alto del grupo"
    indice_mejor = identificar_mejor_promedio(promedios_individuales)

    return promedios_individuales, promedio_grupal, nota_max, nota_min, indice_mejor


# NIVEL 2 (refinamiento de procesar_notas)
def calcular_promedios_individuales(notas):
    promedios = []
    for notas_alumno in notas:
        promedio = sum(notas_alumno) / len(notas_alumno)
        promedios.append(promedio)
    return promedios


# NIVEL 2 (refinamiento de procesar_notas)
def calcular_promedio_grupal(promedios_individuales):
    return sum(promedios_individuales) / len(promedios_individuales)


# NIVEL 2 (refinamiento de procesar_notas) - "recorre cada estudiante"
def identificar_notas_extremas(notas):
    nota_max = notas[0][0]
    nota_min = notas[0][0]
    for notas_alumno in notas:
        for nota in notas_alumno:
            if nota > nota_max:
                nota_max = nota
            if nota < nota_min:
                nota_min = nota
    return nota_max, nota_min


# NIVEL 2 (refinamiento de procesar_notas)
def identificar_mejor_promedio(promedios_individuales):
    mejor = 0
    for i in range(1, len(promedios_individuales)):
        if promedios_individuales[i] > promedios_individuales[mejor]:
            mejor = i
    return mejor


# =========================================================================
# NIVEL 1 -> "Listado final"
# =========================================================================
def mostrar_listado_final(nombres, areas, carreras, asignaturas, notas, promedios_individuales, promedio_grupal, nota_max, nota_min, indice_mejor):
    print("\n==================== LISTADO FINAL ====================")

    # NIVEL 2 -> "Mostrar lista de alumnos con su información base y sus notas"
    # NIVEL 2 -> "Promedio individual al final de su fila"
    for i in range(len(nombres)):
        print(f"Estudiante: {nombres[i]} | Área: {areas[i]} | Carrera: {carreras[i]}")
        for asignatura, nota in zip(asignaturas, notas[i]):
            print(f"   {asignatura}: {nota}")
        print(f"   >> Promedio individual: {promedios_individuales[i]:.2f}")

        # NIVEL 2 -> "Resaltar promedio más alto"
        if i == indice_mejor:
            print("   *** MEJOR PROMEDIO DEL GRUPO ***")
        print("---------------------------------------------------------")

    # NIVEL 2 -> "Promedio grupal al final de columna" + "Resaltar máximo y mínimo"
    print(f"\nPromedio general del grupo: {promedio_grupal:.2f}")
    print(f"Nota MÁXIMA del grupo: {nota_max}")
    print(f"Nota MÍNIMA del grupo: {nota_min}")
    print(f"Estudiante con mejor promedio: {nombres[indice_mejor]}")


# =========================================================================
# NIVEL 0: Módulo/función principal
# =========================================================================
def main():
    print("===== SISTEMA DE GESTIÓN ACADÉMICA =====")
    while True:
        try:
            n = int(input("Ingrese la cantidad de estudiantes a registrar: "))
            if n > 0:
                break
            print("Debe registrar al menos un estudiante.")
        except ValueError:
            print("Ingrese una cantidad numérica válida.")

    # --- Llamado a los 3 módulos de NIVEL 1 (top-down) ---
    nombres, areas, carreras, asignaturas, notas = registrar_alumnos(n)

    promedios_individuales, promedio_grupal, nota_max, nota_min, indice_mejor = procesar_notas(notas)

    mostrar_listado_final(nombres, areas, carreras, asignaturas, notas, promedios_individuales, promedio_grupal, nota_max, nota_min, indice_mejor)


if __name__ == "__main__":
    main()