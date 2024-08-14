## LITCTF: travserse

#### Working solutions: <br>
```curl http://litctf.org:31778/..%2Fflag.txt``` <br>
```└─$ curl -X GET "http://litctf.org:31778/?file=../../../flag.txt"``` <br>

While trying tis challenge i had tried different traversals but none worked. Even gobuster didnt yield anything. Turns out many web servers automatically
normalize URLs before processing them. This means they resolve ../ paths to prevent them from being used to escape the intended directory structure WITHOUT showing any sort of error. 
For example, if you try to access ../flag.txt, the server might normalize it to the root directory or the base path you started from, effectively blocking
access to files outside the intended directory. But when we use %2F, it bypasses input validation.

## LITCTF: scrainbow
This was a good scripting challege
First, you send a GET request to http://litctf.org:31780/data to get a list of color values (colors).Then, you retrieve the grid size n from http://litctf.org:31780/gridSize.

You build a 2D grid grid from the list of colors based on the grid size n.

The colors in the grid are sorted diagonally based on their HSL values.
The sorting function converts each hex color to RGB, then to HSL (hue, saturation, lightness), and sorts them by hue.

The goal is to transform the current grid into the sorted grid by generating a series of swap operations.It iterates through the grid, finding the correct positions of each color, and records the necessary swaps.

Finally, the list of moves is sent in a POST request to the server at http://litctf.org:31780/test.
If everything is implemented correctly, the server validates the moves and provide the flag.

The solve script used is at https://github.com/hbsmmsbh/ctf-writeup/blob/main/Lexington%20Informatics%20Tournament%20CTF/2024/web/scrainbow_solution.py


## CTFzone: Old but gold

In tis challenge i had been looking for direct comment ssti but turns out what we had to do was capture the comment request on burpsuite first. That then showed the endpoint as /api/v2. From the challenege description, it can be deduced that we need to go to v1 endpoint. When we go to /api/v1 then we are prompted to enter a username. Now this username field is the vulnerable field. When we put in a basic ssti payload, we get the flag.
