# Single Symptom Search Result Evaluation

| Symptom Query | Related of top k | Precision |
| :---        |    :----:   |          ---: |
| Malaise | |100% |
| Exhaustion | |100% |
| Dizziness | |90% |
| Cachexia | |100% |
| Cardiovascular problem | |70%|
| Pharyngeal dryness | |100% |
| Twitching eye | |50% |
| Buzzing in ear | |60% |
| Menopausal symptom | |60% |
| Pain in lumbar spine | |50% |
| Mucus in eyes | |10% |
| Cyanosis | |100% |
| Weight problem | |20% |
| Hyperextension | |90% |
| Difficulty standing | |50% |
| Hemiparesis | |70% |
| Constant tinnitus | |100% |

# Natural Language Text Search Result Evaluation

| Document Name | Related of top k | Precision |
| :---        |    :----:   |          ---: |
| 1.json |90% |100% |
| 2.json |30% |30% |
| 3.json |100% |100% | 
| 4.json |80% |100% |
| 5.json |80% |100% |
| 6.json |80% |90% |
| 7.json |40% |100% |

(3.json only return 1 mayo clinic post)
Related of top k: how many of the 10 returned output, it's main topic is relevant to input query.<br>
Precision: how many of the 10 returned output, is related to input query.
