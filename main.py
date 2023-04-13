import random
import tkinter as tk

def crear_tablero(filas, columnas, minas):
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    minas_generadas = 0
    while minas_generadas < minas:
        fila = random.randint(0, filas-1)
        columna = random.randint(0, columnas-1)
        if tablero[fila][columna] != -1:
            tablero[fila][columna] = -1
            minas_generadas += 1
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(valor) for valor in fila))

def main():
    filas = 5
    columnas = 5
    minas = 5
    tablero = crear_tablero(filas, columnas, minas)
    imprimir_tablero(tablero)

if __name__ == "__main__":
    main()

class BuscaminasGUI(tk.Frame):
    def __init__(self, master=None, filas=5, columnas=5, minas=5):
        super().__init__(master)
        self.master = master
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.tablero = crear_tablero(filas, columnas, minas)
        self.crear_widgets()
        
    def crear_widgets(self):
        self.botones = []
        for fila in range(self.filas):
            fila_botones = []
        for columna in range(self.columnas):
            boton = tk.Button(self, text="", width=2)
            boton.grid(row=fila, column=columna)
            fila_botones.append(boton)
        self.botones.append(fila_botones)
        
        for fila, fila_botones in enumerate(self.botones):
            for columna, boton in enumerate(fila_botones):
                boton.config(command=lambda f=fila, c=columna: self.clic_boton(f, c))

    def clic_boton(self, fila, columna):
        valor = self.tablero[fila][columna]
        if valor == -1:
            self.botones[fila][columna].config(text="X")
        else:
            self.botones[fila][columna].config(text=str(valor))

if __name__ == "__main__":
    root = tk.Tk()
    app = BuscaminasGUI(master=root)
    app.pack()
    app.mainloop()
