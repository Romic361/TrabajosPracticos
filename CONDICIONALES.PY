num =int (input("Ingrese un numero: "))

if num == 10:
    print ("¡Usted ha ganado el sorteo! ")
else:
    if num < 10:
        print ("¡Faltó un poco , seguí participando!")
    else:
        print ("¡Te pasaste, a seguir intentando")



dia = (input("Ingrese un día de la semana :  "))
if dia == "lunes":
    print ("seleccionó el primer día de la semana ")
elif dia == "viernes":

    print ("comienza el fin de semana ")
elif dia == "sabado" or "domingo":
    print ("el dia que seleccionó, es un día de descanso")
else:
    dia == "martes or miercoles or jueves"
    print ("plena semana, a trabajar!")


letra = (input ("Escriba una letra por favor : "))
if letra == "a" or "e" or "i" or "o" or "u":
    print ("es vocal")
else:
    print ("es consonante")
    
 
 
