import base64

def encode(username):
    user_bytes = username.encode("ascii")
    base64_bytes = base64.b64encode(user_bytes)
    return base64_bytes.decode("ascii")

def decode():
    pass