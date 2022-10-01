from dotenv import dotenv_values
import requests
config = dotenv_values('.env')

class MesaController():
    def __init__(self):
        pass

#------------Accion para Crear-------------#
    
    def create (self, data):
        headers={
            "Content-Type":"application/json"
        }
        response = requests.post(url=f"{config['URL_VOTACIONES']}/mesa/",json=data, headers=headers)
        if response.status_code == 201:
            return response.json(),201
        return ({"message": "error"}), 400
    
#------------Accion para Modificar-------------#
    
    def update(self,id,data):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.put(url=f"{config['URL_VOTACIONES']}/mesa/{id}",json=data, headers=headers)
        if response.status_code == 204:
            return {}, 204
        return {}, 400

#------------Accion para Eliminar-------------#
    
    def delete(self,id):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.delete(url=f"{config['URL_VOTACIONES']}/mesa/{id}", headers=headers)
        if response.status_code == 204:
            return {"mesa eliminado"}, 204
        return {"No se encontro un usuario con ese ID"}, 400

#------------Accion para Mostrar Todos-------------#

    def get_all(self, data):
        headers = {
            "Content-Type": "application/json"
        }
        response= requests.get(url=(f"{config['URL_VOTACIONES']}/mesa/"),json=data,headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json() 
