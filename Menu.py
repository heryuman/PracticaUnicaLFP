import json
def  cargar_datos(ruta):
   with open(ruta) as cont:
      archivo = json.load(cont)
      print("******------DATOS EN JSON--------*****")
      for archivo in archivo:
       print(archivo.get('nombre')+ " "+archivo.get('Apellido'))
      print("La clase de la estructura es: ")
      print(type(archivo))
      print("******------ FIN DE DATOS EN JSON-------*****")



def verificarOpcion(cadena):
     verificar=cadena.split(sep=',')
    # verificar=cadena.split(sep=' ')
     if verificar[0] == "cargar":
         print("ESta en la funcion cargar")
         print(verificar)

         i = 1
         while i < len(verificar):
             cargar_datos(verificar[i])
             i += 1
         print("Programa terminado")


   #  print(len(verificar))

