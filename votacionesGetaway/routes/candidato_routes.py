from flask import Blueprint, jsonify, request
from controllers.candidato_controller import CandidatoController
from decorators.token_decorator import role, token
import requests

candidato_module = Blueprint("candidato",__name__)
controller = CandidatoController()

#------------Ruta para Crear-------------#

@candidato_module.post('/partido/<string:partido_id>')
@token
@role("Admin")
def create_candidato(partido_id):
    response, code = controller.create(request.get_json(),partido_id)
    return jsonify(response), code

#------------Ruta para Modifica-------------#

@candidato_module.put('/<string:id>')
@token
@role("Admin")
def update_candidato(id):
    response,code = controller.update(id,request.get_json())
    return jsonify(response),code

#------------Ruta para Eliminar-------------#

@candidato_module.delete('/<string:id>')
@token
@role("Admin")
def del_candidato(id):
    controller.delete(id)
    return jsonify({}), 204

#------------Ruta para Mostrar Todo-------------#

@candidato_module.get('/')
@token
@role("Admin")
def get_candidato():
    return jsonify(controller.get_all(request.args)), 200