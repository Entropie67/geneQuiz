from flask import Flask, render_template, request
from data.questions import liste_questions
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', nom='Olivier', questions=liste_questions)

@app.route('/resultat', methods=['post'])
def resultat():
    reponses = request.form
    r = ""
    for i in reponses.items():
        r += f"<p>A la question {i[0]} il a répondu : {i[1]} \n</p>"
    return r

if __name__ == '__main__':
    app.run(debug=True)


