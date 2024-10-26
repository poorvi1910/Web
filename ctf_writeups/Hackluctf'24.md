### Bench Press

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


We now have the height difference that corresponds to the individual height of a letter. However, this value is stored as a number, so how can we send it to our server?
We’ll make use of one final (also animation-related) trick: paused animations. By changing the delay of a paused animation, we can select different values. We use it to select an exfiltration URL that matches the right letter:

