#EJEMPLO DE USO DE REPOSITORIO

print("DATOS PERSONALES")
print("---------------- \n" )
while True:
 vnom = str(input("Ingrese su Nombre: "))
 try:
   vEdad = int(input("Ingrese su Edad: "))
   break 
 except: print("Valor no Corresponde")

print("---------------------------")
print(f"Su Nombre es: {vnom}")
print(f"Su Edad es: {vEdad}")

print("Programa Finalizado...")