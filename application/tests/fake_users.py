from faker import Faker
from pprint import pprint
from bson.json_util import dumps, loads
#import json
from _datetime import datetime
from random import randint

def random_user(locale="pt_BR"):
    Fake= Faker(locale)
    profile= Fake.simple_profile()
    profile["birthdate"]= profile["birthdate"].strftime("%d/%m/%Y")
    profile["cbo2002"] = randint(10105, 992225)
    del(profile['username'])
    profile["address"]= profile["address"].replace("\n","-")
    return (dumps(profile))
if __name__ == "__main__":
    print(random_user())
