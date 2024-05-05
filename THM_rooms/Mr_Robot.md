### Visiting the ip:<br>
I went to the ip and ran the commands which were just videos. The source code also didnt give anything.

### Starting off by running an nmap scan:<br>
```nmap -A [Domain Name] <br>```
Here -A indicates aggressive, it will give us extra information, like OS detection (-O), version detection, script scanning (-sC), and traceroute (–traceroute). It even provides a lot of valuable information about the host.
![image](https://github.com/poorvi1910/Web/assets/146640913/ab5c0625-1ae3-410f-b292-f75a0a113d83)

### Next running a dirsearch:<br>
Dirsearch tool is an advanced command-line tool designed to brute-force directories and files in web servers or web path scanners

```dirsearch -u http://10.10.67.171/ -t 60 /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt```

![image](https://github.com/poorvi1910/Web/assets/146640913/a2ddd5c8-5425-48c6-ba3a-e82e48b891db)

I am going to be following all the 200 (OK) response endpoints.
We can see a robots.txt here. A robots.txt file tells search engine crawlers which URLs the crawler can access on your site.Goin there we get the first key.
```
User-agent: *
fsocity.dic
key-1-of-3.txt
```
Going to http://10.10.67.171/fsocity.dic we get a list which i cant figure out the use of right now <br>
Going to http://10.10.67.171/key-1-of-3.txt we get the key: <br>
```KEY1: 073403c8a58a1f80d943455fb30724b9```

I next went to sitemap.xml and did not find anything.
I next come to a /wp-login/ endpoint. Going to it:

![image](https://github.com/poorvi1910/Web/assets/146640913/1764057e-fb53-42f8-b335-e36a3f925e9c)

I think i know where the wordlist fsocity will be used
If we go to burp and put in the list as payload for username in intruder and start attack, we see that for the name 'Elliot', the response is very unique as that from others
![image](https://github.com/poorvi1910/Web/assets/146640913/388619b5-bdaf-46a5-86d4-220c839d9515)

I tried the same list for password field but didn't get it. So I tired rockyu but burp wasnt able to even load the list for me. So went to a writeup and it was mentioned that the process tokk half an hour and that the password is ER28–0652. NOTE that password attacks on wordpress site can also be done using wpscan which i didn't know.

### Reverse shell:<br>
NOTE: Port 53 is a good port to start areverse shell on because it is rarely blocked by a firewall

Code for php reverse shell ca be found on this site:
https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

If we go to Appearences-->Editor-->404 template and paste this code there, chage the ip address to that of vpn and port to say 1234 and run the following command on terminal:

```nc -nvlp 1234```

```python -c "import pty; pty.spawn('/bin/bash')"```
The command  is a Python one-liner that invokes the pty module to spawn a pseudo-terminal running /bin/bash. This effectively creates an interactive shell session within the current terminal.

It's commonly used when you have a limited shell (such as when you're executing commands through a web application or SSH session) and you want to upgrade it to a fully interactive shell. This can be particularly useful for tasks like exploring the file system, running more complex commands, or accessing restricted resources.

After executing this command, you'll typically find yourself in a more interactive shell environment where you can execute commands as if you were directly logged into the system.


![image](https://github.com/poorvi1910/Web/assets/146640913/df0e08d5-2c09-48f4-9c53-26fe4e49f980)


Cracking the md5 hash: https://crackstation.net/ <br>
![image](https://github.com/poorvi1910/Web/assets/146640913/ba4a8825-5ab7-48a6-8b81-a4d992380cbb)

![image](https://github.com/poorvi1910/Web/assets/146640913/e32f55e3-54b5-450b-ab39-9cea64f06cdc)

We need to the user to be robot to be able to read the key-2-of3.txt file

The su command changes user credentials to those of the root user or to the user specified by the Name parameter, and initiates a new session. It cannot be run from a shell that is not interactive

![image](https://github.com/poorvi1910/Web/assets/146640913/086b79c5-e557-4fd4-8101-551e8d498647)

```KEY 2: 822c73956184f694993bede3eb39f959```

### Privelege escalation :<br>

User robot doesn’t have permission to run sudo command

Commonly noted as SUID, the special permission for the user access level has a single function: A file with SUID always executes as the user who owns the file, regardless of the user passing the command. Hence running this command which searches for all files having SUID bit set

```find / -perm -u=s -type f 2>/dev/null```

![image](https://github.com/poorvi1910/Web/assets/146640913/5988476e-6583-4cd0-a72c-ae9f8cebf9c6)

Apart from nmap, rest all are standard, hence we know that we have to make use of that. Now if we visit GTFO bins website(GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.) https://gtfobins.github.io/ and search “nmap” which shows us possible command to privilege escalate.

![image](https://github.com/poorvi1910/Web/assets/146640913/b79181c4-5594-4ac5-9325-8dba0b17aace)

Using the second option: <br>

![image](https://github.com/poorvi1910/Web/assets/146640913/e1975405-1f0d-4747-b388-6eb8c2534395)

```KEY 3: 04787ddef27c3dee1ee161b21670b4e4```

## Additional shell commands :<br>

![image](https://github.com/poorvi1910/Web/assets/146640913/d2330191-5d81-431a-9784-c01d33293670)

![image](https://github.com/poorvi1910/Web/assets/146640913/ede36303-2a3c-4f0f-a670-eca3b4976d72)

![image](https://github.com/poorvi1910/Web/assets/146640913/26df536c-a945-4ef1-bf93-3479f9b6bce5)

![image](https://github.com/poorvi1910/Web/assets/146640913/1190c447-46bd-4136-aeb9-96a7f1191ca9)
