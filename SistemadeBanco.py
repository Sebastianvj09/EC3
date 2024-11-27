#Trabajo Final
#Menú de Opciones
#1. Aperturar Cuenta
#2. Cerrar Cuenta
#3. Depósito en Cuenta
#4. Retiro de Cuenta
#5. Transferencia entre Cuentas
#6. Saldos de Cuenta
#7. Movimientos de Cuenta
#8. Listar Cuentas (NroCuenta, Titular, Saldo)
#Cuentas=[NroCuenta, Titular, FechaApertura, SaldoInicial, SaldoDisponible, Estado(A,I)]
#NrodeCuenta--> Deber ser un número correlativo que inicie en 10000000
#Movimientos=[NroCuenta, TipoMovi, Monto, Fecha]
#Consideraciones
##Saldo Inicial debe ser cero o mayor
##No se pueden realizar operaciones en cuentas inactivadas
##Los retiros o transferecias estan sujetas al saldo disponible
##Todos los montos ingresados deben ser positivos
CorrelativoCuenta=10000000
def AperturarCuentas(pCuentas, pMovi):
 lCuenta=[]
 lMovi=[]
 global CorrelativoCuenta
 print("APARTADO DE APERTURA DE CUENTAS")
 print("###############################")
 vNroCuenta=CorrelativoCuenta
 print("N°Cuenta: ",vNroCuenta)
 print("Titular Cuenta: ")
 vTitular=input()
 print("Fecha de apertura: ")
 vFecha=input()
 while True:
  print("Saldo Inicial: " )
  vSaldoIn=float(input())
  if vSaldoIn<0:
   print("Saldo inicial no válido...")
  else:
   break
#Adicionando datos de cuenta al arreglo local
 lCuenta.append(vNroCuenta)
 lCuenta.append(vTitular)
 lCuenta.append(vFecha)
 lCuenta.append(vSaldoIn)
 lCuenta.append(vSaldoIn)
 lCuenta.append('A')
#print(lCuenta)
# Adicionando datos de cuenta al arreglo general
 pCuentas.append(lCuenta)
#print(pCuentas)
 lMovi.append(vNroCuenta)
 lMovi.append("Apertura")
 lMovi.append(vSaldoIn)
 lMovi.append(vFecha)
 pMovi.append(lMovi)
 CorrelativoCuenta=CorrelativoCuenta+1
def CerrarCuentas(lCuentas):
 print("APARTADO DE CIERRE DE CUENTAS")
 print("###############################")
 if len(lCuentas)>0:
  print("Ingrese en N° de Cuenta:")
  vCuenta=int(input())
  vUbica=BuscarCuenta(lCuentas,vCuenta)
#print(vUbica)
if vUbica== -1:
 print("Cuenta no existe")
else:
 if lCuentas[vUbica][4]>0:
print("La cuenta tiene saldo dsiponible, debe hacer el retiro previo parapoder inactivar...")
else:
if lCuentas[vUbica][5]=='A':
lCuentas[vUbica][5]='I'
print("Cuenta inactivada de manera satisfactoria")
else:
print("La cuenta ya se encuentra inactiva")
else:
print("La lista de cuentas está vacía")
def BuscarCuenta(pCuentas,NroCuenta):
pos=-1
for i in range(0, len(pCuentas)):
if pCuentas[i][0]==NroCuenta:
pos=i
break
return pos
#================= Menú Principal ==========================
lCuentas=[]
lMovimientos=[]
while True:
print("Menú de Opciones")
print("================")
print("1. Aperturar Cuenta")
print("2. Cerrar Cuenta")
print("3. Depósito en Cuenta")
print("4. Retiro de Cuenta")
print("5. Transferencia entre Cuentas")
print("6. Saldos de Cuenta")
print("7. Movimientos de Cuenta")
print("8. Listar Cuentas")
print("9. Salir")
print("Ingrese una opción-->")
Op=int(input())
if Op==1:
AperturarCuentas(lCuentas, lMovimientos)
elif Op==2:
CerrarCuentas(lCuentas)
elif Op==3:
print("")
#DepositoCuenta(lCuentas,lMovimientos)
elif Op==4:
print("")
#RetiroCuenta(lCuentas,lMovimientos)
elif Op==5:
print("")
#TransferCuentas(lCuentas,lMovimientos)
elif Op==6:
print("")
#SaldoCuenta(lCuentas)
elif Op==7:
print("")
#MoviCuentas(lCuentas,lMovimientos)
elif Op==8:
print("")
#ListaCuentas(lCuentas)
elif Op==9:
break
else:
print("Opción no válida....")