from hashlib import sha256
from .app import app
from base64 import b64encode

def space_between(input:str, nbr:int) -> str:
    res = ""

    for i in range(len(input)):
        if i % (nbr) == 0:
            res += ' '

        res += input[i]

    return res

def crypt(text:str) -> str:
    h = sha256()
    h.update(text.encode())

    return h.hexdigest()

@app.template_filter('to_b64')
def to_b64(value):
    return b64encode(value)