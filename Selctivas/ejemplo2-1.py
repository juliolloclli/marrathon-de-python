"""
Construya un diagrama de flujo tal que dado como dato calificación 
de un alumno en un examen, escrita “aprobado” si su calificación es 
mayor o igual que 10.5 y “reprobado” en caso contrario.
"""

examen=float(input("ingrese su nota de examen: "))
if examen>=10.5 and examen <=20:
    print(f"ud. ha aprobado {examen}")
elif examen >=0 and examen <10.5:
    print(f"reprobado esfuercese mas {examen}")
else:
    print("Datos incorrectos")