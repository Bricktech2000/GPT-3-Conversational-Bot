import hashlib

def gen_username_hash(name):
    """return 2-char hash for the given username"""
    return hashlib.sha1(name.encode("ascii")).hexdigest()[:2]

def change_usernames(convo):
    lines = convo.split('\n')

    for i, line in enumerate(lines):
        name_message = line.split(": ", 1) # split at the first ":"

        if len(name_message) == 2: # line not empty
            name, message = name_message
            new_name = gen_username_hash(name)
            lines[i] = f'{new_name}: {message}'

    return "\n".join(lines)


# base-64 is a good idea actually

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
