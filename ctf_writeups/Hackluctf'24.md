## Bench Press

- Concept : Leaking Text Nodes with CSS

- The csp
 ```
style-src 'unsafe-inline'
we’re big fans of inline styles here
img-src http: https:
remote images are welcome too
frame-ancestors 'none'
no framing
base-uri 'none'
no <base>
form-action 'self'
no weird forms
default-src 'none'
no other stuff (read: no JS)
sandbox allow-forms
really, really no JS (missing allow-scripts)
```
### Steps used
- Make the text element have 1 char per line
- Configure letters to have unique heights
- Iteratively remove/hide more and more characters from the text
- Calculate the height difference between two steps to find which character was removed
- Exfiltrate the letter to our attacker server

### Payload construction

- Exfiltrating the Letters
  
We now have the height difference that corresponds to the individual height of a letter. However, this value is stored as a number, so how can we send it to our server? Paused animations. 
```
Paused animations can be useful in CSS and JavaScript when you want to stop or control the timing of animations on the page
```
By changing the delay of a paused animation, we can select different values. We use it to select an exfiltration URL that matches the right letter:

