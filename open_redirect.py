import optparse
import colorama
from colorama import Fore, Style
from goop import goop
from itertools import imap

def search(domain, dorks, verbios):
    banner()
    domain = domain
    dorks = open(dorks, "r")
    payloads = dorks.readlines()
    final = []
    print(Fore.CYAN+"[*] Scanning is established, it may takes a minutes ...\n\n")
    for payload in payloads:
        dork = "site:"+domain+" AND inurl:"+payload
        result = goop.search(dork, cookies, page=10, full=True)
        print(Fore.MAGENTA+"[+] Trying: "+dork)
        if result:
            for each in result: 
                final.append(str(result[each]['url']))
        if verbios:
            print(Fore.RED+"[-] No result for this dork >> "+dork)
    print(Fore.GREEN+"[+] Scanning Done \n")
    dorks.close()
    if len(final) == 0:
        print(Fore.RED+"[-] No result for your scan, Try Harder! U can Do it")
    else:
        x=1
        for i in final:
            if(CheckInterest(i)):
                print(Fore.YELLOW+"["+str(x)+"] "+"Interesting one >> "+ i + "\n")
                x=x+1
            else:
                print(Fore.BLUE+"["+str(x)+"] "+i+"\n")
                x=x+1


def CheckInterest(checkit):
    white_list = ['=http','%3dhttp','%3dhttps','=https','%3D%2F','=/']
    for i in white_list:
        if i.lower() in checkit.lower():
            return True
    return False

def banner():
    schizo="""                        ,---,                                     
                      ,--.' |      ,--,                           
                      |  |  :    ,--.'|          ,----,   ,---.   
  .--.--.             :  :  :    |  |,         .'   .`|  '   ,'\  
 /  /    '     ,---.  :  |  |,--.`--'_      .'   .'  .' /   /   | 
|  :  /`./    /     \ |  :  '   |,' ,'|   ,---, '   ./ .   ; ,. : 
|  :  ;_     /    / ' |  |   /' :'  | |   ;   | .'  /  '   | |: : 
 \  \    `. .    ' /  '  :  | | ||  | :   `---' /  ;--,'   | .; : 
  `----.   \'   ; :__  |  |  ' | :'  : |__   /  /  / .`||   :    | 
 /  /`--'  /'   | '.'||  :  :_:,'|  | '.'|./__;     .'  \   \  /  
'--'.     / |   :    :|  | ,'    ;  :    ;;   |  .'      `----'   
  `--'---'   \   \  / `--''      |  ,   / `---'                   
              `----'              ---`-'                          
                                                                  """
    twitter="twitter:@isch1zo"
    print(Fore.BLUE+"\n"+schizo)
    print(Fore.RED+twitter)
    
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-d", "--domain", dest="domain", help="Enter Target Domain")
    parser.add_option("-f", "--dorks", dest="dorks", help="Enter Dorks")
    parser.add_option("-v", "--verbose", dest="verbose", help='Print more data', action='store_true')
    #Verbose
    (options, arguments) = parser.parse_args()
    if not options.domain:
        parser.error("[-] Please specify a domain, use --help for more info.")
    elif not options.dorks:
        parser.error("[-] Please specify a dorks file, use --help for more info.")
    else:
        return options


cookies = "c_user=100049340122491; xs=16%3A3HnCwkJVltq31g%3A2%3A1585934121%3A-1%3A-1;"
options = get_arguments()
search(options.domain, options.dorks, options.verbose)
