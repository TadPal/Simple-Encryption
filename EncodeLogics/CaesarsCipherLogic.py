class Logic:
    def __init__(self):
        self.text = ""
        self.private_key = ""
        self.result = ""
        self.name = "Caesars Cipher"

    def encode(self):
        # Create an empty list to store the encoded characters
        enc = []
        # Iterate through each character in the message text
        for char in self.text:
            # Shift the character by the key value (in ASCII table) and append it to the enc list
            enc.append(chr((ord(char) + int(self.private_key)) % 256))
        # Join the encoded characters in the enc list and assign the result to the result attribute
        self.result = "".join(enc)

    def decode(self):
        # Create an empty list to store the decoded characters
        dec = []
        # Iterate through each character in the message text
        for char in self.text:
            # Shift the character by the key value in the opposite direction and append it to the dec list
            dec.append(chr((256 + ord(char) - int(self.private_key)) % 256))
        # Join the decoded characters in the dec list and assign the result to the result attribute
        self.result = "".join(dec)
