# Bind_DLZ_API

RESTful API to Bind-DLZ, written by Python/Flask. Providing add/remove/query dns records.

## How To Use

### Config and Run

1. Modify `dns_api.conf`:

```shell
# Run on the given IP.
host =
# Run on the given port.
port = 
# Debug Mode (True of False)
debug =
# Path to the log
log_path =
# table name of the bind-dlz database.
table_name =
# connection to database. e.g, mysql+pymysql://username:password@127.0.0.1/dns
connection =
# Responsible person SOA record. e.g, "root.domain.com.".
resp_person =
# Primary name server SOA record. e.g, "ns.domain.com.".
primary_ns =
```


2. Start Bind-DLZ Api:

```shell
$ python dns_api.py
```

### Usage

1. Add a DNS record:

```shell
$ curl -X POST -H 'Content-Type: application/json' -d '{"zone": "example.com", "host": "test", "type": "A", "data": "1.1.1.1"}' http://localhost:8991/v1.0/dns
```

2. Delete a DNS record:
```shell
curl -X DELETE -H 'Content-Type: application/json' -d '{"zone": "example.com", "host": "test", "type": "A", "data": "1.1.1.1"}' http://localhost:8991/v1.0/dns
```

3. Get all DNS records:
```shell
curl -X GET http://localhost:8991/v1.0/dns
```

4. Get DNS records by zone:
```shell
curl -X GET http://localhost:8991/v1.0/dns/zone
```