from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import decode_token
from werkzeug.datastructures import ImmutableMultiDict
import requests
from dotenv import dotenv_values
config = dotenv_values('.env')

def token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization','No hay token')
        parts = token.split()
        if parts[0] != 'Bearer':
            return jsonify({
                'message' : 'Token esta mal formateado'
            }),401
        decoded = decode_token(parts[1])
        http_args= request.args.to_dict()
        http_args['user_id'] = decoded['sub']
        http_args['role'] = decoded['role']
        request.args = ImmutableMultiDict(http_args)
        result =  f(*args, **kwargs)
        return result
    return decorated

# def role(role):
    #     def inner_decorator(f):
    #     @wraps(f)
    #     def decorated (*args, **kwargs):
    #         try: 
    #             headers = {
    #                 "Content-Type" : "application/json"
    #             }
    #             print(role)
    #             response = requests.get(f"{config['URL_AUTH']}/api/roles/{role}", headers = headers)
    #             print(response)
    #             if response.status_code == 200:
    #                 permission = response.json()
    #                 # print(permission)
    #                 flag = False
    #                 method = request.method.lower()
    #                 print(method)
    #                 url = request.path
    #                 print(url)
    #                 for p in permission:
    #                     if p['method'].lower()== method and url ==p['url']:
    #                         flag = True
    #                         break
    #                 if flag:
    #                     result = f(*args,**kwargs)
    #                     return result
                
    #                 return jsonify({
    #                 "message" : "No tiene permisos1"
    #                 }),403                
    #         except:
    #             return jsonify({
    #                 "message":"No tiene permisos2"
    #             }),403    
    #     return decorated
    # return inner_decorator
    
def role(*roles):
    def inner_decorator(f):
        @wraps(f)
        def decorated (*args, **kwargs):
            try:
                roles_list = list(roles)
                print(roles_list)
                roles_list.index(request.args.to_dict()['role'])
                result = f(*args,**kwargs)
                print(roles_list)
                print(result)
                return result           
            except:
                return jsonify({
                    "message":"No tiene permisos"
                }),403    
        return decorated
    return inner_decorator

#video 12:04