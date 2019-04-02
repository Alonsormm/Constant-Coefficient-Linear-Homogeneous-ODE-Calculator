from fractions import Fraction

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


def segGrado(expresion,vec):
    disc = (expresion[1]*expresion[1])-4*expresion[0]*expresion[2]
    if disc > 0:

def divisionSintetica(expresion,vec):
    if len(expresion) == 1:
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
            break;

expresion = []
raices = []

grado = int(input("Dame el orden de la ecuacion diferencial: "))
for i in range(grado+1):
    expresion.append(int(input("Dame coeficiente de la derivada " + str(grado-i) + ": ")))
divisionSintetica(expresion,raices)
print(raices)
