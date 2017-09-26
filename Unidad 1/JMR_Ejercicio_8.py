#Ejercicio 8
import random
def num_alto_o_bajo():
    """Funcion para jugar a encontrar el numero"""
    numero = random.randint(1, 100)
    print ("Es un numero entre el 1 y el 100")
    for num in range(1, 100) :
        print("Intenta adivinar")
        estimacion = input()
        estimacion = int(estimacion)

        if estimacion < numero:
            print ("El numero es muy bajo")

        if estimacion > numero:
            print ("El numero es muy alto")

        if estimacion == numero:
            print ("felicidades le adivinaste")
            break
            
