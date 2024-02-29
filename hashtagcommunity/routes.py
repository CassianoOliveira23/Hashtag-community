from flask import render_template, redirect, url_for, flash, request
from hashtagcommunity import app
from hashtagcommunity.forms import FormCriarConta, FormLogin
from hashtagcommunity.models import Usuario


lista_usuarios = ['Cassiano Oliveira', 'Ket Wolski Goetz', 'Alina Kovalenko', 'Angelina Mikhailichenko']

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
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=form_criarconta.senha.data)
        
        
        flash(f'Conta criada com o email: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
        
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)