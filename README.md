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
$ cd Open-Redirect-tool
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
$ python uDork.py -h
       _____             _    
      |  __ \           | |   
 _   _| |  | | ___  _ __| | __
| | | | |  | |/ _ \| '__| |/ /
| |_| | |__| | (_) | |  |   < 
 \__,_|_____/ \___/|_|  |_|\_\ v.2020.03.13
		by M3n0sD0n4ld - (@David_Uton)

----------------------------------------------------------------------------------------------------
usage: uDork.py [-h] [-d DOMAIN] [-f FILE] [-v verbose]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain Domain or IP address.
  -f FILE, --file FILE  Use your own personalized list of dorks.
  -v VERBOSE, --verbose used to find which dorks are not successed 
```

# Thanks:

Many Thanx s0md3v for goop, very good job! https://github.com/s0md3v/goop
Many Thanx M3n0sD0n4ld for uDork my inspire script https://github.com/m3n0sd0n4ld/uDork



