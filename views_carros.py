from nork_town import app, db
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models import Carros, Carro, Clientes
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash

@app.route('/listar_carros/<int:id_cliente>')
def listar_carros(id_cliente):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))
    
    cliente = Clientes.query.filter_by(id=id_cliente).first()        
    carros = Carros.query.filter_by(id_cliente=id_cliente).all()        
    
    dados = {
        'cliente':cliente,
        'carros':carros
    }
    return render_template('lista_carros.html', dados=dados)

@app.route('/novo_carro/<int:id_cliente>')
def novo_carro(id_cliente):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))

    cliente = Clientes.query.filter_by(id=id_cliente).first()

    dados = {
        'id_cliente':cliente.id,
        'nome_cliente':cliente.nome,
        'cores': Carro.COR,
        'modelos': Carro.MODELOS,
    }
    return render_template('novo_carro.html',dados=dados)

@app.route('/adionar_carro', methods=['POST'])
def adionar_carro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))

    id_cliente = request.form['id_cliente']
    cor = request.form['select_cor']
    modelo = request.form['select_modelo']
    
    carros = Carros.query.filter_by(id_cliente=id_cliente).all()

    if len(carros) >= 3:
        flash('Limete de carros atingido!')
        return redirect(url_for("novo_carro", id_cliente=id_cliente))
    
    novo_carro = Carros(id_cliente=id_cliente, cor=cor, modelo=modelo)
    db.session.add(novo_carro)
    db.session.commit()
   
    return redirect(url_for("listar_clientes"))

@app.route('/editar_carro/<int:id_carro>/<int:id_cliente>')
def editar_carro(id_carro, id_cliente):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))

    cliente = Clientes.query.filter_by(id=id_cliente).first()
    carro = Carros.query.filter_by(id=id_carro).first()

    dados = {
        'id_cliente':cliente.id,
        'nome_cliente':cliente.nome,
        'cores': Carro.COR,
        'modelos': Carro.MODELOS,
        'carro':carro
    }
    return render_template('editar_carro.html',dados=dados)

@app.route('/alterar_carro', methods=['POST'])
def alterar_carro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))

    id_cliente = request.form['id_cliente']
    id_carro = request.form['id_carro']
    cor = request.form['select_cor']
    modelo = request.form['select_modelo']

    carro = Carros.query.filter_by(id=id_carro).first()

    carro.cor = cor
    carro.modelo = modelo

    db.session.commit()

    return redirect(url_for("listar_carros", id_cliente=id_cliente ))


@app.route('/excluir_carro/<int:id_carro>/<int:id_cliente>')
def excluir_carro(id_carro, id_cliente):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for("login"))

    carro = Carros.query.filter_by(id=id_carro).first()
    db.session.delete(carro)
    db.session.commit()

    return redirect(url_for("listar_carros", id_cliente=id_cliente ))

