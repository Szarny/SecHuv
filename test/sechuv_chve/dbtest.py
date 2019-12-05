from tinydb import TinyDB

db = TinyDB("hoge.json")

class C:
    def __init__(self, p):
        self.p = p
    
    def map(self):
        return {
            "p": self.p
        }

c = C(1)
print(db.insert(c.map()))