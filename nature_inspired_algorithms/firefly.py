import numpy as np

class FireflyAlgorithm:
    def __init__(self, n_fireflies=20, max_iter=100, alpha=0.5, beta_min=0.2, gamma=1.0):
        self.n_fireflies = n_fireflies
        self.max_iter = max_iter
        self.alpha = alpha  # Randomness factor
        self.beta_min = beta_min  # Attraction factor
        self.gamma = gamma  # Absorption coefficient (light intensity)

    def optimize(self, train_x, train_y, fitness_func):
        dim = train_x.shape[1]
        fireflies = np.random.uniform(0, 1, (self.n_fireflies, dim))  # Initial population
        light_intensity = np.array([fitness_func(f, train_x, train_y) for f in fireflies])
        best_solution = fireflies[np.argmax(light_intensity)]
        best_fitness = max(light_intensity)

        for iteration in range(self.max_iter):
            for i in range(self.n_fireflies):
                for j in range(self.n_fireflies):
                    if light_intensity[i] < light_intensity[j]:
                        r = np.linalg.norm(fireflies[i] - fireflies[j])  # Distance between fireflies
                        beta = self.beta_min * np.exp(-self.gamma * r**2)  # Attraction formula
                        fireflies[i] += beta * (fireflies[j] - fireflies[i]) + \
                                        self.alpha * (np.random.uniform(0, 1, dim) - 0.5)
                        fireflies[i] = np.clip(fireflies[i], 0, 1)  # Keep within bounds

