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

