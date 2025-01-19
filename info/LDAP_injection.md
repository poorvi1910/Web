## LDAP
LDAP stands for Lightweight Directory Access Protocol. It's a protocol that allows users to access and search for information and devices on a network. LDAP is used for user management and is a key part of many single sign-on solutions

## LDAP Injection

LDAP injection is similar to SQL injection and it arises when user-controllable data is copied in an unsafe way into an LDAP query that is performed by the application. <br>

If an attacker can inject LDAP metacharacters into the query, then they can interfere with the query's logic. Depending on the function for which the query is used, the attacker may be able to retrieve sensitive data to which they are not authorized, or subvert the application's logic to perform some unauthorized action.

## Some examples
- (cn=David*) matches anything with a common name beginning with the string David (the asterisk matches any character).
- (!(cn=David*)) matches anything where the common name does not start with the string David.
- (&(cn=D*)(cn=*Smith)) uses the AND logical operator, represented by the & symbol. Matches entries that start with the letter D and end with Smith.
- (|(cn=David*)(cn=Elisa*)) uses the OR logical operator, represented by the pipe symbol. Matches entries whose common name starts with one of the strings Dave or Elisa.

## Examples of test inputs:
- Wildcards (*): Test if * returns all results when used in inputs.
- Logical operators: Try injecting ) or (&) to modify query logic.
- Invalid characters: Test for characters that may disrupt LDAP syntax, such as (, ), |, or &.

## Access Control Bypass
Backend code: ```(&(USER=Uname)(PASSWORD=Pwd))``` <br>
Injection: ```john90)(&) ```<br>
Because of the & it bypasses the password input <br>

## Privilege Escalation
Injection: ```“Information)(security_level=*))(&(directory=documents”``` <br>
LDAP processes the first filter and ignores the second one. Using this a hacker see a list of documents that can usually only be accessed by users with all security levels <br>

## Information extraction
Injection: ```(|(type=Jeans)(uid=*))(type=T-Shirts))``` <br>
The LDAP server then shows all the jeans and user objects.

## Blind LDAP injection
A hacker can obtain all sorts of information by using TRUE/FALSE questions via Blind LDAP injections <br>
Backend code: ```(&(objectClass=Shirt)(type=Puma*))``` <br>
Injecton: ```*)objectClass=*))(&(objectClass=void ``` <br>

If there are no Puma shirts available, the user won’t see any icons<br>
After putting the payload, the query looks like ```(&(objectClass=*)(objectClass=*))(&(objectClass=void)(type=Puma*))``` <br>

Now the shirt icon shows to the client. How so? The objectClass=* filter always returns an object. An icon showing means the response is true. Otherwise the response is false. <br>

NOTE : ADAM LDAP doesn’t allow queries with two filters. This renders this injection useless<br>

An LDAP filter can be used to make a query that’s missing a logic operator (OR and AND). An injection like:

```value)(injected_filter```

Results in two filters (the second gets ignored while the first one gets executed in OpenLDAP implementations):

```(attribute=value)(injected_filter)```

## How to prevent

1. Applications should avoid copying user-controllable data into LDAP queries. 
2. The data should be strictly validated to prevent LDAP injection attacks by allowing only short alphanumeric strings to be copied into queries, and any other input should be rejected. At a minimum, input containing any LDAP metacharacters should be rejected
3. Characters to be blocked include ( ) ; , * | & = and whitespace.
4. Use a size limit to prevent the server from returning more items than expected. 
5. Avoid creating LDAP search filters by concatenating strings

### Payloads
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/LDAP%20Injection/README.md

### Resource used
https://brightsec.com/blog/ldap-injection/
