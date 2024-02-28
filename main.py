from flask import Flask, render_template, url_for, request, flash, redirect
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login realizado com sucesso no email: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada com o email: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
        
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
    