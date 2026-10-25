#~< >

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

n = 10

while n >= 1:
    print(n)
    n -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

n = 1
suma = 0
while n <= 20:
    if n % 2 == 0:
        suma += n
    n += 1

print(suma)

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input("Introdueix un numero: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1
print(f"{num} != {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida"

contrasenya = input("Introdueix una contrasenya: ")

while len(contrasenya) < 8:
    print("Ha de tenir com a mínim 8 caràcters. Torna a provar.")
    contrasenya = input("Introdueix una contrasenya: ")

print("Contrasenya valida.")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

num = int(input("Introdueix un numero: "))

i = 1

while i <= 10:
    print(f"{num} . {i} = {num * i}")
    i += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

N = int(input("Introdueix un numero: "))

i = 2

while i <= N:
    divisor = 2
    es_primer = True
    while divisor < i:
        if i % divisor == 0:
            es_primer = False
        divisor += 1
    if es_primer:
        print(i)
    i += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.

num = int(input("Introdueix un numero: "))
suma = 0
while num != 0: 
    suma += num
    num = int(input("Introdueix un numero: "))
print("suma: ", suma)

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.

num = int(input("Introdueix un numero: "))

i = 0

while num > 0:
    num = num // 10
    i += 1
print("Nombre de xifres: ", i)

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

termes = int(input("Quants termes vols veure?"))
a = 0
b = 1
i = 0

while i < termes:
    print(a)
    a, b = b, a + b
    i += 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

secret = 7
num = int(input("Introdueix el numero secret: "))

while num != secret:
    if num < secret:
        print("El numero secret es més gran.")
    else:
        print("El numero secret es més petit.")

    secret = int(input("Torna-ho a provar: "))
print("Ho has encertat!")





