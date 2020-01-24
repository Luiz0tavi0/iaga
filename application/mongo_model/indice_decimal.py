from mongoengine.document import Document
from mongoengine.fields import IntField, StringField
from pprint import pprint

class Indice(Document):
    name= StringField(max_length= 10, min_length= 2)
    ind_colab= IntField(min_value=0)
    ind_ponto= IntField(min_value=0)

def nextId(dec= False, indexColl= "colab"):
    if  indexColl == "colab":
        if dec == True:
            Indice.objects.upsert_one(id= "0"*24, dec__ind_colab= 1)
        else:
            Indice.objects.upsert_one(id= "0"*24, inc__ind_colab= 1)
        id= Indice.objects(id= "0"*24).get()
        return id.ind_colab
    elif indexColl == "ponto":
        if dec == True:
            Indice.objects.upsert_one(id= "0"*24, dec__ind_ponto= 1 )       
        else:
            Indice.objects.upsert_one(id= "0"*24, inc__ind_ponto= 1)
        id= Indice.objects(id= "0"*24).get()
        return id.ind_ponto