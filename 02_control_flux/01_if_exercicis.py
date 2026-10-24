# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.


num1 = input("Introdueix un numero: ") 
num2 = input("Introdueix un altre numero: ")

num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(f"El numero més gran es el {num1}")
elif num1 < num2:
    print(f"El numero més gran es el {num2}")
else:
    print(f"Els dos numeros són iguals")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).

num1 = input("Introdueix un numero: ")
num2 = input("Introdueix un numero: ")

num1 = float(num1)
num2 = float(num2)

operacio = input("Introdueix l'operació: ")

if operacio == "/" and num2 == 0:
    print(f"No es pot dividir")
elif operacio == "+":
    o = num1 + num2
    print(f"{o}")
elif operacio == "*":
    o = num1 * num2
    print(f"{o}")
elif operacio == "/":
    o = num1/num2
    print(f"{o}")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

any = int(input("Introdueix un any: "))

if (any % 4 == 0 and any % 100 != 0) or any % 400 == 0:
    print(f"{any} es un any de trasapas.")
else:
    print(f"{any} no es de traspas.")


# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat = int(input("Introdueix una edat: "))

if edat >= 0 and edat <= 2:
    print(f"ets un nadó")
elif edat >= 3 and edat <= 12:
    print(f"ets un infant")
elif edat >= 13 and edat <= 17:
    print(f"ets un adolescent")
elif edat >= 18 and edat <= 65:
    print(f"ets un adult")
elif edat >= 66:
    print(f"Ets una persona gran")
else:
    print(f"Edat no vàlida")

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia_optica = float(input("Introdueix la potencia optica rebuda en dBm: "))

if potencia_optica < -27:
    print(f"El nivell {potencia_optica} és massa baix")
elif potencia_optica <= -8:
    print(f"El nivell {potencia_optica} és acceptable")
else: 
    print(f"El nivell {potencia_optica} és massa alt")

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = float(input("Introdueix la latencia en mil.lisegons: "))
paquets = float(input("Introdueix el percentatge de paquets perduts: "))

if latencia < 0 or 0 > paquets > 100:
    print("Latencia no acceptada.")
elif latenica <= 30 and paquets <= 1:
    print("Latencia excel.lent!")
elif latencia <= 80 and paquets <= 3:
    print("Latencia bona.")
elif latencia <= 150 and paquets <= 5:
    print("Latencia acceptable.")
else:
    print("Latencia deficient.")

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

servei_critic = input("La incidència afecta un servei crític? (s/n): ").strip().lower()
usuaris = int(input("Introdueix el nombre total d'usuaris de la xarxa: "))

if usuaris < 0:
    print(f"No poden existir {usuaris}.")
else:
    alternativa = input("Hi ha una alternativa de connexió? (s/n):").strip().lower()
    if(servei_critic == "s" and alternativa != "s") or (usuaris >= 50 and alternativa != "s" ):
        print("Prioritat crítica.")
    elif usuaris >= 10 or servei_critic == "s":
        print("Prioritat alta.")
    else:
        print("Prioritat baixa.")







    

