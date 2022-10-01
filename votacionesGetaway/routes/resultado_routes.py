from flask import Blueprint, jsonify, request
from controllers.resultado_controller import ResultadoController
from decorators.token_decorator import role, token
import requests

resultado_module = Blueprint("resultado",__name__)
controller = ResultadoController()

#------------Ruta para Crear-------------#

@resultado_module.post('/mesa/<string:mesa_id>/candidato/<string:candidato_id>')
@token
@role("Admin" , "Jurado")
def create_resultado(mesa_id, candidato_id):
    response, code = controller.create(request.get_json(),mesa_id, candidato_id)
    return jsonify(response), code

#------------Ruta para Modifica-------------#

@resultado_module.put('/<string:id>')
@token
@role("Admin" , "Jurado")
def update_resultado(id):
    response,code = controller.update(id,request.get_json())
    return jsonify(response),code

#------------Ruta para Eliminar-------------#

@resultado_module.delete('/<string:id>')
@token
@role("Admin" , "Jurado")
def del_resultado(id):
    controller.delete(id)
    return jsonify({}), 204

#------------Ruta para Mostrar Todo-------------#

@resultado_module.get('/')
@token
@role("Admin" , "Jurado")
def get_resultado():
    return jsonify(controller.get_all(request.args)), 200
