import shutil
import sqlite3
from datetime import datetime
from os import listdir
import os
import csv
from application_logging.logger import App_Logger

class dBOperation:
    """
    This class shall be used for handling all the SQL operations related to fake news prediction.
    """

    def __init__(self):
        self.path = 'Prediction_Database/'
        self.badFilePath = "Prediction_Raw_Files_Validated/Bad_Raw"
        self.goodFilePath = "Prediction_Raw_Files_Validated/Good_Raw"
        self.logger = App_Logger()

    def dataBaseConnection(self, DatabaseName):
        """
        Method Name: dataBaseConnection
        Description: Creates or opens the connection to the specified database.
        Output: Connection to the DB
        On Failure: Raise ConnectionError
        """
        try:
            conn = sqlite3.connect(self.path + DatabaseName + '.db')
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", 'a+')
            self.logger.log(file, "Opened %s database successfully" % DatabaseName)
            file.close()
        except ConnectionError as e:
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", 'a+')
            self.logger.log(file, "Error while connecting to database: %s" % e)
            file.close()
            raise ConnectionError
        return conn

    def createTableDb(self, DatabaseName, column_names):
        """
        Method Name: createTableDb
        Description: Creates a table in the given database for storing good prediction data.
        Output: None
        On Failure: Raise Exception
        """
        try:
            conn = self.dataBaseConnection(DatabaseName)
            conn.execute('DROP TABLE IF EXISTS Prediction_Data;')

            columns = ', '.join(['"{}" {}'.format(k, v) for k, v in column_names.items()])
            conn.execute('CREATE TABLE Prediction_Data ({})'.format(columns))

            conn.close()
            file = open("Prediction_Logs/DbTableCreateLog.txt", 'a+')
            self.logger.log(file, "Table created successfully!!")
            file.close()
        except Exception as e:
            file = open("Prediction_Logs/DbTableCreateLog.txt", 'a+')
            self.logger.log(file, "Error while creating table: %s " % e)
            file.close()
            raise e

    def insertIntoTableGoodData(self, Database):
        """
        Method Name: insertIntoTableGoodData
        Description: Inserts good prediction data files into the created database table.
        Output: None
        On Failure: Raise Exception
        """
        conn = self.dataBaseConnection(Database)
        goodFilePath = self.goodFilePath
        badFilePath = self.badFilePath
        onlyfiles = [f for f in listdir(goodFilePath)]
        log_file = open("Prediction_Logs/DbInsertLog.txt", 'a+')

        for file in onlyfiles:
            try:
                with open(goodFilePath + '/' + file, "r") as f:
                    next(f)  # Skip header
                    reader = csv.reader(f)
                    for line in reader:
                        try:
                            conn.execute('INSERT INTO Prediction_Data VALUES ({})'.format(', '.join('?' * len(line))), line)
                            self.logger.log(log_file, "%s: File loaded successfully!!" % file)
                            conn.commit()
                        except Exception as e:
                            raise e
            except Exception as e:
                conn.rollback()
                self.logger.log(log_file, "Error while inserting data from file %s: %s" % (file, e))
                shutil.move(goodFilePath + '/' + file, badFilePath)
                self.logger.log(log_file, "File Moved Successfully %s" % file)

        conn.close()
        log_file.close()

    def selectingDatafromtableintocsv(self, Database):
        """
        Method Name: selectingDatafromtableintocsv
        Description: Exports data from the Prediction_Data table to a CSV file.
        Output: None
        On Failure: Raise Exception
        """
        self.fileFromDb = 'Prediction_FileFromDB/'
        self.fileName = 'InputFile.csv'
        log_file = open("Prediction_Logs/ExportToCsv.txt", 'a+')

        try:
            conn = self.dataBaseConnection(Database)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Prediction_Data")
            results = cursor.fetchall()
            headers = [i[0] for i in cursor.description]

            # Create output directory if it doesn't exist
            if not os.path.isdir(self.fileFromDb):
                os.makedirs(self.fileFromDb)

            # Write to CSV
            with open(self.fileFromDb + self.fileName, 'w', newline='', encoding='utf-8') as csvFile:
                csvWriter = csv.writer(csvFile)
                csvWriter.writerow(headers)
                csvWriter.writerows(results)

            self.logger.log(log_file, "File exported successfully!!!")
        except Exception as e:
            self.logger.log(log_file, "File exporting failed. Error: %s" % e)
            raise e
        finally:
            conn.close()
            log_file.close()


