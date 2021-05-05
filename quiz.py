from flask import Flask, render_template, request
from data.questions import liste_questions, reponses
from application.programme import score
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', nom='Olivier', questions=liste_questions)

@app.route('/resultat', methods=['post'])
def resultat():
    reponses_utilisateurs = request.form
    points, nb = score(reponses_utilisateurs, reponses)
    r = ""
    for i in reponses_utilisateurs.items():
        r += f"<p>A la question {i[0]} vous avez répondu : {i[1]} \n</p>"
    r += f"<h3> Votre score est : {points} sur {nb}"
    return r

if __name__ == '__main__':
    app.run(debug=True)


