import json
from common.models import db, Dns
from common.log import LOGGING


def add_dns(zone, host, type, data, view):
    dns_record = Dns(zone=zone, host=host, type=type, data=data, view=view)
    db.session.add(dns_record)
    db.session.commit()
    LOGGING.info('DNS record add successfully. zone=%s, host=%s, type=%s, data=%s', zone, host, type, data)
    return json.dumps({'status': 'success'}), 200


def del_dns(zone, host, type, data, view):
    dns_record = Dns.query.filter_by(zone=zone, host=host, type=type, data=data, view=view).first()
    if dns_record is None:
        return json.dumps({'status': 'error', 'reason': 'DNS Record Not Found'}), 400
    db.session.delete(dns_record)
    db.session.commit()
    LOGGING.info('DNS record delete successfully. zone=%s, host=%s, type=%s, data=%s', zone, host, type, data)
    return json.dumps({'status': 'success'}), 200
