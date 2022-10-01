from flask import jsonify
from dotenv import dotenv_values
config = dotenv_values('.env')
import requests


class RoleController():
    
    def __init__(self) -> None:
       pass
     
    def get_all(self, data):
        headers = {
            "Content-Type": "application/json"
        }
        print(f"{config['URL_AUTH']}/api/roles/")
        response= requests.get(url=(f"{config['URL_AUTH']}/api/roles/"),json=data,headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),

    def get_by_rol(self, role):
        headers = {
      "Content-Type": "application/json"
    }
        response = requests.get(url=f"{config['URL_AUTH']}/api/roles/{role}", headers=headers)
        if response.status_code == 200:
            return response.json(), 200
        return response.json(),