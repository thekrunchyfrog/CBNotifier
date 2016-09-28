from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from flask import Response
from GatherData import GatherData

app = Flask(__name__)


@app.route('/models/followed/online', methods=['POST'])
def api_ModelsFollowedOnline():

    if request.headers['Content-Type'] == 'application/json':
        username = request.json['username']
        password = request.json['password']
        resp = jsonify(GatherData().getOnlineFollowedModels(username, password))
        resp.status_code = 201
        resp.headers['server'] = ""
        return resp

    else:
        resp = Response("Try Again :-(", status=415, mimetype='text/plain')
        resp.headers['server'] = ""
        return resp


@app.route('/models/followed', methods=["POST"])
def api_ModelsFollowed():

    if request.headers['Content-Type'] == 'application/json':
        username = request.json['username']
        password = request.json['password']
        resp = jsonify(GatherData().getAllFollowedModels(username, password))
        resp.status_code = 201
        resp.headers['server'] = ""
        return resp

    else:
        resp = Response("Try Again :-(", status=415, mimetype='text/plain')
        resp.headers['server'] = ""
        return resp


@app.route('/models/info', methods=["POST"])
def api_ModelsInfo():

    if request.headers['Content-Type'] == 'application/json':
        modelName = request.json['modelName']
        resp = jsonify(GatherData().getModelInfo(modelName))
        resp.status_code = 201
        resp.headers['server'] = ""
        return resp

    else:
        resp = Response("Try Again :-(", status=415, mimetype='text/plain')
        resp.headers['server'] = ""
        return resp


@app.route('/models/featured', methods=["GET"])
def api_ModelsFeatured():

    resp = jsonify(GatherData().getFeatured())
    resp.status_code = 201
    resp.headers['server'] = ""
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run()
