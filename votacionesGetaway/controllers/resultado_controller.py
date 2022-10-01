from dotenv import dotenv_values
import requests
config = dotenv_values('.env')

class ResultadoController():
    def __init__(self):
        pass

#------------Accion para Crear-------------#
    
    def create (self, data, mesa_id, candidato_id):
        headers={
            "Content-Type":"application/json"
        }
        response = requests.post(url=f"{config['URL_VOTACIONES']}/resultado/mesa/{mesa_id}/candidato/{candidato_id}",json=data, headers=headers)
        if response.status_code == 201:
            return response.json(),201
        return ({"message": "error"}), 400
    
#------------Accion para Modificar-------------#
    
    def update(self,id,data):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.put(url=f"{config['URL_VOTACIONES']}/resultado/{id}",json=data, headers=headers)
        if response.status_code == 204:
            return {}, 204
        return {}, 400

#------------Accion para Eliminar-------------#
    
    def delete(self,id):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.delete(url=f"{config['URL_VOTACIONES']}/resultado/{id}", headers=headers)
        if response.status_code == 204:
            return {"candidato eliminado"}, 204
        return {"No se encontro un usuario con ese ID"}, 400

#------------Accion para Mostrar Todos-------------#

    def get_all(self, data):
        headers = {
            "Content-Type": "application/json"
        }
        response= requests.get(url=(f"{config['URL_VOTACIONES']}/resultado/"),json=data,headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 
