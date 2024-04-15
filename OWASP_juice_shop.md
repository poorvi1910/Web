# 1 star



# 2 star



# 3 star

Admin registration- Go to user registration frm the login page. Have burp running in bg. We see a post request on submitting the details, we see the attribute 'role' which is customer right now. We can add this role attribute as admin in a new request which we forward using repeater and the challenge is solved.

Bjoern's favourite pet- If we google Bjoern Kimminich's name we get a youtube video https://www.youtube.com/watch?v=Lu0-kDdtVf4 in which he mentions the name of his cat as Zaya and email id as bjoern@owasp.org. Using this we can go to forgot password and log in.

Captcha bypass - When we enter feedback, fill in the captcha and hit enter we can see in the post request that our captcha, and comment are there. I sent it to repeater and sent the request again without a new capttcha and the response was successful. So i sent it to intruder while keeping the payload as null and count as 11 and started the attack which solved the challenge

CSRF - 

Database schema - 

Deluxe Fraud - 

Forged feedback - We can intercept the request in burp, change the user id to some other number and forward the request and the challenge is solved.

Forged review - We can intercept the request in burp, change the email id to someone else's like jim if we are in the admin account and forward the request and the challenge is solved.

GDPR data erasure - 

Login Amy - 

Login Bender - If we look through juice shop product reviews, we find bender's email id. Going to login page. Adding a "' --" after the email id, we nullify whatever is comming after the email id in the sql query which rules out the password field and we can login

Login Jim - If we look through juice shop product reviews, we find jim's email id. Going to login page. Adding a "' --" after the email id, we nullify whatever is comming after the email id in the sql query which rules out the password field and we can login

Manipulate Basket - 

Mint the Honey Pot - 

Payback Time -

Privacy Policy Inspection -

Product Tampering -
 
Reset Jim's Password - If we look at jim's reviews, we see he mentions a 'replicator','tricorder' and 'Starfleet'. All of these are a part of star trek. if we search jim star trek, we get a 'James T kirk'. If we oen the wikipedia page, we see his brother is George Smauel Kirk. Hence inpuuting Samuel as the answer, we are able to rest password.

Upload Size - Upload a file larger than 100 kB. - If we upload a pdf doc that is smaller than 100 kb and analyze the request in burp, we see the entire pdf contents. Hence if we create a larger file, copy paste its contents(after opening in notepad) intead of the orginal document ater sending request to repeater and sending this we can solve the challenge

Upload Type - If we upload a pdf doc that is smaller than 100 kb and analyze the request in burp, we see the entire pdf contents. Hence if we create a jpg file, copy paste its contents(after opening in notepad) intead of the orginal document, change filename and content type to jpg ater sending request to repeater and sending this we can solve the challenge
