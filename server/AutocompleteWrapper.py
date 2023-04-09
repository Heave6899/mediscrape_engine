from utils import Utils
class AutocompleteWrapper(object):
    def __init__(self):
        self.utils = Utils()

    def get_suggestions(self, json):
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