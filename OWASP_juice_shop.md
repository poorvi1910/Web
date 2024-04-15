# 1 star


# 2 star

# 3 star

Admin registration- Go to user registration frm the login page. Have burp running in bg. We see a post request on submitting the details, we see the attribute 'role' which is customer right now. We can add this role attribute as admin in a new request which we forward using repeater and the challenge is solved. 

Bjoern's favourite pet- If we google Bjoern Kimminich's name we get a youtube video https://www.youtube.com/watch?v=Lu0-kDdtVf4 in which he mentions the name of his cat as Zaya and email id as bjoern@owasp.org. Using this we can go to forgot password and log in.

Captcha bypass - When we enter feedback, fill in the captcha and hit enter we can see in the post request that our captcha, and comment are there. I sent it to repeater and sent the request again without a new capttcha and the response was successful. So i sent it to intruder while keeping the payload as null and count as 11 and started the attack which solved the challenge
