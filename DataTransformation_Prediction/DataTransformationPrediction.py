from datetime import datetime
from os import listdir
import pandas as pd
from application_logging.logger import App_Logger

class DataTransformPredict:
    """
    This class shall be used for transforming the Good Raw Prediction Data before processing.
    """

    def __init__(self):
        self.goodDataPath = "Prediction_Raw_Files_Validated/Good_Raw"
        self.logger = App_Logger()

    def replaceMissingWithNull(self):
        """
        Method Name: replaceMissingWithNull
        Description: This method replaces the missing values in columns with "NULL" for easier database storage.
        It processes specific columns (like 'text' for fake news) for further use.
        """
        log_file = open("Prediction_Logs/dataTransformLog.txt", 'a+')
        try:
            onlyfiles = [f for f in listdir(self.goodDataPath)]
            for file in onlyfiles:
                # Read CSV file
                csv = pd.read_csv(self.goodDataPath + "/" + file)

                # Replace missing values with 'NULL'
                csv.fillna('NULL', inplace=True)

                # Example transformation for the 'text' column
                if 'text' in csv.columns:
                    # Apply any necessary text transformations
                    csv['text'] = csv['text'].str.strip()  # Trim whitespace
                    # Additional transformations can be added here

                # Save the transformed data back to CSV
                csv.to_csv(self.goodDataPath + "/" + file, index=False, header=True)
                self.logger.log(log_file, "%s: File transformed successfully!!" % file)

        except Exception as e:
            self.logger.log(log_file, "Data transformation failed because:: %s" % e)
            raise e
        finally:
            log_file.close()


