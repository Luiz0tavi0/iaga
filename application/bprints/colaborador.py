from flask import Blueprint, request, jsonify
from application.mongo_model.mongo_colab import Colaborador, Ponto
from bson.json_util import ObjectId
from pprint import pprint

bp_colab = Blueprint('bp_colab', __name__, url_prefix= "/api/v0.1")

@bp_colab.route('/colaboradores', methods=['POST', 'GET', 'DELETE', 'PATCH'])
def colaborador():
    if request.method == "POST" and request.is_json:
        try:
            data= request.get_json()
            pt= {"name" : "aec", "address" : "Rua Principal",
            "employeelist" : [ObjectId("5e24ee902ca73172fa0e0d12")], "gateway" : ["Rua 1"]}

            new_colab= Colaborador(**data).save()
            return jsonify({"created_id": str(new_colab.id),"ok" : True, "message" : "colab created"}), 201
        except Exception as e:
            return jsonify({"ok": False, "message": f"{e.args[0]}"}), 400

    elif request.method == "GET":
        try:
            if "id" in request.args:
                arg_id= request.args["id"].strip()
                return jsonify(Colaborador.objects.get(id= ObjectId(arg_id)))
            elif "name" in request.args:
                arg_name= str(request.args["name"]).strip()
                return jsonify(Colaborador.objects.filter(name__iexact= arg_name)), 200
            else: return jsonify({"ok": False, "message": "invalid parameter"}), 404
        except Exception as e:
            return jsonify({"ok": False, "message": f"{e}"}), 400

    elif request.method == "PATCH":
        try:
            arg_id= request.args["id"]
            data= request.get_json()
            data["updatedAt"]= datetime.datetime.now()
            print(data)
            Colaborador.objects(id= ObjectId(arg_id)).update(**data)
            return jsonify({"ok": True, "message": "modified"}), 200
        except Exception as e:
            return jsonify({"ok": False, "message": f"{e.args[0]}"}), 400
        
    elif request.method == "DELETE":
        try:
            arg_id= request.args["id"]
            resp= Colaborador.objects(id= ObjectId(arg_id)).delete()
            if resp != 0:
                return jsonify({"ok": True, f"deleted": f"{arg_id}"}), 200
            else:
                return jsonify({"ok": False, f"deleted": None}), 404
        except Exception as e:
            return jsonify({"ok": False, "message": f"{e.args}"}), 400  



