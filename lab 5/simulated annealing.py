import random
import math

def objective(x):
    return (x - 3) ** 2

def simulated_annealing():
    current = random.uniform(-10, 10)
    best = current

    temperature = 100
    cooling_rate = 0.95
    min_temperature = 0.001

    while temperature > min_temperature:
        neighbor = current + random.uniform(-1, 1)

        delta = objective(neighbor) - objective(current)

        if delta < 0:
            current = neighbor
        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                current = neighbor

        if objective(current) < objective(best):
            best = current

        temperature *= cooling_rate

    return best

result = simulated_annealing()

print("Best Solution:", result)
print("Minimum Value:", objective(result))

