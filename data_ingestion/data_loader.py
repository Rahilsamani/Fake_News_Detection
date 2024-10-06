import pandas as pd
import requests
from bs4 import BeautifulSoup

class Data_Getter:
    """
    This class shall be used for obtaining the data from the source for training.
    """
    def __init__(self, file_object, logger_object, source_type='file', source='Training_FileFromDB/InputFile.csv'):
        """
        Initializes the Data_Getter class.

        :param file_object: The file object for logging.
        :param logger_object: The logger object for logging.
        :param source_type: Type of the data source ('file' or 'url').
        :param source: Path to the input file or URL.
        """
        self.source_type = source_type
        self.source = source
        self.file_object = file_object
        self.logger_object = logger_object

    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from the specified source (file or URL).
        Output: A pandas DataFrame.
        On Failure: Raise Exception
        """
        self.logger_object.log(self.file_object, 'Entered the get_data method of the Data_Getter class')
        try:
            if self.source_type == 'file':
                # Reading data from a CSV file
                self.data = pd.read_csv(self.source)  # Reading the data file
            elif self.source_type == 'url':
                # Reading data from a URL
                response = requests.get(self.source)
                if response.status_code == 200:
                    # Use BeautifulSoup to parse the HTML and extract text content
                    soup = BeautifulSoup(response.content, 'html.parser')
                    paragraphs = soup.find_all('p')
                    text = ' '.join([para.get_text() for para in paragraphs])
                    # Create a DataFrame from the text with a placeholder label (for supervised learning)
                    self.data = pd.DataFrame({'text': [text], 'label': [None]})  # Adjust label as needed
                else:
                    raise Exception(f'Failed to retrieve data from URL: {self.source}')

            self.logger_object.log(self.file_object, 'Data Load Successful. Exited the get_data method of the Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object, 'Exception occurred in get_data method of the Data_Getter class. Exception message: ' + str(e))
            self.logger_object.log(self.file_object, 'Data Load Unsuccessful. Exited the get_data method of the Data_Getter class')
            raise Exception()

