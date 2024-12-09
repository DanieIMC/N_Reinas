import random
import math

# Función para calcular el número de ataques (conflictos) entre las reinas
def calcular_conflictos(tablero):
    conflictos = 0
    n = len(tablero)
    for i in range(n):
        for j in range(i+1, n):
            if tablero[i] == tablero[j]:
                conflictos += 1  # Misma columna
            elif abs(tablero[i] - tablero[j]) == abs(i - j):
                conflictos += 1  # Misma diagonal
    return conflictos

# Función de Simulated Annealing para resolver el problema de las n-reinas
def simulated_annealing(n, max_iter=1000, initial_temp=100, alpha=0.99):
    # Generamos una solución inicial aleatoria
    estado_actual = [random.randint(0, n-1) for _ in range(n)]
    temperatura = initial_temp

    # Mejor solución encontrada
    mejor_estado = estado_actual
    mejor_conflictos = calcular_conflictos(estado_actual)

    for _ in range(max_iter):
        # Generamos un vecino (una pequeña modificación)
        vecino = estado_actual[:]
        i = random.randint(0, n-1)
        vecino[i] = random.randint(0, n-1)
        
        # Calculamos el número de conflictos en el vecino
        conflictos_vecino = calcular_conflictos(vecino)

        # Si el vecino es mejor, lo aceptamos
        if conflictos_vecino < mejor_conflictos:
            mejor_estado = vecino
            mejor_conflictos = conflictos_vecino

        # Si el vecino es peor, lo aceptamos con una probabilidad
        if conflictos_vecino <= mejor_conflictos or random.random() < math.exp((calcular_conflictos(estado_actual) - conflictos_vecino) / temperatura):
            estado_actual = vecino
        
        # Reducir la temperatura
        temperatura *= alpha

    return mejor_estado, mejor_conflictos

# Número de reinas
n = 8
mejor_solucion, conflictos = simulated_annealing(n)

print(f"Mejor solución encontrada: {mejor_solucion}")
print(f"Número de conflictos: {conflictos}")
