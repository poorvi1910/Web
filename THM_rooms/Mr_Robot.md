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


