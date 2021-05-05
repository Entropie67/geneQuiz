def score(reponses_donnees, reponses):
    num_question = 0
    points = 0
    for (question, rep) in reponses_donnees.items():
        print(question, rep)
        print(reponses[num_question])
        if rep == reponses[num_question]:
            points += 1
        num_question += 1

    return points, len(reponses)