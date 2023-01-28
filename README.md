# Message Encoding Examples

[![GitHub last commit](https://img.shields.io/github/last-commit/TadPal/PythonProject)](https://github.com/TadPal/PythonProject)
[![Python 3.9+](https://img.shields.io/badge/python-3.9-green.svg)](https://www.python.org/downloads/release/python-390/)

A simple python app to show different types of encoding. Using different encoding libraries and Tkinter for GUI.

Including:
- Caesar's cipher
- Base64
- RSA

## Installation

You will need to install several packages using [pip](https://pip.pypa.io).

```bash
pip install pybase64
pip install pycryptodome
```

or

```bash
py -m pip install pycryptodome
py -m pip install pybase64
```

## Usage

Run the main script and choose desired encoding

1. Fill in the message you want to encode or decode
2. Enter valid key (see below)
3. Click **"Encode"** or **"Decode**

**For RSA the approach is a little different** see [below](#rsa-encryption)

### Caesar's cipher

- The key must be an **integer**

Caesar's cipher shifts the characters' values by the given number in the ASCII table.

It is relatively easy to crack given that the characters are shifted by the same value.

### Base64

- The key must be written using **ASCII characters**

This method shift the characters' values based on the valuse of the key characters first and then use BASE64 encoding explained [here](https://bunny.net/academy/http/what-is-base64-encoding-and-decoding/).

This encoding method is a little harder to crack, given that we shift the characters first and that BASE64 uses 64 characters as its base.

Because the key for encoding and decoding is the same we call this **symmetric encryption**

### RSA Encryption

1. In this case the we must enter the path to the keys' files.
    - In this project there are some keys already generated here: **"RSAKeys/key"**, but if you want to generate new ones press **"Save Keys"** or simply change the keys by opening the files in a text editor
2. Than we have to load the keys by pressing **"Load Keys"**
3. Now we can enter the desired message to encode or decode
4. Press **"Encode"** or **"Decode"**

The RSA encryption method is still used for various purposes. What makes it different from the other examples in this project is that it uses two keys (private and public) for encryption. You don't have to tell anyone your private key, you only send them the public key, which they use to encrypt messages meant for you that can only be decrypted with the private key. The same goes for the other person you only get their public key to encrypt. 

We call this **assymetric encryption**.

The RSA encryption takes advatnage of maths and more precisely prime numbers and modulus operation. Explained [here](https://www.youtube.com/watch?v=4zahvcJ9glg). 

The RSA encryption is considered safe only using large keys. As of today 2048 bits is considered as minimum safe key size. 

## TODO:
- Add more encoding methods
- Allow private and public keys editing in the GUI.

## Example
![Example](Example.png)

