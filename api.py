from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

Alunos=[
 { 
    'nome': 'julia',
    'idade': 17,
    'email': 'julia2810@gmail.com',
    'id': 1,
    'rg': '29125238850'
}
 ]

@app.route('/')
def index():
    return render_template('register.html', resultado = Alunos)

app.run(debug=True)
