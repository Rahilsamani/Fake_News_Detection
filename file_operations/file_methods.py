import pickle
import os
import shutil


class File_Operation:
    """
    This class shall be used to save the trained model for fake news detection
    and load the saved model for making predictions.
    """
    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger_object = logger_object
        self.model_directory = 'models/'

    def save_model(self, model, filename):
        """
        Method Name: save_model
        Description: Save the model file to the directory.
        Outcome: File gets saved.
        On Failure: Raise Exception.
        """
        self.logger_object.log(self.file_object, 'Entered the save_model method of the File_Operation class')
        try:
            path = os.path.join(self.model_directory, filename)  # Create a separate directory for each model
            if os.path.isdir(path):  # Remove previously existing models for each cluster
                shutil.rmtree(path)
            os.makedirs(path)  # Create new directory for the model

            with open(os.path.join(path, filename + '.sav'), 'wb') as f:
                pickle.dump(model, f)  # Save the model to file

            self.logger_object.log(self.file_object,
                                   'Model File ' + filename + ' saved. Exited the save_model method of the File_Operation class')
            return 'success'
        except Exception as e:
            self.logger_object.log(self.file_object, 'Exception occurred in save_model method of the File_Operation class. Exception message: ' + str(e))
            raise Exception()

    def load_model(self, filename):
        """
        Method Name: load_model
        Description: Load the model file into memory.
        Output: The Model file loaded in memory.
        On Failure: Raise Exception.
        """
        self.logger_object.log(self.file_object, 'Entered the load_model method of the File_Operation class')
        try:
            with open(os.path.join(self.model_directory, filename, filename + '.sav'), 'rb') as f:
                self.logger_object.log(self.file_object,
                                       'Model File ' + filename + ' loaded. Exited the load_model method of the File_Operation class')
                return pickle.load(f)
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occurred in load_model method of the File_Operation class. Exception message: ' + str(e))
            raise Exception()

    def find_correct_model_file(self):
        """
        Method Name: find_correct_model_file
        Description: Find the correct model file based on its name.
        Output: The Model file.
        On Failure: Raise Exception.
        """
        self.logger_object.log(self.file_object, 'Entered the find_correct_model_file method of the File_Operation class')
        try:
            self.list_of_model_files = os.listdir(self.model_directory)
            self.model_name = None

            # Identify the appropriate model file (if naming convention indicates the model)
            for model_file in self.list_of_model_files:
                if model_file.endswith('.sav'):
                    self.model_name = model_file.split('.')[0]  # Extract model name without extension
                    break

            if not self.model_name:
                raise Exception("No model file found.")

            self.logger_object.log(self.file_object,
                                   'Exited the find_correct_model_file method of the File_Operation class.')
            return self.model_name
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occurred in find_correct_model_file method of the File_Operation class. Exception message: ' + str(e))
            raise Exception()


