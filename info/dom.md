## What is dompurify
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

  - How not to use it <br>
    If you first sanitize HTML and then modify it afterwards, you might easily void the effects of sanitization. If you feed the sanitized markup to another library after sanitization, please be certain that the library doesn't mess around with the HTML on its own.<br>
    Combining DOMPurify with happy-dom is currently not recommended and will likely lead to XSS<br>
    Use the latest version of jsdom because older versions of jsdom are known to be buggy in ways that result in XSS even if DOMPurify does everything 100% correctly


## What are math tags
The <math> MathML element is the top-level MathML element, used to write a single mathematical formula

## What are glyphs
A glyph is a term used in typography for the visual representation of one or more characters.<br>
The fonts used by a website contain different sets of glyphs, which represent the characters of the font.<br>
A glyph is a single representation of a character. Every font has a Unicode character map that links (abstract) character IDs with how to display that character, using the default glyphs<br>


## WHat is dom
When a web page is loaded, the browser creates a Document Object Model of the page.
The DOM is a W3C (World Wide Web Consortium) standard.
The DOM defines a standard for accessing documents:
"The W3C Document Object Model (DOM) is a platform and language-neutral interface that allows programs and scripts to dynamically access and update the content, structure, and style of a document."
The DOM defines the logical structure of documents and the way a document is accessed and manipulated. Essentially, it transforms the document into a tree of objects, each representing a part of the document, such as elements, attributes, text nodes, and comments. This hierarchical tree structure provides a means to traverse and modify the content of the document easily.

The W3C DOM standard is separated into 3 different parts:
- Core DOM - standard model for all document types
- XML DOM - standard model for XML documents
- HTML DOM - standard model for HTML documents

The HTML DOM is a standard object model and programming interface for HTML. It defines:
- The HTML elements as objects
- The properties of all HTML elements
- The methods to access all HTML elements
- The events for all HTML elements
- In other words: The HTML DOM is a standard for how to get, change, add, or delete HTML elements.

## What's a dom parser
The DOMParser interface provides the ability to parse XML or HTML source code from a string into a DOM Document . You can perform the opposite operation—converting a DOM tree into XML or HTML source—using the XMLSerializer interface. The DOM is a tree representation of the document. In order to create a page, you need to parse the HTML code into its corresponding DOM using DOM Parser.<br>
DOM Parser is a very useful tool for developers who want to manipulate HTML/XML documents. It allows them to easily extract information from the DOM tree.<br>
A DOM (Document Object Model) parser is a tool used in computer programming to read and manipulate an XML (Extensible Markup Language) or HTML (Hypertext Markup Language) document by treating it as a tree structure where each node represents a part of the document. This approach allows developers to access, modify, delete, or add elements and attributes in the document programmatically.

There are two primary types of DOM parsers:
- XML DOM Parsers: Used for parsing XML documents. Examples include:
  - javax.xml.parsers.DocumentBuilder in Java
  - xml.dom.minidom in Python
  - System.Xml.XmlDocument in C#

- HTML DOM Parsers: Used for parsing HTML documents. Examples include:
  - The DOMParser interface in JavaScript
  - BeautifulSoup in Python (although primarily an HTML parser, it also supports XML)
  - NSXMLDocument in Objective-C for macOS and iOS development

![image](https://github.com/poorvi1910/Web/assets/146640913/5e9edfbd-ee54-47b5-b284-7a7e4fd18766)


## If I give you html (i) How does any parser convert that to an actual dom (ii) What part of the dom parser makes the decision making of handling errors i.e. `<img=a>` automatically becoming `<img="a">`

(1)
- Lexical Analysis (Tokenization): The parser reads the HTML string character by character and breaks it down into tokens, such as tags, attributes, text nodes, and comments. Each token represents a distinct element of the document.

- Syntactic Analysis (Parsing): The parser takes the stream of tokens and builds a tree structure according to the rules of HTML grammar. This involves:
  - Element Nodes: Created for tags like <div>, <p>, etc.
  - Text Nodes: Created for the text content between the tags.
  - Attribute Nodes: Created for attributes within tags, such as class="example".

- Tree Construction: The parser organizes the nodes into a tree structure where the root is the document object, and child nodes represent elements, attributes, and text in a hierarchical manner.

(2)


## Choose a dom parser, preferably one using by browsers/dompurify and illustrate how (i) a good html (ii) a bad html i.e. one missing quotes, opening, closing tags gets rendered

(1)

(2)
