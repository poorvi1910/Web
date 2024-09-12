### Lost Pyramid

- **Few observations**

  - After pasting the jwt token, in jwt.io we could see that the algorithm used was eddsa.
  - We also see that at the endpoint ```/scarab_room``` there was an input box. Next lookng at the source code, there was a safelist provided
```
['{', '}', '𓁹', '𓆣', '𓀀', '𓀁', '𓀂', '𓀃', '𓀄', '𓀅', '𓀆', '𓀇', '𓀈', '𓀉', '𓀊',
                  '𓀐', '𓀑', '𓀒', '𓀓', '𓀔', '𓀕', '𓀖', '𓀗', '𓀘', '𓀙', '𓀚', '𓀛', '𓀜', '𓀝', '𓀞', '𓀟',
                  '𓀠', '𓀡', '𓀢', '𓀣', '𓀤', '𓀥', '𓀦', '𓀧', '𓀨', '𓀩', '𓀪', '𓀫', '𓀬', '𓀭', '𓀮', '𓀯',
                  '𓀰', '𓀱', '𓀲', '𓀳', '𓀴', '𓀵', '𓀶', '𓀷', '𓀸', '𓀹', '𓀺', '𓀻']
```
The curly brackets being allowed let to ssti vuln.
  -  To access the kings_lair template which contained our flag,the jwt payload needed the urrent date variable to be equal to kingsday and also the role field  had to be equal to 'royalty'
```
if decoded.get("CURRENT_DATE") == KINGSDAY and decoded.get("ROLE") == "royalty":
            return render_template('kings_lair.html')
```

- **Going ahead**
  - We had to get the value of kinsday
  - Find a way to create our own jwt because eddsa required public and private keys both
  - change the jwt and get access to kings_lair template
 
- **Solve**
  - ```{{KINGSDAY}}``` in the ssti field. which basically means we are trying to print the kingsday variable, prints it out and we get the value of kingsday as ```03_07_1341_BC```
  - 
