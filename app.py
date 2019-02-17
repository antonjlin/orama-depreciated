from flask import Flask
from flask import jsonify
from flask import request
from flask import logging
import os
from models.user import User
from controllers.mongo import *

app = Flask(__name__, static_url_path='/static')


@app.route('/api/users/login', methods=['POST'])
def apiLogin():
    data = request.get_json()
    user = User(email=data.get('email'), password=data.get('password'),faceHash='')
    authenticated,userData = authenticateUser(user)
    return jsonify({
        'authenticated': authenticated,
        'user':userData
    })

@app.route('/api/users/create', methods=['POST'])
def apiCreateUser():
    try:
        data = request.get_json()
        user = User(email=data.get('email'), password=data.get('password'),faceHash='')
        return jsonify({
            'success':True,
            'uid':createUser(user),
        })
    except Exception as e:
        return jsonify({
            'success':False,
            'error':str(e),
        })

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    port = os.environ.get('PORT') or 5000
    print(f"Starting server on port {port}")
    app.run(host="0.0.0.0", port=port)
