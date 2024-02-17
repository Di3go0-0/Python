from jwt import encode, decode



def createToken(data, secret="123456789"):
    token = encode(payload=data, key=secret, algorithm= 'HS256')
    return

def validadeToken(token, secret="123456789"):
    data = decode(token, key=secret, algorithm= ['HS256'])
    return data


