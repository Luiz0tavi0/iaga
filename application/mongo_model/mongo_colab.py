from mongoengine.document import Document, DynamicDocument
from mongoengine.fields import BooleanField, LazyReferenceField, IntField, ReferenceField, StringField, EmailField, ListField, DateTimeField, DateField
from datetime import datetime
from bson.objectid import ObjectId

class Colaborador(Document):
    name= StringField(required= True, max_length= 70, min_length= 2)
    active= BooleanField(default= False)
    cbo2002= IntField(required= True)
    cpf = StringField(regex = r"^\d{3}\.\d{3}\.\d{3}\-(\d{2}|[xX])", required= True, unique= True)
    birthdate= DateField(required= True)
    sex= StringField(regex= r"[F|M|NB]", max_length= 2, min_length= 1)
    address= StringField()
    mail= EmailField()
    workeddays= ListField(DateTimeField(), default=list)
    workplaces= ListField(LazyReferenceField('Ponto'), default=list)
    createdAt= DateTimeField(default= datetime.now())
    updatedAt= DateTimeField(default= datetime.now())
    
class Ponto(Document):
    name= StringField(required= True, max_length=70, min_length=2)
    address= StringField(required= True)
    employeelist= ListField(LazyReferenceField(Colaborador),unique= True)
    gateway = ListField(StringField())
    createdAt= DateTimeField(default= datetime.now())
    updatedAt= DateTimeField(default= datetime.now())