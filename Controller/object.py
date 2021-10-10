import rsa

from Controller import controller

objects = []
object = {}


def add_object(name, description):
    object = {"object_name": name, "description": description, "hash": controller.object_hash(name, description)}
    (object["pubkey"],object["prikey"])=controller.gen_rsa()
    objects.append(object)
    return object["prikey"]


def get_object(name):
    for i in objects:
        if i["object_name"] == name:
            return i
    return

#
# if __name__ == '__main__':
#     sk= add_object("1234", "1234")
#     # print("hash校验", controller.is_valid("123", "123", controller.object_hash("123", "1234")))
#     signature = controller.singn("1234", "1234", sk)
#     print("签名",type(signature),"密钥",objects[0]["pubkey"])
#     print("rsa校验", str(controller.verify("1234", "1234", signature, objects[0]["pubkey"])))
