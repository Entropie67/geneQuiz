from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    question = ["Quelle est la couleur du chat ?", "rouge", "violet", "orange", "bleu"]
    question2 = ["Quel est l'age du chat ?", 45, 3, 273, 1]
    liste_questions = [question, question2]
    return render_template('index.html', nom='Olivier', questions=liste_questions)


if __name__ == '__main__':
    app.run(debug=True)


