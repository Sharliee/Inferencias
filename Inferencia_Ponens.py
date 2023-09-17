"Carlos Andrés Riveramelo Del Toro"

# Definimos las premisas

p = True  # Premisa 1: P es verdadero
q = False # Premisa 2: Q es falso

# Definimos la regla (si P, entonces Q)

def modus_ponens(premisa1, premisa2):
    if premisa1:
        return premisa2
    else:
        return "No se puede aplicar Modus Ponens, la premisa 1 es falsa."

# Aplicamos la regla

resultado = modus_ponens(p, q)

# Mostramos el resultado

print("Resultado de Modus Ponens:", resultado)