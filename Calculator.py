from fractions import Fraction
from tkinter import *
from math import sqrt

raiz= Tk()
miFrame= Frame(raiz, width= 300, height= 600)
miFrame.pack()

expresion = []
raices = []

num= StringVar()
cte= StringVar()


def candRaiz(dep,ind):
    dep = abs(dep)
    ind = abs(ind)
    depPosible = []
    indPosible = []
    fin = []
    i = 1
    while(i <= dep/2):
        if dep%i == 0:
            depPosible.append(i)
        i+=1
    depPosible.append(dep)
    i = 1
    while(i<=ind/2):
        if ind%i == 0:
            indPosible.append(i)
        i+=1
    indPosible.append(ind)
    for i in indPosible:
        for j in depPosible:
            temp = i/j
            if temp not in fin:
                fin.append(temp)
    return fin


<<<<<<< HEAD
def segundoGrado(expresion, vec):
    a = expresion[2]
    b = expresion[1]
    c = expresion[0]
    disc = b*b-4*a*c
    if(disc == 0):
        vec.append(-b/(2*a))
        vec.append(-b/(2*a))
    elif(disc > 0):
        vec.append((-b+sqrt(disc))/(2*a))
        vec.append((-b-sqrt(disc))/(2*a))
    else:
        vec.append(complex((-b)/(2*a),sqrt(-disc)/(2*a)))
        vec.append(complex((-b)/(2*a),-sqrt(-disc)/(2*a)))
=======
def segundoGrado(expresion,vec):
    disc = (expresion[1]*expresion[1])-4*expresion[0]*expresion[2]
    if disc > 0:
        vec.append((-expresion[1]+disc**(0.5))/(2*expresion[0]))
        vec.append((-expresion[1]-disc**(0.5))/(2*expresion[0]))
    elif disc == 0:
        vec.append(-expresion[1]/(2*expresion[0]))
        vec.append(-expresion[1]/(2*expresion[0]))
    else:
        vec.append(complex(-expresion[1]/(2*expresion[0]),(-disc)**(0.5)/(2*expresion[0])))
        vec.append(complex(-expresion[1]/(2*expresion[0]),-(-disc)**(0.5)/(2*expresion[0])))
        
>>>>>>> 880f1de8cc4e2c4068cdab0c6293e8b420d0954b

def divisionSintetica(expresion,vec):
    if len(expresion) == 3:
        segundoGrado(expresion,vec)
        return
    candidatos = candRaiz(expresion[0],expresion[-1])
    c = 0
    tam = len(candidatos)
    while(c < tam):
        candidatos.append(-candidatos[c])
        c+=1
    semi = []
    resi = 0
    resta = 0
    i = 1
    for cand in candidatos:
        resi = 0
        resi = expresion[0]
        i = 1
        semi.clear()
        while(i<len(expresion)):
            semi.append(resi)
            resi = expresion[i] + (resi*cand)
            i+=1
        if resi == 0:
            divisionSintetica(semi,vec)
            vec.append(cand)
            break

def expresionCaracteristica(expresion,grado):
    carac = ""
    for i in range(grado+1):
        if expresion[grado-i] == 0:
            continue
        elif expresion[grado-i] == 1:
            if grado-i == 0:
                m = "1"
            else:
                m = ""
        else:
            m = str(expresion[grado-i])
        if grado-i == 0:
            m += ""
        elif grado-i == 1:
            m += "m+"
        else:
            m += "(m^" + str(grado-i) + ")+"
        carac += m
    return carac

#
#
#   
#
#

def resultadoFinal(raices):

#
#
#
#
#

def obtenerCoef(campos):
    for i in campos:
        expresion.append(int(i.get()))
    n = int(num.get())
    carac = Label(miFrame, text = "Expresion Caracteristica: " + expresionCaracteristica(expresion,n))
    carac.grid(row = n+3)
    divisionSintetica(expresion,raices)
    raizTemp = str(raices)
    raizLabel = Label(miFrame, text = "Raices: " + raizTemp)
    raizLabel.grid(row = n+4)


def generarVentana():
    n= int(num.get())
    print(n)
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
