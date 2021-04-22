#Este programa dice hola y pregunta por tu nombre
print("Hola humano¡!")
print("¿Cuál es tu nombre?") #Pregunta por sus nombres
myName = input()
print("Qué bueno conocerte, " + myName)
print("Tu nombre tiene estas letras:")
print(len(myName))
print("¿Cuál es tu edad?") #Pregunta por su edad
myAge = input()
print("Tendrás " + str(int(myAge) + 1) + " en un año.")
