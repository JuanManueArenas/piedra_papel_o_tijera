# programa pára simular  el juego piedra papel y tijera
import random

print("------------------------------------------")
print("---------piedra papel o tijera------------")
print("------------------------------------------")

#input

bot = random.randint(1,3)
user = int(input("Agregaste el numero "))
 
# Processing
if (user>3):
    rta = "usted digito un numero no valido"

if (bot==1): #piedra
    if(user==1):
        rta = "EMPATE"
    elif(user==2):
        rta = "GANASTE"
    else: 
        rta = "perdiste"
elif (bot==2): #papel
    if(user==1):
       rta = "GANASTE"
    elif(user==2):
        rta = "EMPATE"
    else:
        rta = "PERDISTE"
elif (bot==3): #tijera
    if(user==1):
        rta = "PERDISTE"
    elif(user==2):
        rta = "GANASTE"
    else:
        rta = "EMPATE"   


#output
print(rta)
print("Bot : " +str(bot))
print("USTED DIGITO: " +str(user))
    




