import heapq

# Definimos las direcciones posibles (arriba, derecha, abajo, izquierda)
MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class AStarAgent:
    def __init__(self, maze, start, goal):
        self.maze = maze  # El laberinto representado como una matriz
        self.start = start  # La posición de inicio
        self.goal = goal  # La posición de la meta
        self.rows = len(maze)
        self.cols = len(maze[0])

    def heuristic(self, pos):
        # Heurística de Manhattan: suma de las diferencias de las coordenadas
        return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])

    def get_neighbors(self, pos):
        # Obtiene los vecinos válidos (dentro de los límites del laberinto)
        neighbors = []
        x, y = pos
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.maze[nx][ny] == 0:
                neighbors.append((nx, ny))
        return neighbors

    def find_path(self):
        # Algoritmo A* para encontrar la ruta más corta
        open_list = []
        heapq.heappush(open_list, (0 + self.heuristic(self.start), 0, self.start))  # (f, g, pos)
        came_from = {}  # Diccionario para reconstruir la ruta
        g_score = {self.start: 0}  # Costo desde el inicio hasta el nodo actual
        f_score = {self.start: self.heuristic(self.start)}  # Costo estimado total (f = g + h)

        while open_list:
            _, current_g, current = heapq.heappop(open_list)

            if current == self.goal:
                # Si alcanzamos la meta, reconstruimos la ruta
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                path.reverse()
                return path

            for neighbor in self.get_neighbors(current):
                tentative_g_score = current_g + 1  # El costo para movernos de current a neighbor

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor)
                    heapq.heappush(open_list, (f_score[neighbor], tentative_g_score, neighbor))

        return None  # Si no se encuentra una ruta

# Definimos el laberinto (0 = espacio libre, 1 = pared)
maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

# Definimos la posición inicial y la meta
start = (0, 0)  # Posición inicial
goal = (4, 4)   # Posición de la meta

# Crear el agente y encontrar la ruta
agent = AStarAgent(maze, start, goal)
path = agent.find_path()

# Mostrar la ruta seguida por el agente
if path:
    print("Ruta seguida por el agente:")
    for step in path:
        print(step)
else:
    print("No se pudo encontrar una ruta.")
