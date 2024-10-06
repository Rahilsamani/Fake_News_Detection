from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from nature_inspired_algorithms import GWO, PSO, GA, ACO, Firefly # Placeholder for imported algorithms

class Model_Finder_NatureInspired:
    """
        This class is designed to find the best model using Nature-Inspired algorithms such as:
        - Grey Wolf Optimizer (GWO) + Particle Swarm Optimization (PSO)
        - Genetic Algorithm (GA)
        - Ant Colony Optimization (ACO)
        - Firefly Algorithm
    """

    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger_object = logger_object
        # Initialize nature-inspired algorithms
        self.gwo = GWO()
        self.pso = PSO()
        self.ga = GA()
        self.aco = ACO()
        self.firefly = Firefly()

    def get_best_params_for_gwo_pso(self, train_x, train_y):
        """
        Method to optimize parameters using Grey Wolf Optimizer (GWO) and Particle Swarm Optimization (PSO).
        """
        self.logger_object.log(self.file_object, 'Entered the get_best_params_for_gwo_pso method of the Model_Finder_NatureInspired class')
        try:
            # Apply GWO to find optimal hyperparameters
            gwo_best_params = self.gwo.optimize(train_x, train_y)
            self.logger_object.log(self.file_object, 'GWO best params: ' + str(gwo_best_params))

            # Use the GWO parameters to further optimize with PSO
            pso_best_params = self.pso.optimize(train_x, train_y, gwo_best_params)
            self.logger_object.log(self.file_object, 'PSO best params after GWO: ' + str(pso_best_params))

            # Train the final model with optimized parameters (assuming the model to be optimized is something like SVM or Logistic Regression)
            self.model = SomeMLModel(**pso_best_params)  # Placeholder for actual model
            self.model.fit(train_x, train_y)
            return self.model
        except Exception as e:
            self.logger_object.log(self.file_object, f"Exception in get_best_params_for_gwo_pso: {str(e)}")
            raise Exception()

    def get_best_params_for_ga(self, train_x, train_y):
        """
        Method to optimize model parameters using Genetic Algorithm (GA).
        """
        self.logger_object.log(self.file_object, 'Entered the get_best_params_for_ga method of the Model_Finder_NatureInspired class')
        try:
            # Apply Genetic Algorithm to find the optimal parameters
            ga_best_params = self.ga.optimize(train_x, train_y)
            self.logger_object.log(self.file_object, 'GA best params: ' + str(ga_best_params))

            # Train the final model with optimized parameters
            self.model = SomeMLModel(**ga_best_params)  # Placeholder for actual model
            self.model.fit(train_x, train_y)
            return self.model
        except Exception as e:
            self.logger_object.log(self.file_object, f"Exception in get_best_params_for_ga: {str(e)}")
            raise Exception()

    def get_best_params_for_aco(self, train_x, train_y):
        """
        Method to optimize model parameters using Ant Colony Optimization (ACO).
        """
        self.logger_object.log(self.file_object, 'Entered the get_best_params_for_aco method of the Model_Finder_NatureInspired class')
        try:
            # Apply ACO to find the optimal parameters
            aco_best_params = self.aco.optimize(train_x, train_y)
            self.logger_object.log(self.file_object, 'ACO best params: ' + str(aco_best_params))

            # Train the final model with optimized parameters
            self.model = SomeMLModel(**aco_best_params)  # Placeholder for actual model
            self.model.fit(train_x, train_y)
            return self.model
        except Exception as e:
            self.logger_object.log(self.file_object, f"Exception in get_best_params_for_aco: {str(e)}")
            raise Exception()

    def get_best_params_for_firefly(self, train_x, train_y):
        """
        Method to optimize model parameters using Firefly Algorithm.
        """
        self.logger_object.log(self.file_object, 'Entered the get_best_params_for_firefly method of the Model_Finder_NatureInspired class')
        try:
            # Apply Firefly Algorithm to find the optimal parameters
            firefly_best_params = self.firefly.optimize(train_x, train_y)
            self.logger_object.log(self.file_object, 'Firefly best params: ' + str(firefly_best_params))

            # Train the final model with optimized parameters
            self.model = SomeMLModel(**firefly_best_params)  # Placeholder for actual model
            self.model.fit(train_x, train_y)
            return self.model
        except Exception as e:
            self.logger_object.log(self.file_object, f"Exception in get_best_params_for_firefly: {str(e)}")
            raise Exception()

    def get_best_model(self, train_x, train_y, test_x, test_y):
        """
        Find the best model by comparing AUC scores from different Nature-Inspired algorithms.
        """
        self.logger_object.log(self.file_object, 'Entered the get_best_model method of the Model_Finder_NatureInspired class')
        try:
            # Optimize models using different nature-inspired algorithms
            model_gwo_pso = self.get_best_params_for_gwo_pso(train_x, train_y)
            model_ga = self.get_best_params_for_ga(train_x, train_y)
            model_aco = self.get_best_params_for_aco(train_x, train_y)
            model_firefly = self.get_best_params_for_firefly(train_x, train_y)

            # Evaluate models on the test set
            models = [model_gwo_pso, model_ga, model_aco, model_firefly]
            best_model = None
            best_score = 0

            for model in models:
                predictions = model.predict(test_x)
                if len(test_y.unique()) == 1:  # if there is only one label in y
                    score = accuracy_score(test_y, predictions)
                else:
                    score = roc_auc_score(test_y, predictions)
                
                if score > best_score:
                    best_score = score
                    best_model = model

            self.logger_object.log(self.file_object, f"Best model selected with score: {best_score}")
            return best_model

        except Exception as e:
            self.logger_object.log(self.file_object, f"Exception in get_best_model: {str(e)}")
            raise Exception()
