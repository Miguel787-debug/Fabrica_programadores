# importando as bibliotecas
from flask import Flask, make_response, jsonify, request
from db import carregar_carros, salvar_carros

app = Flask(__name__) # iniciando a aplicação Flask
app.config['JSON_SORT_KEYS'] = False # desabilitando a ordenação automática das chaves JSON 

carros = carregar_carros() # carregando os dados iniciais dos carros

@app.route('/carros', methods=['GET']) # rota para obter todos os carros
def get_carros():
    return make_response(
        jsonify(mensagem="Lista de Carros", dados=carros
                ),
                )
app.route('/carros', methods=['POST']) # rota para obter um carro específico pelo ID
def add_carro():
    if carros:
        novo_id = max (c['id']for c in carros) + 1
    else:
        novo_id = 1
    carros['id'] = novo_id

    carros.append(carros)
    return make_response(
        jsonify(
            mensagem="Carro adicionado com sucesso!", 
            dados=carros
            ),201
    )
app.route('/carros/<int:id>', methods=['PUT']) # rota para obter um carro específico pelo ID
def update_carro(id):
    carro = next((c for c in carros if c['id'] == id), None)
    if not request.is_json:
        return make_response(
            jsonify(mensagem="JSON invalidado"),400)
    
    novo_carro = request.json()
    for i, carro in enumerate(carros):
        if carro.get('id') == id:
            novo_carro['id'] = id
            salvar_carros(carros)
            return make_response(
                jsonify(
                    mensagem="Carro atualizado com sucesso!", 
                    dados=novo_carro
                    )
            )
    return make_response(
        jsonify(mensagem="Carro não encontrado"),404)

@app.route('/carros/<int:id>', methods=['PATCH']) # rota para obter um carro específico pelo ID
def put_carro(id):
    if not request.is_json:
        return make_response(
            jsonify(mensagem="JSON invalidado"),400)
    dados = request.json()

