# Exercicis - input()

#Exercici 1
nom = input("Introdueix el teu nom: ")
xarxa = input("Introdueix el nom de la xarxa que estas instal.lant: ")

print(f" El técnic {nom} està instal.lant la xarxa {xarxa}.")

# Exercici 2
longitud_fibra = float(input("Introdueix la longitud d'un enllaç de la fibra (en km): "))
v_transmissio = float(input("Introdueix la velocitat de transmissió (en Gbps): "))

dades_gb = 1
dades_gb_bits = dades_gb * 8
temps = dades_gb_bits / v_transmissio

print(f"Per un enllaç de {longitud_fibra} caldrien {temps} segons per transmetre 1 GB de dades a una velocitat de {v_transmissio} Gbps.")

# Exercici 3

hores_feina = int(input("Introdueix el nombre d'hores de feina: "))
preu_per_hora = float(input("Introdueix el preu per hora d'una instal.lació de xarxa: "))
preu_material = float(input("Introdueix el preu del material utilitzat: "))

preu_total =(hores_feina * preu_per_hora) + preu_material

print(f"Preu total de la instal.lació: {preu_total} €.")
