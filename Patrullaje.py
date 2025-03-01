import random

class PatrolAgent:
    def __init__(self, path):
        self.path = path
        self.position = 0

    def detect_obstacle(self):
        return random.choice([True, False])

    def move(self):
        if self.detect_obstacle():
            self.position = random.randint(0, len(self.path) - 1)
            print(f"🚧 Obstáculo encontrado. Cambio a {self.path[self.position]}")
        else:
            self.position = (self.position + 1) % len(self.path)
            print(f"➡️ Patrullando: {self.path[self.position]}")

# Ejecución de prueba
patrol = PatrolAgent(["Punto A", "Punto B", "Punto C", "Punto D"])
for _ in range(5):
    patrol.move()
