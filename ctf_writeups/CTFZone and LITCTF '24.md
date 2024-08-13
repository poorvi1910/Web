LITCTF: travserse

Working solutions: 
```curl http://litctf.org:31778/..%2Fflag.txt```
```└─$ curl -X GET "http://litctf.org:31778/?file=../../../flag.txt"```
While trying tis challenge i had tried different traversals but none worked. Even gobuster didnt yield anything. Turns out many web servers automatically
normalize URLs before processing them. This means they resolve ../ paths to prevent them from being used to escape the intended directory structure. 
For example, if you try to access ../flag.txt, the server might normalize it to the root directory or the base path you started from, effectively blocking
access to files outside the intended directory. But when we use %2F, it bypasses input validation
