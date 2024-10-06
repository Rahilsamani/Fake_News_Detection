import numpy as np

class ACO:
    def __init__(self, n_ants=20, max_iter=100, alpha=1.0, beta=2.0, evaporation_rate=0.5):
        self.n_ants = n_ants
        self.max_iter = max_iter
        self.alpha = alpha  # Pheromone importance
        self.beta = beta    # Heuristic importance
        self.evaporation_rate = evaporation_rate  # Evaporation rate of pheromones

    def optimize(self, train_x, train_y, fitness_func):
        dim = train_x.shape[1]
        pheromone = np.ones((dim, dim))  # Pheromone matrix
        best_solution = None
        best_fitness = -np.inf

        for iteration in range(self.max_iter):
            all_solutions = []
            for ant in range(self.n_ants):
                solution = self.construct_solution(pheromone, dim)
                all_solutions.append(solution)
            
            fitness_values = np.array([fitness_func(sol, train_x, train_y) for sol in all_solutions])
            if max(fitness_values) > best_fitness:
                best_fitness = max(fitness_values)
                best_solution = all_solutions[np.argmax(fitness_values)]

            self.update_pheromone(pheromone, all_solutions, fitness_values)
            pheromone *= (1 - self.evaporation_rate)  # Evaporation

        return best_solution, best_fitness

    def construct_solution(self, pheromone, dim):
        solution = np.zeros(dim)
        for i in range(dim):
            prob = (pheromone[i] ** self.alpha) / (np.sum(pheromone[i]) ** self.beta)
            solution[i] = np.random.choice(np.arange(0, 1, 1/dim), p=prob)
        return solution

    def update_pheromone(self, pheromone, solutions, fitness_values):
        for i in range(len(solutions)):
            pheromone += fitness_values[i] * solutions[i]
