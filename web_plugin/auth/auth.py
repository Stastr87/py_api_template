# """Authorization module"""
#
# from flask import Flask
# from flask_jwt_extended import create_access_token, jwt_required
#
#
#
#
#
# # Endpoint to generate access token
# @app.route('/login', methods=['POST'])
# def login():
#     # Authenticate user (e.g., check username and password)
#     if valid_credentials:
#         access_token = create_access_token(identity=username)
#         return {'access_token': access_token}, 200
#     else:
#         return {'message': 'Invalid credentials'}, 401
#
# # Protected endpoint requiring authentication
# @app.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     return {'message': 'Access granted'}, 200
