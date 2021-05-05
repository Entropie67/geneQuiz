import json

with open("json/animaux.json", "r", encoding='utf-8') as json_data:
    data_dict = json.load(json_data)
    print(data_dict)
theme = data_dict["thème"]
quizz = data_dict["quizz"]['fr']

print(theme, quizz)