# Covert Communication on Filecoin-slate

## Required dependencies

- Install the required dependencies before running the project

```bash
pip install -r requirements.txt
```

## Create the Filecoin-slate Account

- <https://slate.host/>
- Get API key from the slate.host after creating the account.
- Replace the API key in sender.py & get_details.py on lines 64 & 6 respectively.

## Run the sender code

```bash
python3 sender.py
```

- Script takes the input image, secret info and password, hides it into the image and uploads it to the filecoin-slate.
- Note: Change the fName & dest path variables accordingly before running the code.

## Download the image from slate or IPFS gateways using CID

- To get the CID of the image run the below script.

```bash
python3 get_details.py
```

- Or you can download it from the slate.host itself.
- Below are the gateways where you can find the image using CID.

```text
https://slate.textile.io/ipfs/<CID>
https://cloudflare-ipfs.com/ipfs/<CID>
http://ipfs.io/ipfs/<CID>
```

- Place the downloaded image in the project directory
- Replace the downloaded file name in Major_receiver.py on line 14.

## Run the receiver code

```bash
python3 receiver.py
```

- Script reads the downloaded image and extracts the hidden data from it using the password.

## Code organization

- EncodedImages - contains the encoded images after running the major_sender.py script.

- Testimages - contains the test images for uploading into the filecoin-slate blockchain.

- The project directory contains the receiver & sender python scripts which are the main project programs.

- Architectural block diagram of the project.

## References

- <https://github.com/filecoin-project/slate>
- <https://github.com/textileio/textile>
- <https://github.com/ipfs/ipfs>
- <https://asecuritysite.com/encryption/aes_gcm>
- <https://slate.host/>
- <https://www.mcafee.com/enterprise/en-in/downloads/free-tools/steganography.html>
- <https://security.filecoin.io/>
- <https://docs.filecoin.io/about-filecoin/ipfs-and-filecoin/#using-ipfs-and-filecoin>
