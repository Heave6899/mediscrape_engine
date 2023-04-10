import json
import numpy as np
import csv

stopwords = ["(finding)", "Signs and Symptoms", "Other symptoms", "Multiple symptoms", "Symptoms and Signs", ","]
substrings_to_replace = [" (symptom)",  " - symptom", " - cause unknown"]

def condition(symptom):
    for x in stopwords:
        if x.casefold() in symptom.casefold():
            return False
    return True

def well_form(symptom):
    for y in substrings_to_replace:
        symptom = symptom.replace(y, "")
    return symptom.lower().capitalize()

def getPostWiseSymptoms():
    allpostSymptoms = {}
    allSymptoms = []
    postIndex = 1
    files = ['./merged_data.json']

    for file in files:
        with open(file) as f:
            data = json.load(f)
            for obj in data:
                if 'symptoms' in obj.keys():
                    postId = obj["post_group"]
                    symptomList = obj["symptoms"]
                    if postId not in allpostSymptoms:
                        allpostSymptoms[postId] = {"index": postIndex, "symptomList": []}
                        postIndex += 1
                    for symptom in symptomList:
                        if condition(symptom):
                            symptom = well_form(symptom)
                            if symptom not in allpostSymptoms[postId]["symptomList"]:
                                allpostSymptoms[postId]["symptomList"].append(symptom)
                            if symptom not in allSymptoms:
                                allSymptoms.append(symptom)
    return allpostSymptoms, allSymptoms


def postWiseSymptomMatrix(allpostSymptoms, allSymptoms):
    postSymptomsMat = []
    for _, postInfo in allpostSymptoms.items():
        symptoms = [0]*len(allSymptoms)
        for symptomName in postInfo["symptomList"]:
            symptomMatIndex = allSymptoms.index(symptomName)
            symptoms[symptomMatIndex] += 1
        postSymptomsMat.append(symptoms)
    return postSymptomsMat


def createSympGraph(postSymptomsMat, allSymptoms):
    postSymptomsMat = np.array(postSymptomsMat)
    symptomGraphShape = (len(allSymptoms),len(allSymptoms))
    symptomGraph = np.zeros(symptomGraphShape, dtype=np.uint8)

    for postSymptoms in postSymptomsMat:
        postSymptoms = np.matrix(postSymptoms, dtype=np.uint8)
        postSymptomGraph = np.matmul(postSymptoms.transpose(), postSymptoms)
        symptomGraph += postSymptomGraph

    print(symptomGraph.shape)
    return symptomGraph

def getSymgraphEdges(symptomGraph, allSymptoms):
    symptomGraphList = symptomGraph.tolist()
    edgeList = []
    for row, _ in enumerate(symptomGraphList):
        for col in range(row + 1 ,len(symptomGraphList)):
            source = allSymptoms[row]
            dest = allSymptoms[col]
            weight = symptomGraphList[row][col]
            if weight > 1:
                edgeList.append([source, dest, weight])
    return edgeList

def writeSympGraph(edgeList):
    with open('sympgraph.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(["Source", "Target", "Weight"])
        writer.writerows(edgeList)
        writeFile.close()

if __name__ == '__main__':
    allpostSymptoms, allSymptoms = getPostWiseSymptoms()
    postSymptomsMat = postWiseSymptomMatrix(allpostSymptoms, allSymptoms)
    symptomGraph = createSympGraph(postSymptomsMat, allSymptoms)
    edgeList = getSymgraphEdges(symptomGraph, allSymptoms)
    writeSympGraph(edgeList)
    print("Successully generated Sympgraph and saved in CSV")