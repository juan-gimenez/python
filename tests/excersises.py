""" 1) function that returns max of two numbers"""
def max1(n1,n2):
    " function that return max"
    if n1 > n2:
        return n1
    else:
        return n2

a = -6
b = -8
maximo = max1(a,b)
print(maximo)

""" 2) funcion max de 3 """

def maxde3(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

print(maxde3(143,343434,342322))

""" 3) funcion que toma un caracter y devuelve true si es vocal o sino false"""

def is_vocal(char):
    vocales = ["a","e","i","o","u"]
    if char not in vocales:
        return False
    else:
        return True

print(is_vocal("u"))

""" 4) sum de lista"""

def sum_lista(lista):
    suml = 0
    for item in lista:
        suml += item
    return suml


print(sum_lista([1,2,3,4,2,45454,2]))


""" 5) inversa una cadena"""

def inversa(string):
 for i in range(len(string),-1):
    print (string[i])

inversa("hola")


""" 6) Funcion es_palindromo retorna true si la cadena es palindromo"""

def is_palindromo(string):
    reversed1 = (string[::-1])
    print ("True") if reversed1 == string else print("False")


is_palindromo("ana")