def solicitud(empleados):
    print("\n---SISTEMA DE SOLICITUD DE VACACIONES---\n          ---(BorPac S.R.L)---\n")
    nombre = input("Hola soy BorPi su asistente para sacar sus vacaciones, por favor ingrese su nombre y apellido: ").lower()
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
                dias = input("Por favor ngrese la cantidad de dias que desea solicitar: ")
            dias = int(dias)
            while dias > i["dias"]:
                print("No tiene esa cantidad de dias disponibles")
                dias= int (input("Ingrese una nueva cantidad: " ))
            if dias <= i ["dias"]:
                i["dias"]-=dias
                print("\nSu solicitud ha sido enviada al jefe de area \nRecibira una respuesta a la brevedad\n")
                print (f"Le quedarian {i["dias"]} disponibles\n Gracias por usar BorPi-Bot, que tenga buen dia\n")

            encontrado=True
    
    if encontrado== False:
        print("No encontramos su nombre en nuestra base de datos.Comuniquese con recursos humanos o intente nuevamente con otro nombre")             
   
import csv
empleados=[

]
with open ("Libro1.csv","r") as archivo:
     encabezado= next(archivo)
     for linea in archivo:
        linea_limpia= linea.strip()
        datos = linea_limpia.split(";")
        dic_productos={"nombre":datos[0],"dias":int(datos[1])}
        empleados.append(dic_productos)
        print (dic_productos)


solicitud(empleados)

