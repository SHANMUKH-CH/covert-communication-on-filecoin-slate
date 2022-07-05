import base64
import stegano
import hashlib
from Cryptodome.Cipher import AES
from stegano.lsbset import generators

# password used to encrypt data
password = 'Xy_shan_d.500b22a'

# symmetric key used to encrypt or decrypt data
key = hashlib.sha256(password.encode()).digest()

colossal = base64.b64decode(stegano.lsbset.reveal(
    "./code.png", generators.eratosthenes()).encode("ascii"))
print(colossal)

# AES
def decryption(ciphertext, key, mode):
    (ciphertext,  authenticationTag, nonce) = ciphertext
    encodedobject = AES.new(key,  mode, nonce)
    return(encodedobject.decrypt_and_verify(ciphertext, authenticationTag))


# passing the values to decryption function
enc_mess = (colossal[0:16], colossal[16:32], colossal[32:])[::-1]
res = decryption(enc_mess, key, AES.MODE_GCM)

# printing the decrypted message
print("\nDecrypted Message:", res.decode())
