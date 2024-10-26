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

Visibility Control: Instead of actually deleting a character from the HTML (which would be permanent and wouldn’t allow us to measure changes), the character can be hidden using CSS properties like display: none; or visibility: hidden;. This effectively makes it “removed” from view without altering the document structure.

Measuring Height Differences: Each character has a specific height, and by hiding one character at a time, you can observe how the total height of the text element changes. The difference in height indicates which character was hidden based on its unique height value.

Iterative Process: By sequentially hiding each character and measuring the height after each removal, you can track and log the height changes corresponding to each character. For example, if hiding the letter "A" reduces the height by a specific amount, that height difference can be tied back to "A" based on the unique height mapping.

Data Exfiltration: The goal is to leak this character information by sending the recorded height changes to an attacker's server. Since each character corresponds to a unique height, the attacker can reconstruct the hidden text from the received height values.
- Goal: To get the authentication token below and only possible injection was the theme parameter which was inside the style tag

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
This allows us to do conditional styling based on the text height
 
- Exfiltrating the Letters
  
The height difference that corresponds to the individual height of a letter is stored as a number, so how can we send it to our server? Paused animations. 
```
When the height difference (corresponding to the height of a single letter) is stored as a number in CSS, it becomes challenging to send this data directly to a server because CSS properties alone do not support direct network requests or data transmission. CSS is inherently limited to styling and layout purposes and cannot interact directly with external resources like servers.

Paused animations can be useful in CSS and JavaScript when you want to stop or control the timing of animations on the page
```
By changing the delay of a paused animation, we can select different values. We use it to select an exfiltration URL that matches the right letter

- Unique Letter Heights
To give every letter an individual height, we make use of descent-override (MDN):

```
@font-face {
    font-family: has_A;
    /* local font must be present on the target: */
    src: local('DejaVu Sans Mono');
    /* matches only the letter A: */
    unicode-range: U+41;
    /* set the height to 200% of its normal height: */
    descent-override: 200%;
}
```
By repeating this for all possible characters (in our case hex), we can give each letter an individual height. This will later allow us to map a height difference to a letter.

