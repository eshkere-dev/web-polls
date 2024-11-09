import bcrypt
import os

def hash_password_bcrypt(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password_bcrypt(stored_hash, input_password):
    return stored_hash == bcrypt.hashpw(input_password.encode('utf-8'), stored_hash)

password = "my_secure_password"
hashed_password = hash_password_bcrypt(password)
print(password, hashed_password)
print(verify_password_bcrypt(b'$2b$12$OoxgHDid.P2kFbmb.oL8z.Nkc/erNHJ9NkImohYFWYWtKuZA/tjvS', password))
