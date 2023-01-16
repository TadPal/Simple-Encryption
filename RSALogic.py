import rsa

class RSAEncoder:
    def __init__(self):
        self.text = ""
        self.result = ""
        self.public_key = ""
        self.private_key = ""

    def generate_keys(self):
        # Generate a new RSA key pair
        (pubkey, privkey) = rsa.newkeys(512)
        # Assign the public and private keys to the public_key and private_key attributes
        self.public_key = pubkey
        self.private_key = privkey

    def encode(self):
        # Encrypt the message using the public key
        self.result = rsa.encrypt(self.text.encode(), self.public_key)

    def decode(self):
        # Decrypt the message using the private key
        self.result = rsa.decrypt(self.text, self.private_key).decode()
