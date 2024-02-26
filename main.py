from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta


app = Flask(__name__)

lista_usuarios = ['Cassiano Oliveira', 'Juliana de Santis', 'Ket Wolski Goetz', 'Alina Kovalenko', 'Angelina Mikhailichenko']

app.config['SECRET_KEY'] = 'e1fd9deaca81440cf9c4edfdbdb146f4'

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login')
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
    