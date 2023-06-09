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
        # print(json)
        # need to get output of diseases and symtoms whatever is detected from the sympgraph code
        # call your function take 10 symptoms, diseases
        if 'symptoms' in json:
            outsyos = self.utils.ranker(10,','.join(json['symptoms']))
            outdisea = self.utils.disease_finder(10, ','.join(json['symptoms']))
            json['syos'] = outsyos if type(outsyos) is list else []
            json['disea'] = outdisea if type(outdisea) is list else []
        else:
            outsyos = self.utils.ranker(10, json['text'])
            outdisea = self.utils.disease_finder(10, json['text'])
            json['syos'] = outsyos if type(outsyos) is list else []
            json['disea'] = outdisea if type(outdisea) is list else []
        return json
