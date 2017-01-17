from flask import Flask
from flask_restful import Api
from resources.dns import Dns, DnsList
from common.config import CONF

app = Flask(__name__)

api_v1 = Api(app, prefix='/v1.0')
api_v1.add_resource(Dns, '/dns')
api_v1.add_resource(DnsList, '/dns/<string:zone>')


if __name__ == '__main__':
    app.run(debug=CONF.debug, host=CONF.host, port=CONF.port)
