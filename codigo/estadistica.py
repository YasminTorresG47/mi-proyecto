import operator
from typing import Counter

global lis_serie
lis_serie=[]
def adm_serie():
    ciclo3= True
    while ciclo3:
        print("")
        print("  ¿Que operacion desea realizar?")
        print("======================================")
        print("1-Agregar número a la serie ")
        print("2-Modificar número de la serie")
        print("3-Borrar  numero de la serie")
        print("4-Consultar numero la serie")
        print("5-Salir")
        print("")

        gs=int(input("Digite Opción: "))
        if gs==1:
            enserie=True
            i=0
            while enserie:
                print("Agregue un numero a la serie (para terminar digite fin), ",i,": ",end=" ")
                elemento=input("")
                if elemento.upper() == "FIN":
                    enserie=False
                    break
                elemento=float(elemento)
                if elemento != "fin":
                    lis_serie.append(elemento)
                i+=1
            input(" Puede Consultar la Serie, Enter para continuar")
        if gs==2:    
            print("digite el indice del valor a cambiar: ",end=" ")
            idx=int(input(""))
            print("digite el valor a Cambiar: ",end=" ")
            new_valor=float(input(""))
            lis_serie[idx]=new_valor
        if gs==3:
            print("Digite el indice del valor a Borrar: ",end=" ")
            idx=int(input(""))
            lis_serie.pop(idx)
            print("    Dato Borrado, puede consultar serie")
            input("            Enter para continuar")
        if gs==4:
            print("Serie Registrada")
            print("===================")
            for i in range(0,len(lis_serie)):
                print("serie ",i,": ",lis_serie[i])
                i+=1
            input(" Enter para continuar")
        if gs==5:
            ciclo3= False
            break
    return lis_serie
        
def la_media():
    items=0
    media=0.0
    sum_media=0.0
    for i in lis_serie:
        sum_media=sum_media+i
    media=sum_media / len(lis_serie)
    print("La serie (poblacion) es: ",lis_serie)
    return media

def la_varianza():
    media=la_media()
    varianz=0.0
    for i in lis_serie:
        varianz=varianz+((i-media)**2)         
    varianz =varianz / len(lis_serie)
    return varianz
   
def la_desviatipica():
    desvitipica=la_varianza()
    desvitipica=desvitipica**.5
    return desvitipica


def el_coefvariacion():
    coefvaria=la_desviatipica()
    coefvaria=coefvaria / la_media()
    return coefvaria

def el_rango():
    rango=max(lis_serie)-min(lis_serie)
    return rango

def la_moda():
    Lista2 = list(filter(lambda n: n >= 0, lis_serie))
    lista3= dict(Counter(Lista2))
    lista3 = sorted(lista3.items(), key=operator.itemgetter(1), reverse= True)
    print("Serie, ordenada, mostrando las")
    print("repeteciones de cada elemento: ")
    print("   ",lista3)
    print("===============================")
    print("")
    print("Moda             Repite")
    print("=======        ========")
    j=0
    sw_valor=0
    for valor in (lista3):
        if valor[1]>1:
            print("  ", str(valor[0]).ljust(7), " ", str(valor[1]).rjust(7))
        j+=1
    print(" ")
    return 
