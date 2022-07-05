import shutil
import base64
import stegano
import hashlib
import urllib3
import tempfile
import requests
from Cryptodome.Cipher import AES
from stegano.lsbset import generators
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Temporary variable to store the image name
f = tempfile.NamedTemporaryFile(prefix='csb')

# Image - input
fName = '../testimages/6.png'
size = len(open(fName, "rb").read())

# secret message
plaintext = 'secret message here...'

# password to encrypt data
password = 'password here ...'

# AES encryption
def encryption(plaintext, key, mode):
    encobj = AES.new(key, AES.MODE_GCM)
    ciphertext, authTag = encobj.encrypt_and_digest(plaintext)
    return(ciphertext, authTag, encobj.nonce)


# symmetric key generation using password
key = hashlib.sha256(password.encode()).digest()

# encrypted data
enc = encryption(plaintext.encode(), key, AES.MODE_GCM)[::-1]
colossal = b""
for i in enc:
    colossal += i

# saving encrypted data to a variable
encoded_msg = colossal

# saving the encoded message to image file using stegano module
secret = stegano.lsbset.hide(fName,
                             base64.b64encode(encoded_msg).decode("ascii"),
                             generators.eratosthenes())

# saving the image file
secret.save(f.name+".png")

dest = '../EncodedImages/Steganography_Image.png'

# moving the encoded file from tmp directory to EncodedImages dir
shutil.move(f.name+".png", dest)

# uploading to filecoin/slate
url = "https://uploads.slate.host/api/v3/public"
files = {
    # "file": open(dest, "rb")
    "file": ("Steganography_Image.png", open(dest, "rb"), "image/png")
}
headers = {
    "Authorization": "<auth-key>"  # <authorization-key>
}
r = requests.post(url, headers=headers, files=files)
