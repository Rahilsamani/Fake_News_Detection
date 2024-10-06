import numpy as np

class GA:
    def __init__(self, population_size=50, max_iter=100, mutation_rate=0.01):
        self.population_size = population_size
        self.max_iter = max_iter
        self.mutation_rate = mutation_rate

    def optimize(self, train_x, train_y):
        dim = train_x.shape[1]
        population = np.random.uniform(0, 1, (self.population_size, dim))

        for gen in range(self.max_iter):
            fitness = self.evaluate_fitness(population, train_x, train_y)
            parents = self.select_parents(population, fitness)
            offspring = self.crossover(parents)
            population = self.mutate(offspring)
        
        best_solution = population[np.argmax(fitness)]
        return best_solution

    def evaluate_fitness(self, population, train_x, train_y):
        # Custom fitness evaluation (placeholder)
        return np.random.rand(len(population))  # Dummy fitness

    def select_parents(self, population, fitness):
        # Roulette wheel selection
        prob = fitness / np.sum(fitness)
        return population[np.random.choice(range(len(fitness)), size=len(fitness), p=prob)]

    def crossover(self, parents):
        offspring = np.copy(parents)
        for i in range(0, len(parents), 2):
            crossover_point = np.random.randint(0, len(parents[0]))
            offspring[i, :crossover_point], offspring[i+1, :crossover_point] = \
                parents[i+1, :crossover_point], parents[i, :crossover_point]
        return offspring

    def mutate(self, offspring):
        for i in range(len(offspring)):
            for j in range(len(offspring[0])):
                if np.random.rand() < self.mutation_rate:
                    offspring[i, j] = np.random.uniform(0, 1)
        return offspring
