import os
import shutil

import time
#para renombrar un archivo os.rename('archivo_original.txt','nombre_nuevo.txt')
# os.rename('Modulo_tres.rar','Modulo_tres.html')
# os.rename('archivo_sin_renombre.txt','otro.txt')

#se ejecuta la excepcion FileNotFoundError si no encuentra el asrchivo


shutil.move('mover/Modulo_tres.js', 'Modulo_tres.html')
time.sleep(5)
shutil.copy('Modulo_tres.html','mover/Modulo_tres.js' )
