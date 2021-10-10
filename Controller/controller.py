import hashlib
import marshal
import rsa


# 生成hash
def object_hash(name, description):
    s = name + " " + description
    s_bytes = s.encode("utf-8")
    hash_value = hashlib.md5(s_bytes)
    return hash_value.hexdigest()


# 校验hash
def is_valid(name, description, hash):
    pre_hash = object_hash(name, description)
    return pre_hash == hash


def gen_rsa():
    (pk, sk) = rsa.newkeys(512)
    return (pk.save_pkcs1().decode(), sk.save_pkcs1().decode())


# 私钥对物品签名
def singn(name, description, sk):
    message =name+description
    sk = rsa.PrivateKey.load_pkcs1(sk.encode())
    signture = rsa.sign(message.encode(), sk, 'SHA-1')
    return signture


# 对签名进行校验
def verify(name, description, singnature, pk):
    pk = rsa.PublicKey.load_pkcs1(pk.encode())
    message =name+description
    res=''
    try:
        res = rsa.verify(message.encode(), singnature, pk)
        rsa.verify(message, singnature, pk)
        print("密钥通过~~")
    except :
       print("有异常")
    if res=='SHA-1':
        return True
    else :
        return False

# if __name__ == '__main__':
#     # test = object_hash("1234", "123")
#     # print(test)
#     # print(is_valid("123", "123", test))
#     pk_test,sk_test= gen_rsa()
#     sk=rsa.PrivateKey.load_pkcs1(sk_test.encode())
#     signature=singn("123","123",sk)
#     pk=rsa.PublicKey.load_pkcs1(pk_test.encode())
#     print(verify("123","123",signature,pk))
