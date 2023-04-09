import pandas as pd

class Utils:
    def __init__(self, path = "./sympgraph.csv"):
        self.df = pd.read_csv(path, encoding = "latin-1")
        self.query_table = self.df["Source"].values

    def ranker(self, top, query):
        query = query.split(",")
        if len(query) > 1:
            query = [i for i in query if i in self.query_table]
            filter_df = self.df[self.df["Source"].isin(query)]
        elif len(query) == 1:
            if query[0] not in self.query_table:
                return "Invalid Query -- Try again"
            filter_df = self.df[self.df["Source"] == query[0]]
        else:
            return "Empty Query -- Try again"
        
        filter_df = filter_df[~filter_df["Target"].isin(query)]
        filter_df = filter_df.sort_values("Weight", ascending = False)
        filter_df.drop_duplicates(subset = ["Target"], inplace = True)
        
        return filter_df["Target"][:top].to_list()
    
    def disease_finder(self, top, query):
        query = set(query.split(","))
        df = pd.read_pickle("sdframe.pkl").to_dict("records")
        queue = []
        maxx = 0
        for row in df:
            if len(query.intersection(row['Symptoms'])) > maxx:
                maxx = len(query.intersection(row['Symptoms']))
                queue.extend(row['Diseases'])
                queue = list(set(queue))
                while len(queue) > top:
                    queue.pop(0)
        return queue
