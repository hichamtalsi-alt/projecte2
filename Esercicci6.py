
# Demanar tres nombres per teclat
num1 = float(input("Introdueix el primer nombre: "))
num2 = float(input("Introdueix el segon nombre: "))
num3 = float(input("Introdueix el tercer nombre: "))

# Comprovar quin és el nombre més gran
if num1 > num2 and num1 > num3:
    print("El nombre més gran és:", num1)
elif num2 > num1 and num2 > num3:
    print("El nombre més gran és:", num2)
else:
    print("El nombre més gran és:", num3)
