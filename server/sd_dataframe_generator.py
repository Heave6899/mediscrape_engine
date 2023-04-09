import json
import pandas as pd
files = ["./merged_data.json"]

l = []
for file in files:
    with open(file) as f:
        d = json.load(f)
        for obj in d:
            if "symptoms" in obj.keys() and "diseases" in obj.keys():
                l.append({"Symptoms": tuple(obj["symptoms"]),"Diseases": tuple(obj["diseases"])})
        
df = pd.DataFrame.from_records(l)
print(df.info())
    
df.to_pickle("./sdframe.pkl")
