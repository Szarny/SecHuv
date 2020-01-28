# http://swdrsker.hatenablog.com/entry/2018/01/27/080000

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64decode, b64encode
import sys


def sign(data, passphrase="SecHuv"):
    secret_key = open("/project/util/key/secret.key", "rb").read()

    try:
        rsakey = RSA.importKey(secret_key, passphrase=passphrase)
    except ValueError as e:
        print(e)
        sys.exit(1)

    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    digest.update(b64decode(data))
    sign = signer.sign(digest)

    return b64encode(sign)


def verify(signature, data):
    pub_key = open("/project/util/key/public.key", "rb").read()

    rsakey = RSA.importKey(pub_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    digest.update(b64decode(data))

    if signer.verify(digest, b64decode(signature)):
        return True
    else:
        return False
