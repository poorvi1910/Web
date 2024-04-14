We have been given a web page and openeing inspector we see the following

![image](https://github.com/poorvi1910/Web/assets/146640913/d1501f75-14a5-4bfb-bff2-9c7136110ebb)

CSP policy: 
default-src 'self' openlibrary.org;img-src 'self' raw.githubusercontent.com external-content.duckduckgo.com;base-uri 'self';font-src 'self' https: data:;form-action 'self';frame-ancestors 'self';object-src 'none';style-src 'self' https: 'unsafe-inline'

I first thought its an unsafe-inline vulnerability but i tried a few payloads and they didnt work

Then I went to https://csp-evaluator.withgoogle.com/ site 
![image](https://github.com/poorvi1910/Web/assets/146640913/b326cd9c-1224-4b9a-a50f-0079ceb1ee33)
Could not find any loop hole as such

Also logged as a new registered user and tried payloads in the add book section.

## FRESH APPROACH

I Logged on to the website as a new user, performed a delete operation, copied as curl and put it into https://curlconverter.com/ to make my python payload script.<br>
I then looked at the source code and in the script.js file, we can see that there has been usage of innerHTML which lets us know that the book adding field is susceptible to xss. <br>
So now we need to make a payload that would perform xss (while keeping in mind the csp policy used) that would give us the books table that only admin can access and has our flag and send it using the python script

