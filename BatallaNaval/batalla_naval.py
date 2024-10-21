import utilerias as ut
import os
import time

obj_ut = ut.Utilerias()

class JuegoBN():
    matriz= []
    file = ""
    aciertos= 0
    fallos = 0
    def __init__(self):
        self.matriz = []
        self.file = ""
        self.aciertos = 0
        self.fallos = 0
        self.iniciar_juego()
        
    def iniciar_juego(self):
        print("-" * 60)
        print("""
Para iniciar, indica el nombre del archivo que deseas cargar.
Si deseas una nueva partida, simplemente presiona [ENTER].
Escribe el nombre del archivo sin la extensión.
""")
        print("-" * 60)

        self.file = obj_ut.pide_cadena("Indique el nombre del archivo: ", 0, 10)
        self.file = "inicial.csv" if len(self.file) == 0 else self.file + ".csv"

    def carga_matriz_file(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as arch:
                for ren, registro in enumerate(arch.readlines()):
                    registro = registro.strip()
                    lista = registro.split(",")
                    self.matriz.append([])
                    for col in range(8):
                        self.matriz[ren].append(lista[col])
                        if self.matriz[ren][col] == "X":
                            self.fallos += 1
                        elif self.matriz[ren][col] == "A":
                            self.aciertos += 1
        else:
            obj_ut.mensaje("El archivo no existe")
            time.sleep(1)
            if len(self.file) == 0 or self.file != "inicial.csv":
                self.file = "inicial.csv"
            else:
                self.file += ".csv"
            self.carga_matriz_file() 

    def muestra_matriz(self):
        print("   0 1 2 3 4 5 6 7")
        print("  " + ("-" * 17))
        for ren in range(8):
            print(f"{ren} |", end="")
            for col in range(8):
                cell = self.matriz[ren][col]
                if cell in ("V", "B"):
                    print(" ", end="|")
                else:
                    print(cell, end="|")
            if ren == 0:
                print(f"     Aciertos= {self.aciertos}", end="")
            elif ren == 1:
                print(f"     Fallos= {self.fallos}", end="")
            print("\n  " + ("-" * 17))

    def descarga_matriz_file(self):
        nombre_file = obj_ut.pide_cadena("Nombre del archivo: ", 1, 10) + ".csv"
        with open(nombre_file, "w") as arch:
            for ren in range(8):
                registro = ",".join(self.matriz[ren]) + "\n"
                arch.write(registro)
        print("Archivo creado con éxito, finalizando el juego...")
        time.sleep(2)
        exit()

    def tiro(self, ren, col):
        if ren == 8 and col == 8:
            self.descarga_matriz_file()
        else:
            if self.matriz[ren][col] in ("A", "X"):
                obj_ut.mensaje("Error, ya existe un tiro previo en la celda")
            else:
                if self.matriz[ren][col] == "V":
                    obj_ut.mensaje("Celda vacía, se incrementan los errores")
                    self.fallos += 1
                    self.matriz[ren][col] = "X"
                else:
                    obj_ut.mensaje("Celda con barco, se incrementan los aciertos")
                    self.aciertos += 1
                    self.matriz[ren][col] = "A"
