import shutil
import sqlite3
from datetime import datetime
from os import listdir
import os
import csv
from application_logging.logger import App_Logger


class dBOperation:
    """
      This class shall be used for handling all the SQL operations related to fake news detection.
    """

    def __init__(self):
        self.path = 'Training_Database/'
        self.badFilePath = "Training_Raw_Files_Validated/Bad_Raw"
        self.goodFilePath = "Training_Raw_Files_Validated/Good_Raw"
        self.logger = App_Logger()

    def dataBaseConnection(self, DatabaseName):
        """
                Method Name: dataBaseConnection
                Description: This method creates the database with the given name and if Database already exists then opens the connection to the DB.
                Output: Connection to the DB
                On Failure: Raise ConnectionError
        """
        try:
            conn = sqlite3.connect(self.path + DatabaseName + '.db')
            file = open("Training_Logs/DataBaseConnectionLog.txt", 'a+')
            self.logger.log(file, "Opened %s database successfully" % DatabaseName)
            file.close()
        except ConnectionError:
            file = open("Training_Logs/DataBaseConnectionLog.txt", 'a+')
            self.logger.log(file, "Error while connecting to database: %s" % ConnectionError)
            file.close()
            raise ConnectionError
        return conn

    def createTableDb(self, DatabaseName, column_names):
        """
                Method Name: createTableDb
                Description: This method creates a table in the given database for storing validated training data.
                Output: None
                On Failure: Raise Exception
        """
        try:
            conn = self.dataBaseConnection(DatabaseName)
            c = conn.cursor()
            c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Good_Raw_Data'")
            if c.fetchone()[0] == 1:
                conn.close()
                file = open("Training_Logs/DbTableCreateLog.txt", 'a+')
                self.logger.log(file, "Table 'Good_Raw_Data' already exists.")
                file.close()
                return

            for key, data_type in column_names.items():
                try:
                    conn.execute('ALTER TABLE Good_Raw_Data ADD COLUMN "{column_name}" {dataType}'.format(column_name=key, dataType=data_type))
                except:
                    conn.execute('CREATE TABLE Good_Raw_Data ({column_name} {dataType})'.format(column_name=key, dataType=data_type))

            conn.close()

            file = open("Training_Logs/DbTableCreateLog.txt", 'a+')
            self.logger.log(file, "Table 'Good_Raw_Data' created successfully!!")
            file.close()

        except Exception as e:
            file = open("Training_Logs/DbTableCreateLog.txt", 'a+')
            self.logger.log(file, "Error while creating table: %s" % e)
            file.close()
            conn.close()
            raise e

    def insertIntoTableGoodData(self, Database):
        """
                Method Name: insertIntoTableGoodData
                Description: This method inserts the good data files from the Good_Raw folder into the database.
                Output: None
                On Failure: Raise Exception
        """
        conn = self.dataBaseConnection(Database)
        goodFilePath = self.goodFilePath
        badFilePath = self.badFilePath
        onlyfiles = [f for f in listdir(goodFilePath)]
        log_file = open("Training_Logs/DbInsertLog.txt", 'a+')

        for file in onlyfiles:
            try:
                with open(goodFilePath + '/' + file, "r") as f:
                    next(f)  # Skip header
                    reader = csv.reader(f)
                    for line in reader:
                        try:
                            conn.execute('INSERT INTO Good_Raw_Data VALUES ({values})'.format(values=','.join(line)))
                            self.logger.log(log_file, "%s: File loaded successfully!!" % file)
                            conn.commit()
                        except Exception as e:
                            raise e
            except Exception as e:
                conn.rollback()
                self.logger.log(log_file, "Error while inserting data: %s" % e)
                shutil.move(goodFilePath + '/' + file, badFilePath)
                self.logger.log(log_file, "File moved to Bad_Raw: %s" % file)

        conn.close()
        log_file.close()

    def selectingDatafromtableintocsv(self, Database):
        """
                Method Name: selectingDatafromtableintocsv
                Description: This method exports the data in the Good_Raw_Data table as a CSV file.
                Output: None
                On Failure: Raise Exception
        """
        self.fileFromDb = 'Training_FileFromDB/'
        self.fileName = 'InputFile.csv'
        log_file = open("Training_Logs/ExportToCsv.txt", 'a+')
        try:
            conn = self.dataBaseConnection(Database)
            sqlSelect = "SELECT * FROM Good_Raw_Data"
            cursor = conn.cursor()
            cursor.execute(sqlSelect)
            results = cursor.fetchall()

            # Get the headers of the CSV file
            headers = [i[0] for i in cursor.description]

            # Make the CSV output directory
            if not os.path.isdir(self.fileFromDb):
                os.makedirs(self.fileFromDb)

            # Open CSV file for writing.
            with open(self.fileFromDb + self.fileName, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                # Add the headers and data to the CSV file.
                csv_writer.writerow(headers)
                csv_writer.writerows(results)

            self.logger.log(log_file, "File exported successfully!!!")

        except Exception as e:
            self.logger.log(log_file, "File exporting failed. Error: %s" % e)

        log_file.close()


