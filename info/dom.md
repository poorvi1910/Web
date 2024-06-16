## What is dompurity
  - DOMPurify sanitizes HTML and prevents XSS attacks. You can feed DOMPurify with string full of dirty HTML and it will return a string (unless configured otherwise) with clean HTML. DOMPurify will strip out everything that contains dangerous HTML and thereby prevent XSS attacks and other nastiness.
  - ### How to use it <br>
  Just include DOMPurify on your website<br>
  
  Using the unminified development version<br>
  ```<script type="text/javascript" src="src/purify.js"></script>```<br>
  
  Using the minified and tested production version (source-map available)<br>
  ```<script type="text/javascript" src="dist/purify.min.js"></script>```<br>
  
  Afterwards you can sanitize strings by executing the following code:<br>
  ```const clean = DOMPurify.sanitize(dirty);```<br>
  
  Or maybe this, if you love working with Angular or alike:<br>
  ```
  import DOMPurify from 'dompurify';
  const clean = DOMPurify.sanitize('<b>hello there</b>');
  ```
  The resulting HTML can be written into a DOM element using innerHTML or the DOM using ```document.write()```. That is fully up to you. Note that by    default, we permit HTML, SVG and MathML. If you only need HTML, which might be a very common use-case, you can easily set that up as well:
 ``` const clean = DOMPurify.sanitize(dirty, { USE_PROFILES: { html: true } })```

  - How not to use it

    
  - Configuration, what to allow, what not
## What are math tags
## what are glyphs

500 words minimum on below stuff
WHat is dom
what's a dom parser
if I give you html
how does any parser convert that to an actual dom
what part of the dom parser makes the decision making of handling errors i.e. `<img=a>` automatically becoming `<img="a">`
choose a dom parser, preferably one using by browsers/dompurify and illustrate how 
1 a good html
2 a bad html i.e. one missing quotes, opening, closing tags
gets rendered