from flask import Blueprint, jsonify, request
from controllers.mesa_controller import MesaController
from decorators.token_decorator import role, token
import requests

mesa_module = Blueprint("mesa",__name__)
controller = MesaController()

#------------Ruta para Crear-------------#

@mesa_module.post('/')
@token
@role("Admin")
def create_mesa():
    response, code = controller.create(request.get_json())
    return jsonify(response), code

#------------Ruta para Modifica-------------#

@mesa_module.put('/<string:id>')
@token
@role("Admin")
def update_mesa(id):
    response,code = controller.update(id,request.get_json())
    return jsonify(response),code

#------------Ruta para Eliminar-------------#

@mesa_module.delete('/<string:id>')
@token
@role("Admin")
def del_mesa(id):
    controller.delete(id)
    return jsonify({}), 204

#------------Ruta para Mostrar Todo-------------#

@mesa_module.get('/')
@token
@role("Admin")
def get_mesa():
    return jsonify(controller.get_all(request.args)), 200