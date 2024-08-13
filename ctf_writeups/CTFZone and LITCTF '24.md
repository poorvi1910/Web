## LITCTF: travserse

#### Working solutions: <br>
```curl http://litctf.org:31778/..%2Fflag.txt``` <br>
```└─$ curl -X GET "http://litctf.org:31778/?file=../../../flag.txt"``` <br>

While trying tis challenge i had tried different traversals but none worked. Even gobuster didnt yield anything. Turns out many web servers automatically
normalize URLs before processing them. This means they resolve ../ paths to prevent them from being used to escape the intended directory structure WITHOUT showing any sort of error. 
For example, if you try to access ../flag.txt, the server might normalize it to the root directory or the base path you started from, effectively blocking
access to files outside the intended directory. But when we use %2F, it bypasses input validation.

## CTFzone: Old but gold

In tis challenge i had been looking for direct comment ssti but turns out what we had to do was capture the comment request on burpsuite first. That then showed the endpoint as /api/v2. From the challenege description, it can be deduced that we need to go to v1 endpoint. When we go to /api/v1 then we are prompted to enter a username. Now this username field is the vulnerable field. When we put in a basic ssti payload, we get the flag.
