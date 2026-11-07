from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

symmetric_key = Fernet.generate_key()
cipher = Fernet(symmetric_key)

message = input("Enter a message: ")

encrypted_symmetric = cipher.encrypt(message.encode())

print("\n--- Symmetric Encryption ---")
print("Encrypted Message:", encrypted_symmetric.decode())

decrypted_symmetric = cipher.decrypt(encrypted_symmetric)

print("Decrypted Message:", decrypted_symmetric.decode())

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

encrypted_asymmetric = public_key.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\n--- Asymmetric Encryption")
print("Encrypted Message:", encrypted_asymmetric.hex())

decrypted_asymmetric = private_key.decrypt(
    encrypted_asymmetric,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Decrypted Message:", decrypted_asymmetric.decode())
