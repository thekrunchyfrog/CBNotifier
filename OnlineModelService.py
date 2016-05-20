from flask import Flask
from flask import request
from GetOnlineModels import GetOnlineModels
import json

app = Flask(__name__)


@app.route('/echo', methods=['POST'])
def api_echo():

    if request.headers['Content-Type'] == 'application/json':
        username = request.json['username']
        password = request.json['password']
        print username + ' ' + password
        x = GetOnlineModels()
        y = x.myModels(username, password)
        return json.dumps(y)

    else:
        return "415 Unsupported Media Type"


if __name__ == '__main__':
    app.run()
