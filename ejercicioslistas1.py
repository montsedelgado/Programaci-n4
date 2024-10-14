
import random


VidaA = 100
AtaqueA = 25
VidaB = 100
AtaqueB = 25

inicia=random.randrange(1,10,1)
if inicia >=5: 
    #Ataque de A hacia B
    VidaB -= AtaqueA
    print(f"El jugador A ataco a A" "\n" f"a el jugador B le restan {VidaB}")
    
else:
    #Ataque de B hacia A
    VidaA -= AtaqueB
    print(f"El jugador B ataco a A" "\n" f"a el jugador B le restan {VidaA}")
    