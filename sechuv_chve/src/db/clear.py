from tinydb import TinyDB

db = {
    "web": TinyDB("./web.json"),
    "webvalid": TinyDB("./webvalid.json"),
    "mail": TinyDB("./mail.json"),
    "mailvalid": TinyDB("./mailvalid.json"),
    "other": TinyDB("./other.json"),
    "othervalid": TinyDB("./othervalid.json"),
    "vulnerability": TinyDB("./vulnerability.json"),
}

for db_name in db.keys():
    db[db_name].purge()
    print("[*] DB({}) was purged.".format(db_name))