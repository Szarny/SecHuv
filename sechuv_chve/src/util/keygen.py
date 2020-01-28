# http://swdrsker.hatenablog.com/entry/2018/01/27/080000

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64decode, b64encode
import sys


def generate_key(keysize=2048, passphrase=None):
    new_key = RSA.generate(keysize)
    public_key = new_key.publickey().exportKey()
    secret_key = new_key.exportKey(passphrase=passphrase)
    
    with open("key/public.key", "wb") as f:
        f.write(public_key)

    with open("key/secret.key", "wb") as f:
        f.write(secret_key)


if __name__ == '__main__':
    generate_key(2048, input())