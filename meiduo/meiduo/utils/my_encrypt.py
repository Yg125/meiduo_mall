from itsdangerous.jws import TimedJSONWebSignatureSerializer as TJWSSerializer
from django.conf import settings


# 1, 加密openid
def encode_openid(openid):
    # 1, 创建加密对象
    serizlier = TJWSSerializer(settings.SECRET_KEY, expires_in=300)

    # 2, 加密数据
    token = serizlier.dumps({"openid": openid})

    # 3, 返回加密结果
    return token.decode()


# 2, 解密openid
def decode_openid(token):
    # 1, 创建加密对象
    serizlier = TJWSSerializer(settings.SECRET_KEY, expires_in=300)

    # 2, 加密数据
    try:
        openid = serizlier.loads(token).get("openid")
    except Exception as e:
        return None

    # 3, 返回加密结果
    return openid
