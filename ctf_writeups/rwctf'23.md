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

## Solution
