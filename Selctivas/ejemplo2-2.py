"""
Construya un diagrama de flujo tal que dado como dato el sueldo 
de un trabajador, le aplique un aumento del 15% si su sueldo es 
inferior a $1000 y 12% en caso contrario. Imprima el nuevo sueldo
del trabajador.
"""
sueldo=float(input("Ingrese su sueldo: "))
if sueldo<1000:
    incremento=sueldo*0.15
else:
    incremento=sueldo*0.12
print(f"Su sueldo es: {sueldo+incremento}")