


turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
            "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
            "012": ["Julian Martinez", "Argentina", "19-09-2023"],
            "014": ["Agustin Morales", "Argentina", "28-03-2024"],
            "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
            "006": ["Maria Lopez", "Mexico", "08-12-2023"],
            "007": ["Joao Silva", "Brasil", "20-06-2024"],
	        "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	        "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
            "008": ["Ana Santos", "Brasil", "03-10-2023"],
            "010": ["Martin Fernandez", "Argentina", "13-03-2023"],
            "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
     }

def mostrar_menu ():
    print ('''*** MENU PRINCIPAL ***
            1.- Turistas por país.
            2.- Turista por mes.
            3.- Eliminar turista.
            4.- Salir
            ''')
    

def turistas_por_pais():
    buscado = input("Ingrese el pais , de los turistas que desea visualizar:")
    encontrado = False
    for p in turistas:
        if (turistas[p][1]).lower() == buscado.lower():
            print (turistas[p][0])
            encontrado = True
    if not encontrado:
        len(turistas[p][1])== 0
        print ("No hay turistas en ese pais") 

def turistas_por_mes(mes):
    total = len(turistas)
    cantidad = 0

    for datos in turistas.values():
        fecha = datos[2]
        partes = fecha.split("-")

        if len(partes) == 3:
            mes_en_fecha = partes[1].lstrip("0")
            if mes_en_fecha == str(mes).lstrip("0"):
                cantidad += 1

    if total > 0:
        porcentaje = (cantidad * 100) / total
        print(f"\n Porcentaje de turistas en ese mes: {round(porcentaje, 1)}%")
    else:
        print("No hay turistas registrados.")



    
def eliminar_turista():
     nom_eliminado = input("Ingrese el nombre del turista a eliminar: ")
     for clave in list(turistas):
          if turistas[clave][0].lower() == nom_eliminado.lower():
               del turistas[clave]
               print ("Turista eliminado con éxito.")
               return   
     else:
        print( "Turista no encontrado. No se pudo eliminar.") 
def programa_terminado():
     print ("Programa terminado...")

                        
         
            
    



    
while True:
    mostrar_menu ()
    try:
            opcion = int (input("Ingresa una opcion , 1-2-3-4 :"))
            if opcion < 1 and opcion > 4:
                    print ("Ingrese un valor valido")
            if opcion == 4:
                    programa_terminado() 
                    break
            elif opcion == 1:
                    turistas_por_pais()
            elif opcion == 2:
                try:
                    mes = int(input("Ingrese un mes (1 a 12): "))
                    if mes >= 1 and mes <= 12:
                        turistas_por_mes(mes)
                    else:
                        print("Ingrese un valor entre 1 y 12")
                except ValueError as error:
                    print("Ingrese un valor válido")
            elif opcion == 3:
                 eliminar_turista()
            
    except ValueError as error:
            print ("Ingrese solo numeros")   
        

               


            
     
       
