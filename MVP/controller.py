from flask import Flask, render_template, request
import modelo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('visao.html')


@app.route('/login',  methods = ["POST", "GET"])
def cadastro():
    if request.method == 'POST':
        user = request.form["user"]
        senha = request.form["password"]
        if user == '' or senha == '':
            return '<h1>Por favor, insira nome de usuario e senha!</h1>'
        else:
            pessoa = modelo.Aluno(user,senha)
            pessoa.save()
            return "<h1>Cadastro realizado com sucesso</h1>"
    
app.run()