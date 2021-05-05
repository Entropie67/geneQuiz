import json

with open("data/json/animaux.json", "r", encoding='utf-8') as json_data:
    data_dict = json.load(json_data)
theme = data_dict["thème"]
quizz = data_dict["quizz"]['fr']
liste_questions = []
for (cle, valeur) in quizz.items():
    print(cle, valeur)
    for i in valeur:
        q = []
        question = i["question"]
        propositions = i["propositions"]
        q.append(question)
        q.extend(propositions)
        liste_questions.append(q)
        print(q)
print(liste_questions)

reponses = [
    "Staline",
    "L'Espagne",
    "Ralph Lauren"
]