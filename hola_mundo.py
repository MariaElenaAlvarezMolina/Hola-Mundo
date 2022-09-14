#No.1
text = "Hola, Mundo"
print(text)

#No.2
name = "María Elena"
#2a
print("Hola,", name)
#2b
print("Hola, "+name)

#No.3
num = 2
#3a
print("Hola,", num)
#3b
print("Hola, "+str(num))

#No.4
fave_food1 = "sushi"
fave_food2 = "chacarero"
#4a
print("Amo comer {} y {}".format(fave_food1, fave_food2))
#4b
print(f"Amo comer {fave_food1} y {fave_food2}")

#BONUS
#%-formatting
nombre = "María Elena"
edad = 29
print("Mi nombre es %s y tengo %d" % (nombre, edad))