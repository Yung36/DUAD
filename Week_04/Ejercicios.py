# Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.


nombre = input("¿Cual es su nombre?: ")
apellido = input("¿Cual es su apellido:?: ")
edad = int(input("¿Cual es su edad?: "))

if edad <= 2:
    categoria = "bebe"
elif edad <= 12:
    categoria = "niño"
elif edad <= 14:
    categoria = "preadolecente"
elif edad <= 19:
    categoria = "adolescente"
elif edad <= 35:
    categoria = "adulto joven"
elif edad <= 59:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

print (f"{nombre}{apellido}, con {edad} años , eres un {categoria}")