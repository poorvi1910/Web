# Fireleak

### Overview
Cross-site leaks (aka XS-Leaks, XSLeaks) are a class of vulnerabilities derived from side-channels built into the web platform. They take advantage of the web’s core principle of composability, which allows websites to interact with each other, and abuse legitimate mechanisms to infer information about the user.

An XS-Leak (Cross-Site Leak) is a vulnerability where an attacker can infer sensitive information from another site based on side effects or timing differences, even if direct access to the information is not possible due to the Same-Origin Policy (SOP). XS-Leaks exploit the browser's behavior rather than directly interacting with server-side data.

The pieces of information used for an XS-Leak usually have a binary form and are referred to as “oracles”. Oracles generally answer with YES or NO to cleverly prepared questions in a way that is visible to an attacker. For example, an oracle can be asked:
Does the word secret appear in the user’s search results in another web application?

### How this chall uses it
This challenge is an XS-Leak because it leverages timing differences caused by the processing of invalid input patterns in an HTML <input> element to infer the sensitive admin token (req.cookies.TOKEN)

### Goal :
To steal an admin token: req.cookies.TOKEN and the token's format is 6-bytes hex string ([0-9a-f]{12})

### Limitations :
- For the html parameter:
  - Length limit: 1024
  - Allowed characters: [\x20-\x7e\r\n]
  - Disallowed substring (case-insensitive): meta, link, src, data, href, svg, :, %, &, \, //
- CSP: default-src 'none'; base-uri 'none'; frame-ancestors 'none'
- A new token is issued each time a URL is reported to the admin bot.
- You need to steal the token within 60 seconds

### Solution
- **The pattern attribute**:
  When specified, is a regular expression which the input's value must match for the value to pass constraint validation.
