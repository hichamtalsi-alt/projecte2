
# Demanar dos nombres enters
num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))

# Calcular les operacions
suma = num1 + num2
resta = num1 - num2
multiplicacio = num1 * num2

# Mostrar els resultats
print("La suma és:", suma)
print("La resta és:", resta)
print("La multiplicació és:", multiplicacio)

# Comprovar que no es divideixi entre zero
if num2 != 0:
    divisio = num1 / num2
    print("La divisió és:", divisio)
else:
    print("No es pot dividir entre zero.")
