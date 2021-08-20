from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.submission import submission

app = Flask(__name__, static_url_path='', static_folder='frontend/dist')
CORS(app) #comment this on deployment
api = Api(app)

#Home page
@app.route("/", defaults={'path':''})
def serve(path):
    #print(path)
    return send_from_directory(app.static_folder,'index.html')

#Everything except send
@app.route("/<path>", defaults={'path':''})
def serve2(path):
    #print(path)
    return send_from_directory(app.static_folder,'index.html')

#@app.route('/<path:path>')

api.add_resource(submission, '/send')
