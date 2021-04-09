#This program says hello and asks for my name
print("Hello World")

print("¿Cuál es tu nombre?") #ask for their name
myName = input ()
print("Es un placer conocerte, " + myName)
print("Tu nombre tiene estas letras:")
print(len(myName))

print("¿Cuál es tu edad?") #ask for their name
myAge = input()
print("Tendrás " + str(int(myAge) + 1) + " en un año.")
