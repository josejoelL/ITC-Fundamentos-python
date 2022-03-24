# Insercion de costo de la compra
def catProductos():
    SeEscogio = False
    while not SeEscogio :
        Coca = 350
        Sprite = 700
        Fanta = 850
        print('---Menu---')
        print('1.- Coca Cola -',Coca)
        print('2.- Sprite -',Sprite)
        print('3.- Fanta -',Fanta)
        b=int(input('Ingrese el numero de bebida:'))
        if b >= 1 and b <= 3 : 
            SeEscogio = True
           # break
        else :
            print("no selecciono correctamente")
    if b == 1:
        c=Coca
    if b == 2:
        c=Sprite
    if b == 3:
        c=Fanta        
    return c

# Calculo de pago y cuanto sobra
def insercionDinero(costo):
    sumaTotal = 0
    SePago = False
    while not SePago  :
        print("su total es de : ",costo, " Ingrese el monto a pagar")
        insert =int( input() )
        sumaPrecio =+ insert
        if sumaPrecio < costo :
            print("a agregado :", sumaPrecio) 
        if sumaPrecio == costo :
            print("pago exacto")
            return 0
        if sumaPrecio > costo :
             SePago = True
    cambio =sumaPrecio - costo
    print("Su cambio es de : ", cambio)       
    return cambio         

#Monedas a devolver
def calcular_cambio(CantidadEntregar,CambioA,CambioB,CambioC,CambioD):
    SePagoTodo = False
    while not SePagoTodo :
        if CantidadEntregar >= A :
            CantidadEntregar -= A
            CambioA =+ 1
            calcular_cambio(CantidadEntregar,CambioA,CambioB,CambioC,CambioD)
        
        if CantidadEntregar >= B :
            CantidadEntregar -= B
            CambioB =+ 1
            calcular_cambio(CantidadEntregar,CambioA,CambioB,CambioC,CambioD)

        if CantidadEntregar >= C :
            CantidadEntregar -= C
            CambioC =+ 1
            calcular_cambio(CantidadEntregar,CambioA,CambioB,CambioC,CambioD)

        if CantidadEntregar >= D :
            CantidadEntregar -= D
            CambioD =+ 1
            calcular_cambio(CantidadEntregar,CambioA,CambioB,CambioC,CambioD)

        if CantidadEntregar == 0 :
            SePagoTodo = True
            break

        else:  
            CambioA = 0   #<-------  contadores
            CambioB = 0
            CambioC = 0
            CambioD = 0  
           

    TM = [CambioA, CambioB, CambioC, CambioD]  
    return TM      

# string
def mensajeCambio(TotalMonedas):
        print("Su cambio en monedas : ")
        if TotalMonedas[0] != 0:
            print( TotalMonedas[0]," monedas A :",A)
        if TotalMonedas[1] != 0:
            print( TotalMonedas[1]," monedas B :",B)
        if TotalMonedas[2] != 0:
            print( TotalMonedas[2]," monedas C :",C)
        if TotalMonedas[3] != 0:
            print( TotalMonedas[3]," monedas D :",D)

# Programa Principal
A = 500
B = 200
C = 100
D = 50
CambioA = 0   #<-------  contadores
CambioB = 0
CambioC = 0
CambioD = 0  
costo = catProductos()
CantidadEntregar = insercionDinero(costo)
TotalMonedas = calcular_cambio(CantidadEntregar,CambioA,CambioB,CambioC,CambioD)
mensajeCambio(TotalMonedas)