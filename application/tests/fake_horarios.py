#fake_horarios.py
from random import randint, choice
from datetime import time

def fake_hora(hora_m):
    t_op=[((hora_m-1, randint(39, 49),randint(0, 59)),1),
        ((hora_m-1, randint(49, 59),randint(0, 59)),3),
        ((hora_m, randint(0, 14),randint(0, 59)),2),
        ((hora_m,0,0),3),          
        ((hora_m, randint(15, 29), randint(0, 59)),2),
        ((hora_m, randint(29, 39), randint(0, 59)),1),
        ((hora_m, randint(40, 59), randint(0, 59)),1)]

    h,m,s= choice(
            [
                hora for hora, peso in t_op for d in range(peso)
            ]
        )
    
    return time(h, m,s)
           
    
                   
