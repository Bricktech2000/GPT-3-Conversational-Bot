import base64
import hashlib

def genHashUsername(name):
    """retrun 2 char long hash for the given username"""
    return hashlib.sha1(name.encode("ascii")).hexdigest()[:2]

def change_usernames(convo):
    lines = convo.split('\n')
    names = set()
    for i in range(len(lines)):
        name = lines[i].split(":")
        print(name)
        newName = genHashUsername(name[0])
        lines[i] = newName + ":"
        lines[i] += ":".join(name[1:len(name)]) if len(name) > 2 else name[1]
    
    return "\n".join(lines)
        
    #print(names)

# def encode_to_b64(username):
#     user_bytes = username.encode("ascii")
#     base64_bytes = base64.b64encode(user_bytes)
#     return base64_bytes.decode("ascii")

# def decode_from_b64(base64_username):
#     base64_bytes = base64_username.encode("ascii")
#     user_bytes = base64.b64decode(base64_bytes)
#     username = user_bytes.decode("ascii")
#     return username

# print(name[::-1])

# conv = open("training_data/Grace_optimized.txt", "r").read()
# print(change_usernames(conv))

# name = "akaowen"
# print(name, base26Value(name))
# print(name, genUsername(name))