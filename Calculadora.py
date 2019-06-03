from tkinter import *
import numpy as coefi

raiz= Tk()
frame= Frame(raiz)
frame.pack()
num= StringVar()
entry= []

def inicio():
    Label(frame,text= "Ingrese orden de ecuacion").grid(row= 0,column= 0)
    Entry(frame,textvariable= num).grid(row= 0,column= 1)
    Button(frame,text= "listo",command= funcion).grid(row= 0,column= 2)

def funcion():
    for child in frame.winfo_children():
        child.destroy()
    while(len(entry)!=0):
        entry.pop()
    inicio()
    n= int(num.get())
    for i in range(0,n):
        Label(frame,text= "Coeficiente de la derivada "+str(n-i)).grid(row= i+1,column= 0)
        entry.append(Entry(frame))
        entry[i].grid(row= i+1,column= 1)
    Label(frame,text= "Coeficiente de la variable y  ").grid(row= n+1,column= 0)
    entry.append(Entry(frame))
    entry[n].grid(row= n+1,column= 1)
    boton= Button(frame,text= "Realizar la operacion",command= lambda:raices(boton))
    boton.grid(row= n+2,column= 1)

def raices(boton):
    boton.destroy()
    expre= ""
    n= int(num.get())
    for i in range(0,n+1):
        if(entry[i].get()!='0' and entry[i].get()!=''):
            expre+= entry[i].get()+"(m^"+str(n-i)+") +\n"
    Label(frame,text= "Polinomio caracteristico: ").grid(row= n+2,column= 0)
    text= Text(frame,width= 10,height= 3)
    text.grid(row= n+2,column= 1)
    text.insert(END,expre)
    scroll= Scrollbar(frame,command= text.yview)
    scroll.grid(row= n+2,column= 2)
    raices =
    #raices= coefi.zeros([n+1])
    for i in range(0,n+1):
        #raices[i]= int(entry[i].get())
        raices.append()
    #Label(frame,text= coefi.roots(raices)).grid(row= n+3,column= 0)
    print(coefi.roots(raices))
    #tenemos una lista con las raices, ahora como separamos cada una?

inicio()
raiz.mainloop()