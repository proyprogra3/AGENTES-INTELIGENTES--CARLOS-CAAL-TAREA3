def get_neighbors(pos, rows, cols):
    # Obtiene los vecinos válidos (dentro de los límites del entorno)
    x, y = pos
    neighbors = []
    if x + 1 < rows:  # Abajo
        neighbors.append((x + 1, y))
    if y + 1 < cols:  # Derecha
        neighbors.append((x, y + 1))
    if x - 1 >= 0:  # Arriba
        neighbors.append((x - 1, y))
    if y - 1 >= 0:  # Izquierda
        neighbors.append((x, y - 1))
    print(f"Vecinos de {pos}: {neighbors}")  # Verificación de vecinos
    return neighbors

def select_best_path(grid, start):
    rows, cols = len(grid), len(grid[0])
    current = start
    best_path = [current]
    total_utility = grid[current[0]][current[1]]

    while True:
        neighbors = get_neighbors(current, rows, cols)
        if not neighbors:  # Si no hay más vecinos, el agente ha llegado a un borde
            print(f"No más vecinos desde {current}. Finalizando.")
            break
        # Seleccionamos el vecino con el valor más alto de recompensa
        next_move = max(neighbors, key=lambda pos: grid[pos[0]][pos[1]])
        best_path.append(next_move)
        total_utility += grid[next_move[0]][next_move[1]]
        current = next_move
        print(f"Moviéndonos a {next_move}. Utilidad total: {total_utility}")

    return best_path, total_utility

# Definir el entorno con valores de recompensa en cada celda
grid = [
    [3, 1, 2, 4],
    [1, 5, 3, 2],
    [4, 2, 6, 1],
    [2, 3, 1, 7]
]

# Seleccionar la mejor ruta
start = (0, 0)  # La posición de inicio
best_path, total_utility = select_best_path(grid, start)

# Mostrar el recorrido óptimo y la utilidad total acumulada
print("Recorrido óptimo:")
for step in best_path:
    print(step)
print(f"Utilidad total acumulada: {total_utility}")

# PRUEBA FINAL CARLOS ROLANDO CAAL ARANA
