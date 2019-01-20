import uuid
import random
import json
from faker import Faker

fake = Faker()


class Info:
    def __init__ (self):
        self.name = fake.name()
        self.address = fake.address()
        self.age = random.randint(18, 60)


class User:
    def __init__ (self, Info, purchase_history, userid):
        self.info = vars(Info)
        self.purchase_history = purchase_history
        self.userid = userid


loUsers = []
for i in range(0,100):
    info = Info()
    user = User(info, None, str(uuid.uuid4()))
    loUsers.append(vars(user))

with open('user-data.json', 'w') as outfile:
    json.dump(loUsers, outfile)