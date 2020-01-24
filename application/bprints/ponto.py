from flask import Blueprint, request,jsonify
from application.mongo_model.mongo_colab import Ponto
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from datetime import datetime


bp_ponto = Blueprint('bp_ponto',__name__,url_prefix="/api/v0.1")

@bp_ponto.route('/pontos', methods=['POST','GET','DELETE'])
def ponto():
    if request.method == "POST" and request.is_json:

        data= request.get_json()
        ponto= Ponto(**data)
        print(ponto)
        resul= ponto.save()
        print(data)
        return jsonify({"ok":"200","resultado": f"{resul.id}"})
        


