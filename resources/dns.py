import json
from flask_restful import Resource, reqparse
from common.dns import add_dns, del_dns
from common.log import LOGGING


class Dns(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('zone', type=str)
        self.reqparse.add_argument('host', type=str)
        self.reqparse.add_argument('type', type=str)
        self.reqparse.add_argument('data', type=str)
        self.reqparse.add_argument('view', type=str)
        super(Dns, self).__init__()

        args = self.reqparse.parse_args()
        self.zone = args.get('zone', None)
        self.host = args.get('host', None)
        self.type = args.get('type', None)
        self.data = args.get('data', None)
        self.view = args.get('view', 'any')

    def post(self):
        for arg in [self.zone, self.host, self.type, self.data]:
            if arg is None:
                return json.dumps({'status': 'error', 'reason': 'Bad Request'}), 400
        try:
            return add_dns(self.zone, self.host, self.type, self.data, self.view)
        except Exception, error:
            LOGGING.exception(str(error))
            return json.dumps({'status': 'error', 'reason': str(error)}), 500

    def delete(self):
        for arg in [self.zone, self.host, self.type, self.data]:
            if arg is None:
                return json.dumps({'status': 'error', 'reason': 'Bad Request'}), 400
        try:
            return del_dns(self.zone, self.host, self.type, self.data, self.view)
        except Exception, error:
            LOGGING.exception(str(error))
            return json.dumps({'status': 'error', 'reason': str(error)}), 500
