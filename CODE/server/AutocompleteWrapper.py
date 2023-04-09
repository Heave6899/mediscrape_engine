from utils import Utils

class AutocompleteWrapper(object):
    """
    A class that wraps the disease-symptom utility functions provided by the Utils class.

    Attributes:
        utils (Utils): An instance of the Utils class.

    """
    def __init__(self):
        self.utils = Utils()

    def get_suggestions(self, json):
        """
        A function that returns the top 'n' diseases and symptoms that match the given query.

        Args:
            json (dict): A dictionary containing the query data.

        Returns:
            dict: A dictionary containing the top 'n' diseases and symptoms that match the given query.

        """
        print(json)
        #need to get output of diseases and symtoms whatever is detected from the sympgraph code
        # call your function take 10 symptoms, diseases
        if 'symptoms' in json:
            json['syos'] = self.utils.ranker(10,','.join(json['symptoms']))
            json['disea'] = self.utils.disease_finder(10,','.join(json['symptoms']))
        else:
            json['syos'] = []
            json['disea'] = []
        return json
