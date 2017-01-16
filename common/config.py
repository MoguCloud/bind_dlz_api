from oslo_config import cfg
from oslo_config import types

CONF = cfg.CONF

PortType = types.Integer(1, 65535)

common_opts = [
    cfg.BoolOpt('debug',
                default=False,
                help='print debugging output.'),

    cfg.IPOpt('host',
              default='0.0.0.0',
              help='host of api server'),

    cfg.Opt('port',
            type=PortType,
            default=8991,
            help='port of api server'),

    cfg.StrOpt('log_path',
               default='dns_api.log',
               help='logging path'),

    cfg.StrOpt('table_name',
               default=False,
               help='table_name of Bind_dlz database'),

    cfg.StrOpt('connection',
               default=False,
               help='connection of Bind_dlz database. dialect+driver://username:password@host:port/database. '
                    'e.g, mysql+pymysql://username:password@127.0.0.1/dns'),

    cfg.StrOpt('resp_person',
               default=False,
               help='Responsible person SOA record.'
                    'e.g, "root.domain.com."'),

    cfg.StrOpt('primary_ns',
               default=False,
               help='Primary name server SOA record.'
                    'e.g, "ns.domain.com."'),
]

CONF.register_cli_opts(common_opts)

CONF(default_config_files=['dns_api.conf'])
