import random

class ExplorerAgent:
    def __init__(self, grid_size):
        # Inicializamos el tamaño de la cuadrícula y la posición inicial del agente
        self.grid_size = grid_size
        self.position = (0, 0)  # Comienza en la esquina superior izquierda
        self.visited = set()  # Conjunto para almacenar las posiciones visitadas
        self.visited.add(self.position)  # Marca la posición inicial como visitada

    def get_neighbors(self, pos):
        # Obtiene los vecinos válidos (movimientos hacia arriba, abajo, izquierda, derecha)
        x, y = pos
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = [(x + dx, y + dy) for dx, dy in moves]
        
        # Filtra los vecinos que están dentro de los límites de la cuadrícula
        return [(nx, ny) for nx, ny in neighbors if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size]

    def explore(self):
        # Obtiene los vecinos no visitados
        neighbors = [n for n in self.get_neighbors(self.position) if n not in self.visited]
        
        # Si hay vecinos no visitados, elige uno aleatorio y se mueve
        if neighbors:
            self.position = random.choice(neighbors)
            self.visited.add(self.position)  # Marca la nueva posición como visitada
        else:
            print("No hay más lugares por explorar.")
        
        print(f"Explorando: {self.position}")

# Ejecución de prueba
grid_size = 5  # Tamaño de la cuadrícula (5x5)
explorer = ExplorerAgent(grid_size)

# El agente explora 20 veces
for _ in range(20):
    explorer.explore()

