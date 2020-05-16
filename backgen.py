#pushrank

import json,requests,re,sys

try:
    print("""

--------------------------------------------------------------------
/$$$$$$$                      / $$       /$$ /$$          / $$   /$$      
| $$__  $$                    | $$      | $$|__/          | $$  /$$/      
| $$  \ $$  /$$$$$$   /$$$$$$$| $$   /$$| $$ /$$ /$$$$$$$ | $$ /$$/       
| $$$$$$$  |____  $$ /$$_____/| $$  /$$/| $$| $$| $$__  $$| $$$$$/        
| $$__  $$  /$$$$$$$| $$      | $$$$$$/ | $$| $$| $$  \ $$| $$  $$        
| $$  \ $$ /$$__  $$| $$      | $$_  $$ | $$| $$| $$  | $$| $$\  $$       
| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$ \  $$| $$| $$| $$  | $$| $$ \  $$      
|_______/  \_______/ \_______/|__/  \__/|__/|__/|__/  |__/|__/  \__/
                      BacklinkGenerator @2020
--------------------------------------------------------------------
powered by local-hunter.com
        """)
    if (sys.version_info.major == 3):
        site = input("[+] Nama Domain\t: ")
    else:
        site = raw_input("[+] Nama Domain\t: ")
    with open("backlink.json", "r") as file:
        data = json.loads(file.read())
        for backlink in data:
            url = backlink['url'].replace("local-hunter.com", site) #change your domain
            try:
                r = requests.get(url).status_code
            except KeyboardInterrupt:
                sys.exit()
            except:
                r = "Request Timed Out"
            
            print ("~ " + site + " | Success -> "+re.search('http:\/\/.*?\/', url).group(0).replace("/", "").replace("http:","")+ " status: "+str(r))
except:
    print("\n\n -> exit\n")
