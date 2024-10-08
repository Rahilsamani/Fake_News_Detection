import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from kneed import KneeLocator
from sklearn.feature_extraction.text import TfidfVectorizer
from file_operations import file_methods

class KMeansClustering:
    """
    This class shall be used to divide the text data into clusters before training.
    """

    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger_object = logger_object
        self.vectorizer = TfidfVectorizer()  # Using TF-IDF for text data

    def elbow_plot(self, data):
        """
        Method Name: elbow_plot
        Description: This method saves the plot to decide the optimum number of clusters to the file.
        Output: A picture saved to the directory
        On Failure: Raise Exception
        """
        self.logger_object.log(self.file_object, 'Entered the elbow_plot method of the KMeansClustering class')
        wcss = []  # initializing an empty list
        try:
            # Transform the text data into TF-IDF features
            tfidf_data = self.vectorizer.fit_transform(data['text'])  # Assuming 'text' is the column with news articles

            for i in range(1, 11):
                kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)  # initializing the KMeans object
                kmeans.fit(tfidf_data)  # fitting the TF-IDF data to the KMeans Algorithm
                wcss.append(kmeans.inertia_)
            
            plt.plot(range(1, 11), wcss)  # creating the graph between WCSS and the number of clusters
            plt.title('The Elbow Method')
            plt.xlabel('Number of clusters')
            plt.ylabel('WCSS')
            plt.savefig('preprocessing_data/K-Means_Elbow.PNG')  # saving the elbow plot locally

            # finding the value of the optimum cluster programmatically
            self.kn = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
            self.logger_object.log(self.file_object, 'The optimum number of clusters is: ' + str(self.kn.knee) + ' . Exited the elbow_plot method of the KMeansClustering class')
            return self.kn.knee

        except Exception as e:
            self.logger_object.log(self.file_object, 'Exception occurred in elbow_plot method of the KMeansClustering class. Exception message: ' + str(e))
            self.logger_object.log(self.file_object, 'Finding the number of clusters failed. Exited the elbow_plot method of the KMeansClustering class')
            raise Exception()

    def create_clusters(self, data, number_of_clusters):
        """
        Method Name: create_clusters
        Description: Create a new dataframe consisting of the cluster information.
        Output: A dataframe with cluster column
        On Failure: Raise Exception
        """
        self.logger_object.log(self.file_object, 'Entered the create_clusters method of the KMeansClustering class')
        self.data = data
        try:
            # Transform the text data into TF-IDF features
            tfidf_data = self.vectorizer.fit_transform(self.data['text'])  # Assuming 'text' is the column with news articles

            self.kmeans = KMeans(n_clusters=number_of_clusters, init='k-means++', random_state=42)
            self.y_kmeans = self.kmeans.fit_predict(tfidf_data)  # divide data into clusters

            self.file_op = file_methods.File_Operation(self.file_object, self.logger_object)
            self.save_model = self.file_op.save_model(self.kmeans, 'KMeans')  # saving the KMeans model to directory

            self.data['Cluster'] = self.y_kmeans  # create a new column in dataset for storing the cluster information
            self.logger_object.log(self.file_object, 'Successfully created ' + str(self.kn.knee) + ' clusters. Exited the create_clusters method of the KMeansClustering class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object, 'Exception occurred in create_clusters method of the KMeansClustering class. Exception message: ' + str(e))
            self.logger_object.log(self.file_object, 'Fitting the data to clusters failed. Exited the create_clusters method of the KMeansClustering class')
            raise Exception()
