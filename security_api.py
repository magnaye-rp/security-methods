import flask,flask_cors,flask_restful
import hashlib

def hash_password(password):
    return hash(password), password

print(hash_password("nigga"))