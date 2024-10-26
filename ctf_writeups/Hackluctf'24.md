## Bench Press

- Concept : Leaking Text Nodes with CSS
  ```
  a text node is the actual text content of an element, but CSS can’t select it independently. Instead, CSS styles can be applied to the parent element to affect its appearance
  ```
- Goal: To get the authentication token below and only possible injection was the theme parameter which was inside the style tag
```
<!DOCTYPE html>
<html>
<head>
  <!-- ... -->
  <script nonce="...">t="01b275146755aac26d5b2c7821b7c3"</script>
<!-- ... -->
```

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
Techniques that leak the charset of a text node that would fit our conditions:

- Using default fonts to cause size differences
- Using default fonts to cause timing differences. Timing side-channels are generally slower and less reliable, so let’s go with the size differences

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

