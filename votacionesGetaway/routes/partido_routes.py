from flask import Blueprint, jsonify, request
from controllers.partido_controller import PartidoController
from decorators.token_decorator import role, token
import requests

partido_module = Blueprint("partido",__name__)
controller = PartidoController()

#------------Ruta para Crear-------------#

@partido_module.post('/')
@token
@role("Admin")
def create():
    response, code = controller.create(request.get_json())
    return jsonify(response), code

#------------Ruta para Modifica-------------#

@partido_module.put('/<string:id>')
@token
@role("Admin")
def update_partido(id):
    response,code = controller.update(id,request.get_json())
    return jsonify(response),code

#------------Ruta para Eliminar-------------#

@partido_module.delete('/<string:id>')
@token
@role("Admin")
def del_partido(id):
    controller.delete(id)
    return jsonify({}), 204

#------------Ruta para Mostrar Todo-------------#

@partido_module.get('/')
@token
@role("Admin")
def get_partido():
    return jsonify(controller.get_all(request.args)), 200