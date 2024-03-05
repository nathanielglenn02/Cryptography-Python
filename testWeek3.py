import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# Create Password
password_provided = "password"
password = password_provided.encode()
salt = b'salt_'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)

message = "Ubaya".encode()

f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)
decrypted = f.decrypt(encrypted)
print(decrypted)