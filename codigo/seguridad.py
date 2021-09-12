import random
def nuevo_usuario():
    try:
        print("")
        print("")
        print("   PROGRAMA ESTADISTICA DESCRIPTIVA")
        print("   =================================")
        print("             Registro de Usuario y Clave")
        print("")
        usuario=input("     Nuevo Usuario: ")
        clave = input("     Nueva Clave  : ")
        print("")
        usuario=usuario+"\n"
        clave=clave+"\n"
        f = open('acceso.txt','w')
        f.write(usuario)
        f.write(clave)
        f.close()
    except:
        print ("No pudo crear el archivo txt en su carpeta.")

def validar_usuario(usuario0,clave0):
    global adivina
    global sesion
    reg=0
    #try:
    f = open ('acceso.txt','r')
    for linea in f:
        reg+=1
        if reg==1:
            usuario=linea
        if reg==2:
            clave=linea
    f.close()   

    if usuario0+"\n"==usuario and clave0+"\n"==clave:
        sesion="paso"
        return sesion

def adivinanzas():
    print("")
    print("              Para verificar que eres una persona")
    print("               Resuelve la siguiente  adivinanza")
    print("                   con un numero de 1 a 10.")
    print("")
    adv=["_","Si soy el ganador, ¿Qué número soy?", "Tengo forma de patito, arqueado y redondito. Quién soy?", "¿Cuántos lados tiene el triángulo equilátero?", "¿Cuántas patas tiene un gato siamés?", "Soy más de cuatro sin llegar a seis, ¿Quién soy?", "Si le sumas su hermano gemelo el tres, ¿Qué número es?", "¿Cuántos días tiene la semana?", "¿Qué número se convierte en cero si le quitas la mitad?", "¿La novena navideña por cuantos días se hace?", "¿Tengo diez manzanas si las parto a la mitad, cuantas manzanas tengo?"]
    azar = random.randint(1, 10)

    print("         *** ",adv[azar], end=" ")
    xadv=int(input(""))
    if xadv==azar:
        return True
    else:
        return False

def concedido():
    global adivina
    global sesion
    print("")
    print("")
    print("          🔣  ESTADISTICA DESCRIPTIVA   🔢")
    print("          =================================")
    print("")
    print("        1-Usuario Registrado,  2-Usuario Nuevo",end=" ")
    regnue=int(input(""))
    if regnue==1:
        usuario0=input("                Digite su usuario: ")
        clave0=input  ("                Digite su clave  : ")  
        sesion=validar_usuario(usuario0,clave0)

        if sesion=="paso":
            adivina=adivinanzas()
            if adivina==True:
                print("               BIENVENIDO  ✅")
                print("")
                x=input("              Oprima Enter para continuar.")

        if sesion!="paso":
            print("                 Acceso Denegado")
            x=input("              Oprima Enter para continuar.")
            iterar1=False
            adivina=False
    if regnue==2: 
        try:
            nuevo_usuario()
            print("")
            print("Reingrese con su nuevo USUARIO y CLAVE")
            x=input("   Oprima Enter para continuar.")               
        except:
            print("")
            print ("            Registre su usuario y contraseña.")
            print ("        Menú Principal, opcion 2 cambiar contraseña")
    return adivina
