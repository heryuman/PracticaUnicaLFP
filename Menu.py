import json
import os
import GenerarHTML
loadfile=False
lista = []

def inicio():
    os.system("cls")
    print("/*/*/*/*/*/*/*/*BIENVENIDO A SIMPLE-SQL*\\*\\*\\*\\*\\*\\")
    print("*******LENGUAJES FORMALES Y DE PROGRAMACION********")

def  cargar_datos(ruta):
   with open(ruta) as cont:
      archivo = json.load(cont)
     # print("******------DATOS EN JSON--------*****")
      for archivo in archivo:
      # print("Nombre: "+archivo.get('nombre')+ " Edad: "+str(archivo.get('edad')))
       global lista
       lista.append(archivo)
     # print("La clase de la estructura es: ")
     # print(type(archivo))
      #print("******------ FIN DE DATOS EN JSON-------*****")

def imprimirDatos():
    i=0
    while i < len(lista):
        print("")
        print("******REGISTRO ******",i+1)
        print("Nombre:     "+lista[i].get("nombre"))
        print("Edad:     ",lista[i].get("edad"))
        print("Activo:   ",lista[i].get("activo"))
        print("promedio: ",lista[i].get("promedio"))
        i+=1
#funcion para calcular los Maximos
def Maximos(atribMax):
    if atribMax.lower() =="edad":
        print("el atributo maximo de ", atribMax + " es: ")
        i = 0
        edades = []
        while i < len(lista):
            edad = lista[i].get(atribMax)
            edades.append(edad)

            i += 1
        print(max(edades))
    elif atribMax.lower()== "promedio":
        print("el atributo maximo de ", atribMax + " es: ")
        i = 0
        proms = []
        while i < len(lista):
            prom = lista[i].get(atribMax)
            proms.append(prom)

            i += 1
        print(max(proms))





#Funcion para calcular los minimos
def Minimos(atribMax):
    if atribMax.lower() =="edad":
        print("el atributo maximo de ", atribMax + " es: ")
        i = 0
        edades = []
        while i < len(lista):
            edad = lista[i].get("edad")
            edades.append(edad)

            i += 1
        print(min(edades))
    elif atribMax.lower()== "promedio":
        print("el atributo maximo de ", atribMax + " es: ")
        i = 0
        proms = []
        while i < len(lista):
            prom = lista[i].get("promedio")
            proms.append(prom)

            i += 1
        print(min(proms))

#funcion para contar registros
def contar():
    print("El numero de registros cargados es: ",len(lista))

#funcion SUMADORA
def sumar(atribMax):
    if atribMax.lower() =="edad":
        print("La suma  de ", atribMax + " es: ")
        i = 0
        edades = []
        while i < len(lista):
            edad = lista[i].get("edad")
            edades.append(edad)

            i += 1
        print(sum(edades))
    elif atribMax.lower()== "promedio":
        print("La suma  de ", atribMax + " es: ")
        i = 0
        proms = []
        while i < len(lista):
            prom = lista[i].get("promedio")
            proms.append(prom)

            i += 1
        print(sum(proms))


def imprimirDatos2(selex):
   # print("printdatos 2")
    par1=""
    par2=""
    elegir=selex.split(sep=' ')

    if elegir[0]== "*":
       #print("asterisco")
        imprimirDatos()
    #print(elegir)
    else:
        f = 0
        while f < len(elegir):
           # print("xds")

            palabra = elegir[f]
            # print(palabra)
            letra = palabra[0]
            # print(letra)
            # print(palabra[0])
            if palabra[0] == '"':
                # print("tiene comillas")

                if (f + 1) < (len(elegir)):
                    palabra = elegir[f] + " " + elegir[f + 1]
                    # print(palabra)
                    elegir.pop(len(elegir) - 1)
                    elegir.pop(len(elegir) - 1)
                    elegir.append(palabra.replace('"', ""))
                # print(elegir)
                else:
                    print()
                    palabra = elegir[f]
                    elegir.pop(len(elegir) - 1)
                    elegir.append(palabra.replace('"', ""))
            f += 1

        try:

            k = 0
            while k < len(elegir):
                if elegir[k].replace(",", "").lower() == "donde":
                    par1 = elegir[k + 1].replace(",", "").lower()
                    par2 = elegir[k + 3].replace(",", "")
                # print(par1)
                # print(par2)
                k += 1

        except:
            print("Error: dato incorrecto o inexistente")

        try:
            coincidencia = False
            i = 0
            while i < len(lista):
                if str(lista[i].get(par1.lower())) == par2:
                    coincidencia = not coincidencia
                    j = 0
                    while j < (len(elegir)):
                        print()

                        if elegir[j].lower() == "donde":
                            print("")
                            # print("en el break")
                            break
                        else:
                            print("Su " + elegir[j].replace(",", "") + " es:",
                                  lista[i].get(elegir[j].replace(",", "").lower()))
                            j += 1

                i += 1
            if coincidencia == False:
                print("No hay coincidencia con la busqueda")
        except:
            print("error ")





 # INICIA BLOQUE DE OPCIONES
def verificarOpcion():



     while True:
         inicio()
         cadena = input("$ ")
         global loadfile
         verificar = cadena.split(sep=' ')

         #MENU cargar archivos
         try:
            if verificar[0].lower() == "cargar":
             # print("ESta en la funcion cargar")
             # print(verificar)
              i = 1
              while i < len(verificar):
               cargar_datos(verificar[i].replace(",", "") + ".json")
              # print(verificar[i].replace(",", ""))
               i += 1
               print("Archivo(s) cargado(s)")
            elif loadfile==False:
                loadfile = not loadfile
         except:
            print("ERROR: Archivo Inexistente, compruebe la escritura del nombre")

        #MENU SELECT
         try:

             if verificar[0].lower()=="seleccionar":
                 if loadfile==True:
              #       print("estas en la func. seleccionar")
                     verificar.pop(0)
                     eleccion= " ".join(verificar)
                     imprimirDatos2(eleccion)
                 else:
                     print("No se ha cargado ningun archivo")

         except:
             print("ERROR: comando invalido o dato inexisten, vuelva a intentarlo")


        #Menu maximos

         try:

             if verificar[0].lower()=="maximo":
                 if loadfile==True:
                     print("")
                     verificar.pop(0)
                     eleccion= " ".join(verificar)
                     Maximos(eleccion)
                 else:
                     print("No se ha cargado ningun archivo")

         except:
             print("ERROR: comando invalido o dato inexisten, vuelva a intentarlo")

            #menu minimos
         try:

             if verificar[0].lower()=="minimo":
                 if loadfile==True:
                     print("")
                     verificar.pop(0)
                     eleccion= " ".join(verificar)
                     Maximos(eleccion)
                 else:
                     print("No se ha cargado ningun archivo")

         except:
             print("ERROR: comando invalido o dato inexisten, vuelva a intentarlo")

   #menu SUMAR
         try:

             if verificar[0].lower()=="suma":
                 if loadfile==True:
                     print("")
                     verificar.pop(0)
                     eleccion= " ".join(verificar)
                     sumar(eleccion)
                 else:
                     print("No se ha cargado ningun archivo")

         except:
             print("ERROR: comando invalido o dato inexisten, vuelva a intentarlo")

   #menu CONTAR
         try:

             if verificar[0].lower()=="cuenta":
                 if loadfile==True:
                     print("")
                     contar()

                 else:
                     print("No se ha cargado ningun archivo")

         except:
             print("ERROR: comando invalido o dato inexisten, vuelva a intentarlo")


   #menu REPORTAR
         try:

             if verificar[0].lower()=="reportar":
                 if loadfile==True:
                     print("reportando")
                     verificar.pop(0)
                     eleccion = " ".join(verificar)
                     print(eleccion)
                     GenerarHTML.html_create(lista,eleccion)
                 else:
                     print("No se ha cargado ningun archivo")

         except:
             print("ERROR: comando invalido o dato inexisten, vuelva a intentarlo")

