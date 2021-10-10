from flask import Flask
from flask import request
from flask_cors import *
import json
from Controller import object, controller
from flask import Flask, render_template, make_response

from Controller.controller import object_hash

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置参数


@app.route("/add_object", methods=["POST", "GET"])
def index():
    print("添加一次物品")
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    object_name = request.form["name"]
    object_description = request.form["description"]
    cur_object = object.get_object(object_name)
    result = {}
    if cur_object!=None:
        result["isexist"]="true"
        return result
    # 返回私钥
    sk_key_test = object.add_object(object_name, object_description)
    result["is_exist"] = "false"
    result["sk"] = sk_key_test
    return result


@app.route("/vertify_hash", methods=["POST", "GET"])
def vertify_hash():
    print("验证hash中···")
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    object_name = request.form["name"]
    object_description = request.form["description"]
    # 返回私钥
    cur_hash = object_hash(object_name, object_description)
    cur_object = object.get_object(object_name)
    result = {}
    if cur_object == None:
        result["is"] = False
        return result

    result["is"] = cur_hash == cur_object["hash"]
    return result


@app.route("/vertify_rsa", methods=["POST", "GET"])
def vertify_rsa():
    print("验证RSA中···")
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    object_name = request.form["name"]
    prikey = request.form["prikey"]
    result = {}
    cur_object = object.get_object(object_name)
    if cur_object is None:
        result["is"] = False
        return result
    # 签名
    print("商品描述"+cur_object["description"])
    signature = controller.singn(object_name, cur_object["description"], prikey)
    result["is"] = controller.verify(object_name, cur_object["description"], signature, cur_object["pubkey"])
    return result


if __name__ == '__main__':
    app.debug = True  # 设置调试模式，生产模式的时候要关掉debug
    app.run()
