def solicitud(empleados):
    
    nombre = input("Por favor ingrese su nombre y apellido: ").lower()
    while nombre.strip().lower()=="":
        print("Error no puede ingresar un espacio en blanco")
        nombre= input("Por favor ingrese su nombre y apellido: ").lower()
    encontrado= False    
    for i in empleados:
        if i ["nombre"] == nombre:
            print(f"Tiene {i["dias"]} dias disponibles")
            dias = input("Ingrese la cantidad de dias que desea solicitar: ")
            while not dias.isdigit():
                print("Error. Debe ingresar un numero entero ") 
                dias = input("Por favor ingrese la cantidad de dias que desea solicitar: ")
            dias = int(dias)
            while dias > i["dias"]:
                print("No tiene esa cantidad de dias disponibles")
                dias= int (input("Ingrese una nueva cantidad: " ))
            if dias <= i ["dias"]:
                i["dias"]-=dias
                print("\nProcesando solicitud...")
                print("Verificando disponibilidad...")
                print("Solicitud enviada correctamente.\n")
                print (f"Le quedarian {i["dias"]} disponibles\n")
            encontrado=True
    
    if encontrado== False:
        print("No encontramos su nombre en nuestra base de datos. Comuniquese con recursos humanos o intente nuevamente con otro nombre")        

def consulta_dias(empleados):
    nombre = input("Por favor ingrese su nombre y apellido: ").lower()
    while nombre.strip().lower()=="":
        print("Error no puede ingresar un espacio en blanco")
        nombre= input("Por favor ingrese su nombre y apellido: ").lower()
    encontrado= False    
    for i in empleados:
        if i ["nombre"] == nombre:
            print("\nProcesando solicitud...")
            print(f"Tiene {i["dias"]} dias disponibles\n")
            encontrado=True
    if encontrado== False:
        print("No encontramos su nombre en nuestra base de datos. Comuniquese con recursos humanos o intente nuevamente con otro nombre") 


empleados=[

]
try:
    with open ("Libro1.csv","r") as archivo:
        encabezado= next(archivo)
        for linea in archivo:
            linea_limpia= linea.strip()
            datos = linea_limpia.split(";")
            dic_productos={"nombre":datos[0].lower(),"dias":int(datos[1])}
            empleados.append(dic_productos)
except FileNotFoundError:
    print ("No pude comunicarme con la base de datos, intente de nuevo mas tarde")

opcion = 0
print("\n---SISTEMA DE SOLICITUD DE VACACIONES---\n          ---(BorPac S.R.L)---\n")
print("Hola soy BorPi estoy aqui para ayudarlo a sacar sus vacaciones")
while opcion != 3:
    try:
        print("¿Como desea continuar?: \n\n1-Solicitar sus vacaciones \n2-Consultar su cantidad de dias disponibles \n3-Salir  ")
        opcion= int(input(""))
        if opcion == 1:
            solicitud(empleados)
            with open("Libro1.csv", "w") as archivo:
                archivo.write("nombre;dias\n")
                for empleado in empleados:
                    archivo.write(f"{empleado['nombre']};{empleado['dias']}\n")
        elif opcion == 2:
            consulta_dias(empleados)
        elif opcion == 3:
            print ("Gracias por usar BorPi-Bot, que tenga buen dia.\n")
        else:
            print("Opcion incorrecta")
    except ValueError:
        print("Error. Ingrese un numero valido")


