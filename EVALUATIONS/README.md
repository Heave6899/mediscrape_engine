# Single Symptom Search Result Evaluation

| Symptom Query | Related of top k | Precision |
| :---        |    :----:   |          ---: |
| Malaise |50% |100% |
| Exhaustion |80% |100% |
| Dizziness |60% |90% |
| Cachexia |60% |100% |
| Cardiovascular problem |70% |70%|
| Pharyngeal dryness |60% |100% |
| Twitching eye |50% |50% |
| Buzzing in ear |30% |60% |
| Menopausal symptom |30% |60% |
| Pain in lumbar spine |50% |50% |
| Mucus in eyes |0% |10% |
| Cyanosis |60% |100% |
| Weight problem |10% |20% |
| Hyperextension |90% |90% |
| Difficulty standing |50% |50% |
| Hemiparesis |10% |70% |
| Constant tinnitus |60% |100% |

# Natural Language Text Search Result Evaluation

| Document Name | Related of top k | Precision |
| :---        |    :----:   |          ---: |
| 1.json |90% |100% |
| 2.json |30% |30% |
| 3.json |100% |100% | (but only return 1 mayo clinic post)
| 4.json |80% |100% |
| 5.json |80% |100% |
| 6.json |80% |90% |
| 7.json |40% |100% |

Related of top k: how many of the 10 returned output, it's main topic is relevant to input query, or the the main topic disease has the input symptom query .
Precision: how many of the 10 returned output, is related to input query.
