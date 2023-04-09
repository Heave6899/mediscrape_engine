import json
import pandas as pd

# Define the file(s) to load
files = ["./merged_data.json"]

# Create an empty list to store the symptom-disease pairs
l = []

# Loop through each file and extract the symptom-disease pairs
for file in files:
    with open(file) as f:
        # Load the JSON data from the file
        d = json.load(f)
        # Loop through each object in the JSON data
        for obj in d:
            # Check if the object contains both symptoms and diseases
            if "symptoms" in obj.keys() and "diseases" in obj.keys():
                # Append a tuple of symptoms and diseases to the list
                l.append({"Symptoms": tuple(obj["symptoms"]),"Diseases": tuple(obj["diseases"])})

# Convert the list of symptom-disease pairs to a pandas DataFrame
df = pd.DataFrame.from_records(l)

# Print information about the DataFrame
print(df.info())

# Save the DataFrame as a pickle file
df.to_pickle("./sdframe.pkl")
