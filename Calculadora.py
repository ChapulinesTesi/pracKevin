def suma(n1=0,n2=0):
    return n1+n2
def SUMAR(funcion,n1=0,n2=0):
    return funcion(n1,n2)
    
print("PROGRAMA QUE REALIZA SUMA CON 2 NÚMEROS\n")
numero1=float (input("Ingresa el primer numero: "))
numero2=float (input("Ingresa el segundo numero: "))

print("\n RESULTADOS DE OPERACION")
fun_suma=suma
ress=SUMAR(fun_suma,numero1,numero2)
print("La suma es =",ress)
