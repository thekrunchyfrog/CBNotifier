from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from GetOnlineModels import GetOnlineModels

app = Flask(__name__)


@app.route('/models/followed/online', methods=['POST'])
def api_echo():

    if request.headers['Content-Type'] == 'application/json':
        username = request.json['username']
        password = request.json['password']
        resp = jsonify(GetOnlineModels().myModels(username, password))
        resp.status_code = 201
        resp.headers['server'] = ""
        return resp

    else:
        resp = Response("Try Again :-(", status=200, mimetype='text/plain')
        resp.status_code = 415
        resp.headers['server'] = ""
        return resp


if __name__ == '__main__':
    app.run()
