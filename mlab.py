import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds155292.mlab.com:55292/demogame


host = "ds155292.mlab.com"
port = 55292
db_name = "demogame"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
