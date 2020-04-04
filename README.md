# open redirect tool - Google Hacking Tool

###### Author: schizo
###### Twitter: [@isch1zo](https://twitter.com/isch1zo)
###### Blog: [ischizo](https://ischizo.com/)

# Description:

open redirect is a script written in Python that uses advanced Google search techniques to obtain urls that very often has open redirect vulnerablity

# You need to have goop installed
```
pip install goop
```

# Download and install:
```
$ git clone https://github.com/dbis0/Open-Redirect-tool
$ cd Open-Redirect-tool/
- Open the file open_redirect.py and write inside this line:
```
cookie = 'YOUR FACEBOOK COOKIES HERE'
```
$ python open_redirect.py -d [Target Domain] -f [Dorks file]
```
# Important!!!
- For the tool to work, you must configure open_redirect.py with your Facebook cookie.
- You must also be logged in to Facebook on the computer you are using uDork WITHOUT logging out.

## Steps to obtain the cookie and configure the cookie
- Login to facebook.com
- Press in your browser control + shift + K (Firefox) o control + shift + J (Google Chrome) to go to console.
- Write document.cookie in the console and copy the cookies "c_user = content" and "xs = content" to the variable "cookie" inside the file "open_redirect.py""
```
cookie = 'c_user=XXXXXX; xs=XXXXXX'
```
Note: If the "xs" cookie does not appear, [follow these steps](https://gist.github.com/sqren/0e4563f258c9e85e4ae1).
- Save and remember, you must NOT log out of Facebook or you will have to do these steps again.


# Use:

## Menu

```
# python open_redirect.py -h

                        ,---,                                     
                      ,--.' |      ,--,                           
                      |  |  :    ,--.'|          ,----,   ,---.   
  .--.--.             :  :  :    |  |,         .'   .`|  '   ,'\  
 /  /    '     ,---.  :  |  |,--.`--'_      .'   .'  .' /   /   | 
|  :  /`./    /     \ |  :  '   |,' ,'|   ,---, '   ./ .   ; ,. : 
|  :  ;_     /    / ' |  |   /' :'  | |   ;   | .'  /  '   | |: : 
 \  \    `. .    ' /  '  :  | | ||  | :   `---' /  ;--,'   | .; : 
  `----.   '   ; :__  |  |  ' | :'  : |__   /  /  / .`||   :    | 
 /  /`--'  /'   | '.'||  :  :_:,'|  | '.'|./__;     .'  \   \  /  
'--'.     / |   :    :|  | ,'    ;  :    ;;   |  .'      `----'   
  `--'---'   \   \  / `--''      |  ,   / `---'                   
              `----'              ---`-'                          
                                                                  
twitter:@isch1zo
----------------------------------------------------------------------------------------------------
Usage: open_redirectGIT.py [options]

Options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain=DOMAIN
                        Enter Target Domain
  -f DORKS, --dorks=DORKS
                        Enter Dorks
  -v, --verbose         Print more data
```
## Scan
```
# python open_redirect.py -d [Target Domain] -f dorks.txt

                        ,---,                                     
                      ,--.' |      ,--,                           
                      |  |  :    ,--.'|          ,----,   ,---.   
  .--.--.             :  :  :    |  |,         .'   .`|  '   ,'\  
 /  /    '     ,---.  :  |  |,--.`--'_      .'   .'  .' /   /   | 
|  :  /`./    /     \ |  :  '   |,' ,'|   ,---, '   ./ .   ; ,. : 
|  :  ;_     /    / ' |  |   /' :'  | |   ;   | .'  /  '   | |: : 
 \  \    `. .    ' /  '  :  | | ||  | :   `---' /  ;--,'   | .; : 
  `----.   '   ; :__  |  |  ' | :'  : |__   /  /  / .`||   :    | 
 /  /`--'  /'   | '.'||  :  :_:,'|  | '.'|./__;     .'  \   \  /  
'--'.     / |   :    :|  | ,'    ;  :    ;;   |  .'      `----'   
  `--'---'   \   \  / `--''      |  ,   / `---'                   
              `----'              ---`-'                          
----------------------------------------------------------------------------------------------------                                                                 
twitter:@isch1zo
[*] Scanning is established, it may takes a minutes ...


[+] Trying: site:[Target Domain] AND inurl:url

[+] Trying: site:[Target Domain] AND inurl:/?page=
....

[+] Scanning Done 

[1] Interesting one >> http://[Target Domain]/redirect.php%3Furl%3Dhttp%253A%252F%252F***%252F***

[2] Interesting one >> http://[Target Domain]/redirect.php%3Furl%3Dhttp%253A%252F%252F***%252F***%252F***
...
[25] https://[Target Domain]/***/***.html
```
## Scan with verbose
```
# python open_redirect.py -d [Target Domain] -f dorks.txt -v

                        ,---,                                     
                      ,--.' |      ,--,                           
                      |  |  :    ,--.'|          ,----,   ,---.   
  .--.--.             :  :  :    |  |,         .'   .`|  '   ,'\  
 /  /    '     ,---.  :  |  |,--.`--'_      .'   .'  .' /   /   | 
|  :  /`./    /     \ |  :  '   |,' ,'|   ,---, '   ./ .   ; ,. : 
|  :  ;_     /    / ' |  |   /' :'  | |   ;   | .'  /  '   | |: : 
 \  \    `. .    ' /  '  :  | | ||  | :   `---' /  ;--,'   | .; : 
  `----.   '   ; :__  |  |  ' | :'  : |__   /  /  / .`||   :    | 
 /  /`--'  /'   | '.'||  :  :_:,'|  | '.'|./__;     .'  \   \  /  
'--'.     / |   :    :|  | ,'    ;  :    ;;   |  .'      `----'   
  `--'---'   \   \  / `--''      |  ,   / `---'                   
              `----'              ---`-'                          
----------------------------------------------------------------------------------------------------                                                                  
twitter:@isch1zo
[*] Scanning is established, it may takes a minutes ...


[+] Trying: site:[Target Domain] AND inurl:url

[+] Trying: site:[Target Domain] AND inurl:/?page=

[-] No result for this dork >> site:[Target Domain] AND inurl:/?page=

[+] Trying: site:[Target Domain] AND inurl:/url?url=

[+] Scanning Done 
```
# Thanks:

Many Thanx s0md3v for goop, very good job! https://github.com/s0md3v/goop
Many Thanx M3n0sD0n4ld for uDork my inspire script https://github.com/m3n0sd0n4ld/uDork



