from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Logic:
    def __init__(self):
        self.text = ""
        self.result = ""
        self.public_key = ""
        self.private_key = ""
        self.generate_keys()

    def generate_keys(self):
        # Generate a new RSA key pair
        key = RSA.generate(2048)
        self.private_key = key.export_key()
        self.public_key = key.publickey().export_key()

    def save_keys(self, priv_file, pub_file):
        with open(priv_file, 'wb') as f:
            f.write(self.private_key)
        with open(pub_file, 'wb') as f:
            f.write(self.public_key)

    def load_keys(self, priv_file, pub_file):
        with open(priv_file, 'rb') as f:
            self.private_key = RSA.import_key(f.read())
        with open(pub_file, 'rb') as f:
            self.public_key = RSA.import_key(f.read())

    def encode(self):
        # Encrypt the message using the public key
        cipher = PKCS1_OAEP.new(self.public_key)
        self.result = cipher.encrypt(self.text.encode())

    def decode(self):
        # Decrypt the message using the private key
        cipher = PKCS1_OAEP.new(self.private_key)
        self.result = cipher.decrypt(self.text).decode()
