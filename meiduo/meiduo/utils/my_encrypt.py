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


# 3, 加密验证邮箱信息
def generate_verify_url(user, email):
    # 1, 准备数据
    user_data = {
        'user_id': user.id,
        "email": email
    }

    # 2, 创建加密对象
    serializer = TJWSSerializer(secret_key=settings.SECRET_KEY, expires_in=300)

    # 3, 加密数据
    token = serializer.dumps(user_data).decode()
    url = 'http://127.0.0.1:8000/verify/email?token=%s' % token
    verify_url = '<a href="%s">%s</a>' % (url, url)

    # 4, 返回数据
    return verify_url
