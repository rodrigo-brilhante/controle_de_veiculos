from nork_town import app, db
from flask import render_template, request, redirect, session, flash, url_for
from models import Acesso, Carros, Clientes

@app.route('/')
def listar_clientes():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))
    
    clientes = Clientes.query.all()
    
    for cliente in clientes:
        cliente.qtd_carro = len(Carros.query.filter_by(id_cliente=cliente.id).all())
    
    dados = {
        'clientes':clientes,
    }
    return render_template('lista.html', dados=dados)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = Acesso.query.filter_by(login=request.form['input_login']).first()
    print(usuario)
    if usuario and usuario.senha == request.form['input_senha']:
        session['usuario_logado'] = request.form['input_login']
        return redirect(url_for("listar_clientes"))
    else:
        flash('Login invalido!')
        return redirect(url_for("login"))

@app.route('/sair')
def sair():
    session['usuario_logado'] = None
    flash('deslogado com sucesso!')
    return redirect(url_for("login"))

@app.route('/novo_cliente')
def novo_cliente():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))

    return render_template('novo_cliente.html')

@app.route('/criar_cliente', methods=['POST'])
def criar_cliente():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))
   
    nome = request.form['input_nome']
   
    cliente = Clientes.query.filter_by(nome=nome).first()
    
    if cliente:
        flash('Cliente já existe!')
        return redirect(url_for("novo_cliente"))

    novo_cliente = Clientes(nome=nome)
    db.session.add(novo_cliente)
    db.session.commit()
 
    return redirect(url_for("listar_clientes"))

@app.route('/excluir_cliente/<int:id>')
def excluir_cliente(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))
    cliente = Clientes.query.filter_by(id=id).first()
    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for("listar_clientes"))


@app.route('/remover_cliente', methods=['POST'])
def remover_cliente():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))
    nome = request.form['input_nome']
 
    return redirect(url_for("listar_clientes"))
