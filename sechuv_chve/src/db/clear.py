from tinydb import TinyDB

db = {
    "web": TinyDB("db/web.json"),
    "webvalid": TinyDB("db/webvalid.json"),
    "mail": TinyDB("db/mail.json"),
    "mailvalid": TinyDB("db/mailvalid.json"),
    "other": TinyDB("db/other.json"),
    "othervalid": TinyDB("db/othervalid.json"),
    "vulnerability": TinyDB("db/vulnerability.json"),
}

for db_name in db.keys():
    db[db_name].purge()
    print("[*] DB({}) was purged.".format(db_name))