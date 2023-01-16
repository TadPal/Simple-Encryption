import rsa

class Logic:
    def __init__(self):
        self.text = ""
        self.result = ""
        self.public_key = ""
        self.private_key = ""
        self.generate_keys()

    def generate_keys(self):
        # Generate a new RSA key pair
        (pubkey, privkey) = rsa.newkeys(512)
        # Assign the public and private keys to the public_key and private_key attributes
        self.public_key = pubkey
        self.private_key = privkey
        
    def save_keys(self, priv_file, pub_file):
        with open(priv_file, 'wb') as f:
            f.write(rsa.PrivateKey.save_pkcs1(self.private_key))
        with open(pub_file, 'wb') as f:
            f.write(rsa.PublicKey.save_pkcs1(self.public_key))

    def load_keys(self, priv_file, pub_file):
        with open(priv_file, 'rb') as f:
            self.private_key = rsa.PrivateKey.load_pkcs1(f.read())
        with open(pub_file, 'rb') as f:
            self.public_key = rsa.PublicKey.load_pkcs1(f.read())

    def encode(self):
        # Encrypt the message using the public key
        self.result = rsa.encrypt(self.text.encode(), self.public_key)

    def decode(self):
        # Decrypt the message using the private key
        self.result = rsa.decrypt(self.text, self.private_key).decode()
