import csv, os

ARCHIVO_NUEVO = input("Ingrese el nombre del archivo a crear: ")
CAMPOS_ARCHIVO_NUEVO = ["Legajo", "Apellido", "Nombre", "Total Vacaciones"]
ARCHIVO_EXISTENTE = "dias.csv"

def planilla(archivo, campos, archivo_vacaciones_tomadas):

    print("\n----------SISTEMA DE VACACIONES----------\n")

    while True:
        print("\nElija una opcion: \n\t1. Ingresar un empleado\n\t2. Imprimir lista de empleados\n\t3. Imprimir vacaciones tomadas\n\t4. Imprimir vacaciones disponibles\n\t5. Salir")

        opcion = int(input(""))

        if opcion == 1:
            guardar_planilla(archivo, campos)
        elif opcion == 2:
            cargar_planilla(archivo)
        elif opcion == 3:
            cargar_vacaciones_tomadas(archivo_vacaciones_tomadas)
        elif opcion == 4:
            vacaciones_disponibles(archivo, archivo_vacaciones_tomadas)
        elif opcion == 5:
            exit()
        else:
            print("Ingrese una opcion valida. Intente nuevamente.")

def guardar_planilla(archivo, campos):

    lista_empleados = []
    
    salir = ""

    print("\n----------INGRESO DE EMPLEADOS----------\n")

    while salir != "si":
    
        empleado = []
    
        for campo in campos:
            if campo == "Legajo" or campo == "Total Vacaciones":
                empleado.append(int(input(f"Ingrese el numero de {campo} del empleado: ")))
            else:
                empleado.append(input(f"Ingrese el {campo} del empleado: "))
        lista_empleados.append(empleado)
        
        salir = input("Desea salir del ingreso de empleados? si/no: ")
    
    try:
        archivo_existe = os.path.isfile(archivo)

        if archivo_existe:
            sobreescribir = input(f"\nEl archivo existe. Desea sobreescribir? si/no: ")
            
            if sobreescribir == "si":
                with open(archivo, "a", newline="") as file:
                    planilla = csv.writer(file)
                    planilla.writerows(lista_empleados)
                    print("\nEl archivo se modifico correctamente.")
            else:
                with open(archivo, "w", newline="") as file:
                    planilla = csv.writer(file)
                    planilla.writerows(lista_empleados)
                    print("\nEl archivo se guardo correctamente.")
        else:
            with open(archivo, "w", newline="") as file:
                planilla = csv.writer(file)
                planilla.writerows(lista_empleados)
                print("\nEl archivo se guardo correctamente.")
        return
    except IOError:
        print("\nOcurrio un error con el archivo.")

def cargar_planilla(archivo):

    try:
        with open(archivo, "r", newline="") as file:
            lectura_csv = csv.reader(file)
            for empleado in lectura_csv:
                print(f"Legajo: {empleado[0]} Apellido: {empleado[1]} Nombre: {empleado[2]} Total Vacaciones: {empleado[3]}")
            return
    except IOError:
        print("\nOcurrio un error con el archivo.")

def cargar_vacaciones_tomadas(archivo_vacaciones_tomadas):

    try:
        with open(archivo_vacaciones_tomadas, "r", newline="") as file:
            lectura_csv = csv.reader(file)
            for linea in lectura_csv:
                print(f"{linea[0]} \t{linea[1]}")
            return
    except IOError:
        print("\nOcurrio un error con el archivo.")
        
def vacaciones_disponibles(archivo, archivo_vacaciones_tomadas):

    legajo = input("\nIngrese el numero de legajo: ")
    cont = 0
    total_vacaciones = 0
    empleado_a_mostrar = []

    try:
        with open(archivo_vacaciones_tomadas, "r", newline="") as file:
            lectura_csv_1 = csv.reader(file)
            for linea in lectura_csv_1:
                if legajo == linea[0]:
                    cont+= 1
        with open(archivo, "r", newline="") as file:
            lectura_csv_2 = csv.reader(file)
            for empleado in lectura_csv_2:
                if legajo == empleado[0]:
                    total_vacaciones = int(empleado[3])
                    empleado_a_mostrar = empleado
        print(f"\nLegajo {empleado_a_mostrar[0]}: {empleado_a_mostrar[2]} {empleado_a_mostrar[1]}, le restan {total_vacaciones - cont} dias de vacaciones.")
        return
    except IOError:
        print("\nOcurrio un error con el archivo.")

planilla(ARCHIVO_NUEVO, CAMPOS_ARCHIVO_NUEVO, ARCHIVO_EXISTENTE)
