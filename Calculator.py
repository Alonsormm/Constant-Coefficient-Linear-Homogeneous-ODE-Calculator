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
    real = []
    imag = []
    final = ""
    for i in raices:
        if isinstance(i,complex):
            imag.append(i)
        else:
            real.append(i)
    real.sort()
    while 8123:
        if len(real) == 0:
            break
        raizTemp = real[0]
        count = 0
        for i in range(1,len(real)):
            if real[i] != raizTemp:
                break
            count+=1
        for i in range(count+1):
            termino = ""
            termino += "C"
            if raizTemp == 0:
                termino+="+"
                real.pop(0)
                final+=termino
                continue
            if i != 0:
                if i == 1:
                    termino+="x"
                else:
                    termino+= "x^("+str(i)+")"
            if raizTemp != 1:
                termino+="e^("+str(raizTemp)+"x)+"
            else:
                termino+="e^x"
            real.pop(0)
            final+=termino
    for i in imag:
        termino = ""
        termino+= "C"
        if i.real == 0:
            if i.imag != 1:
                termino += "cos(" + str(i.imag) + "x)+"
                termino += "Csen(" + str(i.imag) + "x)+"
            else:
                termino += "cos(x)+"
                termino += "Csen(x)"
        else:
            if i.real != 1:
                if i.imag != 1:
                    termino += "e^("+str(i.real)+"x)" + "cos(" + str(i.imag) + "x)+"
                    termino += "Ce^("+str(i.real)+"x)" + "sen(" + str(i.imag) + "x)+"
                else:
                    termino += "e^("+str(i.real)+"x)" + "cos(x)+"
                    termino += "Ce^("+str(i.real)+"x)" + "sen(x)+"
            else:
                if i.imag != 1:
                    termino += "e^(x)" + "cos(" + str(i.imag) + "x)+"
                    termino += "Ce^(x)" + "sen(" + str(i.imag) + "x)+"
                else:
                    termino += "e^(x)" + "cos(x)+"
                    termino += "Ce^(x)" + "sen(x)+"
        final += termino

    if final[-1] == "+":
        final = final [:-1]
    final = "Yp = " + final
    return final

#
#
#
#
#

def obtenerCoef(campos):
    expresion.clear()
    raices.clear()
    for i in campos:
        expresion.append(int(i.get()))
    n = int(num.get())
    carac = Label(miFrame, text = "Expresion Caracteristica: " + expresionCaracteristica(expresion,n))
    carac.grid(row = n+3)
    divisionSintetica(expresion,raices)

    raizTemp = str(raices)
    raizLabel = Label(miFrame, text = "Raices: " + raizTemp)
    raizLabel.grid(row = n+4)
    final = resultadoFinal(raices)
    finalLabel = Label(miFrame, text = final)
    finalLabel.grid(row = n+5)


def generarVentana():
    n= int(num.get())
    print(n)
    campos = []
    expresion.clear()
    raices.clear()
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
