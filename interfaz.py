from tkinter import *
from array import array

raiz= Tk()
miFrame= Frame(raiz, width= 300, height= 600)
miFrame.pack()
num= StringVar()
cte= StringVar()

def obtenerCoef(campos):
    temp = []
    for i in campos:
        temp.append(int(i.get()))
    print(temp)
    
def generarVentana():
    n= int(num.get())
    campos = []
    for i in range(0,n):
        campos.append(Entry(miFrame))
    for i in range(0,n):
        pide= Label(miFrame, text= "Coeficiente de la derivada " + str(n-i))
        pide.grid(row= i+1, column= 0)

        campos[i].grid(row= i+1, column= 1)

    pide= Label(miFrame, text= "Coeficiente de la variable y ")
    pide.grid(row= n+1, column= 0)

    campos.append(Entry(miFrame))
    campos[-1].grid(row= n+1, column= 1)

    boton= Button(miFrame, text="Realizar la operacion", command = lambda:obtenerCoef(campos))
    boton.grid(row= n+2, column= 1)

def inicializar():
    label= Label(miFrame, text= "Ingrese orden de la ecuacion")
    label.grid(row= 0, column= 0)

    texto= Entry(miFrame, textvariable = num)
    texto.grid(row=0, column=1)

    listo= Button(miFrame, text="Listo", command= generarVentana)
    listo.grid(row= 0, column= 2)

    raiz.mainloop()

inicializar()