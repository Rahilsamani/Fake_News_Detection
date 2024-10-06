from datetime import datetime
from os import listdir
import pandas as pd
from application_logging.logger import App_Logger

class DataTransform:
    """
    This class shall be used for transforming the Good Raw Training Data before loading it into the database.
    """

    def __init__(self):
        self.goodDataPath = "Training_Raw_files_validated/Good_Raw"
        self.logger = App_Logger()

    def replaceMissingWithNull(self):
        """
        Method Name: replaceMissingWithNull
        Description: This method replaces the missing values in columns with "NULL" for database storage.
        Also, processes specific columns (like 'text' for fake news) for further use.
        """
        log_file = open("Training_Logs/dataTransformLog.txt", 'a+')
        try:
            onlyfiles = [f for f in listdir(self.goodDataPath)]
            for file in onlyfiles:
                # Read CSV file
                csv = pd.read_csv(self.goodDataPath + "/" + file)
                
                # Replace missing values with 'NULL'
                csv.fillna('NULL', inplace=True)

                # If there are specific transformations required, add them here
                # Example: if you have a 'text' column and you want to apply some transformations
                if 'text' in csv.columns:
                    # Here you could add text-specific transformations, e.g. cleaning or formatting
                    csv['text'] = csv['text'].str.strip()  # Example: trim whitespace

                # Save the transformed data back to CSV
                csv.to_csv(self.goodDataPath + "/" + file, index=False, header=True)
                self.logger.log(log_file, "%s: File transformed successfully!!" % file)

        except Exception as e:
            self.logger.log(log_file, "Data transformation failed because:: %s" % e)
        finally:
            log_file.close()

