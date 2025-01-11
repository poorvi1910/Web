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
- You need to construct a stable oracle to ensure the leak process completes within 60 seconds.
- An XS-Leak depending on the browser's busy state tends to be unstable and takes a long time.

### Solution
- **The pattern attribute**:

  When specified, is a regular expression which the input's value must match for the value to pass constraint validation.

  When a user enters data in an input field, the browser checks if the input matches the regular expression in the pattern. This process is computational and can be exploited for ReDoS (Regular Expression Denial of Service) attacks in certain cases.

- Understanding the Components of the Pattern
  
   ```
    <input
      type="text"
      pattern=".*(.?){12}[abcd]beaf"
      value="xxxxx...snip...xxxxx{{TOKEN}}"
    >
    ```

  - .* (Match anything, 0 or more characters):
  This ensures the regex engine can match any input, regardless of the characters before the token.
  It allows flexibility to handle the padding (xxxxx...snip...xxxxx) used to mask the token in the HTML input field.
  
  - (.?){12} (Match exactly 12 characters, each optionally present):
  This part is tailored to match the exact length of the token, which is a 6-byte hex string ([0-9a-f]{12}).
  
  - The .? allows optional characters, which increases the complexity of the regex engine’s evaluation when matching or failing. The {12} ensures that the regex looks for precisely 12 characters, corresponding to the token length.
    
  - [abcd] (Match any of the characters a, b, c, or d): This narrows down the possibilities for a specific part of the token, enabling the attacker to check whether the token contains a character from this subset.
  
  - beaf (Match the exact string beaf): This checks if the token ends with beaf. If the token doesn't match, the regex engine performs backtracking to reevaluate previous possibilities, causing a measurable delay.

- Why This Specific Pattern?

    - The challenge explicitly states that the token is a 12-character hex string ([0-9a-f]{12}).
  This allows the attacker to design patterns that match the expected format while testing specific subsets of characters or substrings.
  
    - Efficient Testing of Character Sets:
  
  Using [abcd] targets a subset of potential token values, allowing the attacker to narrow down possibilities through timing measurements.
  The attacker can change [abcd] to other subsets (e.g., [efgh], [0123], etc.) to iteratively test the entire character space.
  
    - The beaf part is not fully clear yet
  
    - ReDoS-Like Behavior:
  
  The .? and {12} create optional matches and repeated patterns, increasing the complexity of the regex.
  This intentional complexity ensures that timing differences are more pronounced, making it easier to detect matches.

-
  ```
  <input
    type="text"
    pattern=".*(.?){12}[abcd]beaf"
    value="xxxxx...snip...xxxxx{{TOKEN}}"
  >
  <iframe></iframe>
  
  ```
  How the <iframe> Helps:
  
  The <iframe> element is counted as part of the window.frames or window.length property.
  When the browser parses and renders the HTML containing the <iframe>, the window.length value increases by 1 after the iframe is fully loaded.
  This allows the attacker to measure the time it takes for the iframe to "appear" in the DOM, which indirectly correlates to how long the browser takes to validate the pattern in the <input>.
