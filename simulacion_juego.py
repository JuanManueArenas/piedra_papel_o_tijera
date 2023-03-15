# programa pára simular  el juego piedra papel y tijera
import random

print("------------------------------------------")
print("---------piedra papel o tijera------------")
print("------------------------------------------")

#input

bot = random.randint(1,3)
user = int(input("agrega tu opcion"))
 
# Processing
if (bot==1): #piedra
    if(user==1):
        rta = "EMPATE"
    elif(user==2):
        rta = "GANASTE"
    else:rta = "perdiste"
elif (bot==2): #papel
    if(user==1):
       rta = "GANASTE"
    elif(user==2):
        rta = "EMPATE"
        




