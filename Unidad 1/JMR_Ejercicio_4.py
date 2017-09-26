#Ejercicio 4
def piramide(base):
    """Funcion que dibuja una piramide con la cantidad establecida en la base"""
    spaces = base-1
    asterist = 1
    for lines in range(base):
        if spaces >= 0:
            print ('%s%s%s' % ( (' '*spaces), ('0'*asterist), (' '*spaces) ))
            spaces -= 1
            asterist += 2
