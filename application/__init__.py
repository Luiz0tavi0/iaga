from flask import Flask
from application.bprints.colaborador import bp_colab
from application.bprints.ponto import bp_ponto
from pprint import pprint

def create_app(name: str, mode: str):
    app = Flask(name)
    from application.base.mongo import mongo
    dbconfig= {'db': 'flaskdb','host': 'mongodb://localhost/flaskdb'}
    app.config['MONGODB_SETTINGS'] = dbconfig
    mongo.init_app(app)
    app.register_blueprint(bp_colab)
    app.register_blueprint(bp_ponto)
    return app
    