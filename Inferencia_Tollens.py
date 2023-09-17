"Carlos Andrés Riveramelo Del Toro"

# Definimos las premisas

p = True  # Premisa 1: P es verdadero
q = False # Premisa 2: Q es falso

# Definimos la regla (si P, entonces Q)

def tollens(premisa1, premisa2):
    if not premisa2:
        return not premisa1
    else:
        return "No se puede aplicar Tollens, la premisa 2 es falsa."

# Aplicamos la regla

resultado = tollens(p, q)

# Mostramos el resultado

print("Resultado de Tollens:", resultado)