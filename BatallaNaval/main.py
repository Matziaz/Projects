# main para juego de batalla naval

import batalla_naval as jbn
import utilerias as ut
import time

obj_ut = ut.Utilerias()

obj_jbn=jbn.JuegoBN()
obj_jbn.carga_matriz_file()

while obj_jbn.aciertos <9 and obj_jbn.fallos <10:
    obj_jbn.muestra_matriz()
    ren = obj_ut.pide_entero("Indica el renglón de tiro (8 para guardar): ",0,8)
    col = obj_ut.pide_entero("Indica la columna de tiro (8 para guardar): ",0,8)
    obj_jbn.tiro(ren,col)
              
if obj_jbn.aciertos==9:
     obj_ut.mensaje("Has ganado el juego")
     time.sleep(2)
 
else:
     obj_ut.mensaje("Has perdido el juego")
     time.sleep(2)
