#Ejercicio 3
def piramideinvert(base):
    """Funcion que dibuja una piramide invertida con la cantidad establecida en la base"""
    cerouno = base-1
    espace = 1
    for lines in range(base):
        if cerouno >= 0:
            print ('%s%s%s' % ( ('0'*cerouno), (' '*espace), ('1'*cerouno) ))
            cerouno -= 1
            espace += 2
