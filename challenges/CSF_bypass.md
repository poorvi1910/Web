We have been given a web page and openeing inspector we see the following

![image](https://github.com/poorvi1910/Web/assets/146640913/d1501f75-14a5-4bfb-bff2-9c7136110ebb)

CSP policy: 
default-src 'self' openlibrary.org;img-src 'self' raw.githubusercontent.com external-content.duckduckgo.com;base-uri 'self';font-src 'self' https: data:;form-action 'self';frame-ancestors 'self';object-src 'none';style-src 'self' https: 'unsafe-inline'

I first thought its an unsafe-inline vulnerability but i tried a few payloads and they didnt work

Then I went to https://csp-evaluator.withgoogle.com/ site 
![image](https://github.com/poorvi1910/Web/assets/146640913/b326cd9c-1224-4b9a-a50f-0079ceb1ee33)
Could not find any loop hole as such

Also logged as a new registered user and tried payloads in the add book section.

Since i am trying to log in as admin, as in the source file i put the username as admin and tried payloads in the password field but hae not been able to bypass till now
