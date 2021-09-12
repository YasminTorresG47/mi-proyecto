import os
import operator
from typing import Counter
from estadistica import adm_serie, la_media, la_varianza, la_desviatipica, el_coefvariacion, el_rango, la_moda
from seguridad import nuevo_usuario, validar_usuario, adivinanzas, concedido

os.system("clear")

usuario0= ""
clave0=""
sesion=""
adivina=False
Op_Calculos=1
Op_Acceso=2
OP_Salir = 3

serie=1
media=2
varianza=3
desvtipica=4
coefvarianza=5
recorrido=6
moda=7
salirpal=8

def menu_principal():
    os.system("clear")
    print("")
    print(f'''         🔣  CALCULADORA ESTADISTICA  🔢
    ===========================================
         {Op_Calculos}) Realizar Estadistica descriptiva
         {Op_Acceso}) Cambiar Contraseña
         {OP_Salir}) Salir
    ''')

def menu_formulas():
    os.system("clear")
    print("")
    print(f'''     🔣 CALCULADORA ESTADISTICA DESCRIPTIVA 🔢
    ======== Formulas Estadisticas ============
         {serie}) Creacion de la Serie de valores
         {media}) Media
         {varianza}) Varianza
         {desvtipica}) Desviación Típica
         {coefvarianza}) Coeficiente de Variación
         {recorrido}) Rango o Recorrido
         {moda}) Moda
         {salirpal}) Regresar al menú principal
    ''')

iterar1 = True
iterar2 = True
lis_serie1=[]
while iterar1:
    os.system("clear")
    if sesion=="":
        adivina=concedido()
        
        if adivina==False:
            iterar1=False
            break
        if adivina==True:
            sesion="paso"
            
    if adivina==True and sesion=="paso":
        menu_principal()
        menupal = int(input("   Digite opcion de 1 a 3: "))
        
        if menupal<1 or menupal>3:
            print("   Opcion incorrecta")
            x=input("   Oprima Enter para continuar.")
            continue

        if menupal==3:
            print("")
            print("   Nos vemos......")
            print("")
            break

        if menupal==1 and adivina==True:
            while iterar2:
                os.system("clear")
                menu_formulas()
                if len(lis_serie1)==0:
                    print("  RECUERDE CREAR PRIMERO LA SERIE DE (POBLACION) DE DATOS")
                    print("")
                menufor = int(input("Digite opcion de 1 a 8: "))
                if menufor<1 or menufor>8:
                    print("   Opcion incorrecta")
                    x=input("   Oprima Enter para continuar.")
                    continue
                if menufor==1:
                    print("")
                    print("  Gestiona la serie  ")
                    print("")
                    lis_serie1=adm_serie()
                if len(lis_serie1)!=0:
                    if menufor==2:
                        print("")
                        print ("La Media de la serie es: ",la_media())
                        print("")
                    if menufor==3:
                        print("")
                        print("La Varianza de la serie es: ",la_varianza())
                        print("")
                    if menufor==4:
                        devtip=la_desviatipica()
                        print("")
                        print("La Desviacion Típica es: {:.4f} ".format(devtip))
                        print("")  
                    if menufor==5:
                        coefivar=el_coefvariacion()
                        print("")
                        print("El Coeficiente de Variacion es: {:.4f} ".format(coefivar))
                        print("")  
                    if menufor==6:
                        vrango=el_rango()
                        print("")
                        print("El Rango es: {:.4f} ".format(vrango))
                        print("")
                    if menufor==7:
                        la_moda()
                if menufor==8:  
                   break
                x=input("enter para continuar")
        if menupal==2:
            try:
                nuevo_usuario()
                print("")
                print("Reingrese con su nuevo USUARIO y CLAVE")
                x=input("   Oprima Enter para continuar.")
                break
            except:
                print("")
                print ("            Registre su usuario y contraseña.")
                print ("        Menú Principal, opcion 2 cambiar contraseña")
