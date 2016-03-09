"""
@author: Divyanshu Kakwani
@license: GPL
"""

from flask import Flask, request, make_response, redirect
from flask import render_template
from datetime import datetime
from board import add_question, getall_qs, get_question, get_answers, add_answer, get_num_ans

app = Flask(__name__)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'GET':
        return render_template('ask.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        title = request.form.get('title')
        desc = request.form.get('desc')
        add_question(title=title, desc=desc, asker=name)
        return make_response(redirect('/board'))


@app.route('/board', methods=['GET'])
def board():
    questions = getall_qs()
    answers_cnts = {q[0]: get_num_ans(q[0]) for q in questions}
    return render_template('board.html', questions=questions, answers_cnts=answers_cnts)

@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'GET':
        qid = request.args['id']
        question = get_question(qid)
        answers = get_answers(qid)
        return render_template('question.html', question=question, answers=answers)
    elif request.method == 'POST':
        qid = request.form.get('qid')
        name = request.form.get('name')
        answer = request.form.get('answer')
        add_answer(qid, answer, name)
        return make_response(redirect('/question?id='+qid))
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

