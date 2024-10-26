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

## CSS injection
1. The classic injection attack
The attacker can simply inject the harmful code into the victim’s website either with a persistent injection or a reflected injection. In persistent injection type, the payload is stored in the server and as applicable, it is served to the visitor. While in the reflected injection type, the payload is inserted into a link and in turn, the page reflects the payload. An example is to replace tags such as <script> by <style> and “onerror” by <link rel=stylesheet href=…>

2. Using HTML attributes to read data
Attackers can embed codes for specific details or recursive operations to extract specific or a range of details from the website. In this method, the codes are executed and the malicious server is called with extracted data on matching specific conditions. For example, the below code recursively checks for usernames with specified characters and makes a call to the attacker’s server:

![image](https://github.com/user-attachments/assets/e6790389-2e63-4c56-8070-a70459a66413)

Through the above code, the attackers will keep extracting pieces of information until they can piece all of it to recreate a username to use in an upcoming attack.

3. Reading text in text node
CSS injection-based attacks are capable of reading attributes and extract details, but not from text nodes. In this method, attackers can access text nodes and read characters from within. Finally, the attacker will have bits and pieces of useful information that can be used to recreate actionable data. The below code is an example:

![image](https://github.com/user-attachments/assets/1cf9a2f8-6356-46ed-986a-b0b5cde7837d)

The above code will return characters A and B if they are present but not C. However, it is enough for attackers to plan or execute their next attackThe above are just some of the ways attackers can use CSS injection attacks on your website.

## Prevention

1. Sanitization based on context
This simply means applying different sanitization rules and forms of encoding for respective situations. For example, for script elements or entities within HTML tags, we can use hex encoding. There would be other scenarios where you might require white lists or HTML encoding

2. Using a strong Content Security Policy
You can implement a stringent CSP on your website, as it will protect your website even if you miss sanitizing any content. Using CSP you can restrict the source of image and stylesheets. This will ensure that CSS elements are loaded only from trusted servers and not from other domains thus stopping such attacks
