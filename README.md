# PracticaUnicaLFP SS2020
SimpleQL es un lenguaje de consultas que funciona únicamente a nivel de consola, su
propósito es facilitar al usuario la búsqueda de registros completos en archivos json, en los
que buscar registro por registro podría ser muy tedioso y cansado.

# PRE-REQUISITOS
1. Tener instalada la version actualizada de python
2. tener instalado pycharm

# Modo de uso 
Para poder utilizar SimpleQL abriremos pycharm, en la opcion OPEN, elegimos la carpeta llamada "PracticaUnica", luego de ello se mostrara una serie de carpetas y archivos con extensión py
>>> elegiremos el archivo llamdo main.py
>>> dentro del archivo presionamos shit + F10
se ejecutara el archivo principal y nos mostrara un menu similar a esto:
    "/*/*/*/*/*/*/*/*BIENVENIDO A SIMPLEQL*\\*\\*\\*\\*\\*\\"
    
    *******LENGUAJES FORMALES Y DE PROGRAMACION********
    
    $
luego del "$" podremos ingresar los comandos correspondientes para poder Cargar, Seleccionar, Contar, Verificar el Valor Maximo y minimo  de Edad, Valor Maximo y minimo de Promedio,y Generar el reporte en html.

# COMANDOS 
1. CARGAR: Este comando permitirá la carga de diferentes archivos a memoria, el único parámetro que lo conforma es una lista de direcciones a los archivos que cargará amemoria. *Estos Archivos son .JSON*

para poder cargar un archivo luego de haber ejecutado el main.py y que nos haya mostrado el menu, seguido del signo de dolar sin dejar espacio tecleamos  cargar archivo1, archivo2 despues de haber escrito el nombre de los archivos que deseamos cargar presionamos enter
y se nos muestra un mensaje indicando que los arcivos han sido cargados en memoria, cabe mensionar que el comando puede escribirse en mayusculas o minusculas, excepto los nombres de los archivos, esos deberán teclearse tal cual.
          
          *******LENGUAJES FORMALES Y DE PROGRAMACION********
    
          $ cargar archivo1, archivo2
          




2. SELECCIONAR:Permite seleccionar uno o más registros o atributos de los mismos con base en condiciones simples que pueden aplicarse a los atributos de los mismos.

                *******LENGUAJES FORMALES Y DE PROGRAMACION********
        1.    $ SELECCIONAR nombre, edad, promedio, activo DONDE nombre = “Francisco”  >>>> MUESTRA LOS CAMPOS ESCRITOS EN LA SELECCION siempre que cumpla con la condicion
        2.    $ SELECCIONAR * >>>Muestra todos los campos disponibles de cada registro
        3.    $SELECCIONAR nombre, edad DONDE promedio = 14.45 Mustra los campos escritos en la seleccion siempre que cumpla con la condicion

3. MAXIMO: Permite encontrar el valor máximo que se encuentre en el atributo de uno de losregistros del conjunto en memoria, estps pueden ser edad, promedio.
                  *******LENGUAJES FORMALES Y DE PROGRAMACION********
                  $ maximo edad
                   La edad maxima es 25
                   
4. MINIMO: Permite encontrar el valor minimo que se encuentre en el atributo de uno de losregistros del conjunto en memoria, estps pueden ser edad, promedio.
                  *******LENGUAJES FORMALES Y DE PROGRAMACION********
                  $ minimo edad
                   La edad minima es 18
                   
                   
5. SUMA: Permite obtener la suma de todos los valores de un atributo especificado en el comando.
                           *******LENGUAJES FORMALES Y DE PROGRAMACION********
                            $ SUMA promedio
                            
6. CUENTA: Permite obtener el total de registros en memoria
                      *******LENGUAJES FORMALES Y DE PROGRAMACION********
                            $ cuenta
                             total de registros 8
                             
7. REPORTAR: Este comando permite crear un reporte en html que contiene N cantidad de registros. N es el total de registros a elegir mostrar en el html
                                 *******LENGUAJES FORMALES Y DE PROGRAMACION********
                            $ REPORTAR 8
                              reportando...
                              el archivo html se podra encontrar en la carpeta que contiene al archivo main
  
  # NOTA
        Los campos y los comandos pueden escribirse con mayusculas o minusculas
                             
                      
                            

