import sqlite3
import time
import argparse
#################################################################				                                                
#this file was mades simply in order for me to learn more about sqlite3 #
#    improvements required:					#                            
#          ui presentation (colors/titles/lines etc)		#        
#    	     argparse options					#                            
#	   def Main() (the home page)				#                          
#	   security of code (sqlite3 & string formatting)	#            
#	   personalized database creation(def Create_Database)  #      	   
#	 							#                                                
#################################################################

def Create_Database():
	'''function used to create a database'''

	print '\n\033[1;32myoure in db\033[1;m'
	con = sqlite3.connect(str(raw_input('enter your db name: ')))
	cur = con.cursor()
	tblName = str(raw_input('enter your table name: '))

	# template database collumns, program doesn't allow personalized database creation (not yet anyway)
	common_collumn_names_1 = ['ID', 'Forename', 'Surname', 'Sex',
				 'D.o.b', 'Address', 'Tel', 'Mob', 'Email']


	common_collumn_names_2 = ['ID', 'NationalID', 'Forename', 'Surname', 'Sex', 
					'D.o.b', 'Address', 'Tel', 'Mob', 'Email']


	common_collumn_names_3 = ['ID', 'Patient number', 'Forename', 'Surname', 'Sex',
				 'D.o.b', 'Address', 'Tel', 'Mob', 'Email', 
				 'Emergency contact Name', 'Emergency contact Mob', 
				 'Emergency contact Address']


	common_collumn_names_4 = ['ID', 'Evidence numebr', 'Last accessed', 'Badge ID',
				'Name', 'Surname', 'Description']

	print '--\033[1;32moptions\033[1;m--\n'
	print '1. (General): ',common_collumn_names_1, '\n'
	print '2. (General 2):',common_collumn_names_2, '\n'
	print '3. (NHS): ',common_collumn_names_3, '\n'
	print '4. (Policing): ',common_collumn_names_4, '\n'

	opt = int(raw_input('\033[1;32mEnter option, using the option number:\033[1;m '))
	print '-' * 40

	if opt == 1:
		cur.execute('CREATE TABLE %s(ID CHAR(8), Forename TEXT, Surname TEXT, Sex CHAR(1), Dob CHAR(7), Adress TEXT, Tel INT, Mob INT, Email TEXT)' % tblName)

		num_of_enteries = int(raw_input('enter the number of entries you would like: '))
		time.sleep(1)
		print 'loading database structure...'
		time.sleep(2)
		print '\n'
		counter_1 = 0
		while counter_1 != num_of_enteries:

			ipt1 = str(raw_input('enter ID number	 : '))
			ipt2 = str(raw_input('enter forename	 : '))
			ipt3 = str(raw_input('enter surname	 : '))
			ipt4 = str(raw_input('enter sex    	 : '))
			ipt5 = str(raw_input('enter Date of birth: '))
			ipt6 = str(raw_input('enter Address	 : '))
			ipt7 = int(raw_input('enter Tel number	 : '))
			ipt8 = int(raw_input('enter Mob number	 : '))
			ipt9 = str(raw_input('enter Email address: '))
			print '\n'
			tup  = ((ipt1, ipt2, ipt3, 
				ipt4, ipt5, ipt6,
				ipt7, ipt8, ipt9,))	
			cur.execute('INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?)' % tblName, tup)
			con.commit()
		
			counter_1 += 1
	
	elif opt == 2:
		cur.execute('CREATE TABLE %s(ID CHAR(8), NationalID TEXT, Forename TEXT, Surname TEXT, Sex TEXT, Dob TEXT, Adress TEXT, Tel INT, Mob INT, Email TEXT)' % tblName)

		num_of_enteries = int(raw_input('enter the number of entries you would like: '))
		print '\n'
		counter_1 = 0
		while counter_1 != num_of_enteries:

			ipt1 = str(raw_input('enter ID number	 : '))
			ipt2 = int(raw_input('enter National ID  : '))
			ipt3 = str(raw_input('enter forename	 : '))
			ipt4 = str(raw_input('enter surname	 : '))
			ipt5 = str(raw_input('enter sex    	 : '))
			ipt6 = str(raw_input('enter Date of birth: '))
			ipt7 = str(raw_input('enter Address	 : '))
			ipt8 = int(raw_input('enter Tel number	 : '))
			ipt9 = int(raw_input('enter Mob number	 : '))
			ipt10 = str(raw_input('enter Email address: '))
			print '\n'
			tup  = ((ipt1, ipt2, ipt3, 
				ipt4, ipt5, ipt6,
				ipt7, ipt8, ipt9,))	
			cur.execute('INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?,?)' %tblName, tup)
			con.commit()
	
			counter_1 += 1

	elif opt == 3:
		cur.execute('CREATE TABLE %s(ID CHAR(8), PatientNumber INT, Forename TEXT, Surname TEXT, Sex TEXT, Dob TEXT, Adress TEXT, Tel INT, Mob INT, Email TEXT, EmergencyContactName TEXT, EmergencyContactMob INT, EmergencyContactAddress TEXT)' % tblName)
		
		num_of_enteries = int(raw_input('enter the number of entries you would like: '))
		print '\n'
		counter_1 = 0
		while counter_1 != num_of_enteries:

			ipt1 = str(raw_input('enter ID number	 : '))
			ipt2 = int(raw_input('enter Patient number: '))
			ipt3 = str(raw_input('enter forename	 : '))
			ipt4 = str(raw_input('enter surname	 : '))
			ipt5 = str(raw_input('enter sex    	 : '))
			ipt6 = str(raw_input('enter Date of birth: '))
			ipt7 = str(raw_input('enter Address	 : '))
			ipt8 = int(raw_input('enter Tel number	 : '))
			ipt9 = int(raw_input('enter Mob number	 : '))
			ipt10 = str(raw_input('enter Email address: '))
			ipt11 = str(raw_input('enter Emergency Contact name : '))
			ipt12 = int(raw_input('enter Emergency Contact mob  : '))
			ipt13 = str(raw_input('enter Emergecny Contact address: '))
			print '\n'
			tup  = ((ipt1, ipt2, ipt3, 
				ipt4, ipt5, ipt6,
				ipt7, ipt8, ipt9, ipt10))	
			cur.execute('INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)' % tblName, tup)
			con.commit()
	
			counter_1 += 1

	
	elif opt == 4:
		cur.execute('CREATE TABLE %s(ID CHAR(8), EvidenceNumber INT, LastAccessed TEXT, BadgeID TEXT, Name TEXT, Surname TEXT, Description TEXT)' % tblName)
		
		num_of_enteries = int(raw_input('enter the number of entries you would like: '))
		print '\n'
		counter_1 = 0
		while counter_1 != num_of_enteries:

			ipt1 = str(raw_input('enter ID number	 : '))
			ipt2 = int(raw_input('enter Evidence number  : '))
			ipt3 = str(raw_input('enter Last accessed : '))
			ipt4 = str(raw_input('enter Badge ID: '))
			ipt5 = str(raw_input('enter Name 	 : '))
			ipt6 = str(raw_input('enter Surname: '))
			ipt7 = str(raw_input('enter Description	 : '))
			print '\n'
			tup  = ((ipt1, ipt2, ipt3, 
				ipt4, ipt5, ipt6,
				ipt7))	
			cur.execute('INSERT INTO %s VALUES(?,?,?,?,?,?,?)' %tblName, tup)
			con.commit()
		
			counter_1 += 1

	else:
		print 'sorry you\'ve failed to enter a valid number.'


def Edit_Database():

	print '\n\033[1;32myou\'re in edit db\033[1;m'

	options = ['add entry', 'remove entry', 'modify entry']
	count = 1
	for opts in options:
		print '%d.' % count, opts
		count += 1
 
	user_option = str(raw_input('\nenter above option: '))


	if user_option == '1' or user_option == 'add entry' or user_option == 'add':
		print '\033[1;32mwelcome to add entry\033[1;m'

		con = sqlite3.connect(str(raw_input('\nenter db file to open, to edit: ')))
		cur = con.cursor()
		table = str(raw_input('enter the table name to add to: '))
		print '-' * 35

		cols = []
		for things in cur.execute('PRAGMA table_info(%s)' % table):
		# things would include: collumn names, collumn data types, values, data etc 
			for i in things:
				if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
					pass			
				elif i == 6 or i == 7 or i == 8 or i == 9 or i == 10 or i == 11:
					pass
				elif i == 12 or i == 13 or i == 14 or i == 14 or i == 15 or i == 16:
					pass
				elif i == None:
					pass
				else:
					# extract only collumn names and data types i.e. TEXT INT CHAR() etc.
					#i = collumn_name, collumn_name_data_type...
					cols.append(i)
		collumns = []		
		counter_1 = 0
		counter_2 = 1

		while counter_1 != len(cols):
			collumns.append((cols[counter_1], cols[counter_2]))
			counter_1 += 2
			counter_2 += 2
			#where cols will look something like: [u'ID', u'INT', u'NAME', u'TEXT] etc
			#collumns is to basically 'tupalize' e.g. (ID with INT), and (NAME with TEXT) etc
			
		answers = []
		#time to retrieve user answers
		counter_3 = 0
		while counter_3 != len(collumns):

			for cols in collumns:
				print collumns[counter_3],
				i = raw_input(': ')
				answers.append(i)
				counter_3 += 1	 

		Q = [] #Question mark list
		counter_4 = 0
		while counter_4 != len(collumns):

			for items in collumns:
				Q.append('?')		
				counter_4 += 1

			if counter_4 == len(collumns):
				num = int(len(Q))-1				
				question_mark = '?,' * num

				counter_5 = 0
				while counter_5 != len(answers):
					counter_5 += 1		

					if counter_5 == len(answers):
						tup = tuple(answers)
						print tup
						cur.execute('INSERT INTO %s VALUES(%s?)' % (table, question_mark), tup)
						con.commit()

	elif user_option == '2' or user_option == 'remove entry' or user_option == 'remove' or user_option == 'rm':
		print 'welcome to remove entry'
		
		con = sqlite3.connect(str(raw_input('enter db file to open, to edit: ')))
		cur = con.cursor()

		table = str(raw_input('enter the table name to remove from: '))
		iD = str(raw_input('enter the ID: '))
		print '-' * 35

		cur.execute('SELECT * FROM %s WHERE Id=:id_param' % table, {'id_param': iD})
		print 'Do you wish to remove:', cur.fetchone()
		response = raw_input('> ')

		if response == '' or response == 'n' or response == 'N':
			print 'logging you off session'
			time.sleep(0.5)
			print 'logged off'
	
		else:
			cur.execute('DELETE FROM %s WHERE Id=:id_param' % table, {'id_param': iD})
			con.commit()
			time.sleep(0.5)
			print 'row deleted.'
	
	elif user_option == '3' or user_option == 'modify entry' or user_option == 'mod':
		print 'switching values using entry id numbers.\n'

		con = sqlite3.connect(str(raw_input('enter db file to open, to edit: ')))
		cur = con.cursor()

		table = str(raw_input('enter the table name to edit: '))
		collumn = str(raw_input('enter the collumn name to edit: '))
		IdNum = int(raw_input('enter the idNum: '))
		print '-' * 35

		cur.execute('SELECT * FROM %s WHERE Id=:id_Param' % table, {'id_Param': IdNum})

		old_data = []
		print 'old data: ',
		for data in cur.fetchall():
			print data,
			old_data.append(data) 
	
		data_change = raw_input('\nenter new data: ')
		time.sleep(0.5)
		print '\n\033[1;30mupdating database...\033[1;m',
		time.sleep(0.5)

		cur.execute('UPDATE %s SET %s=:new_data WHERE Id=:id_Param' % (table, collumn), {'new_data': data_change, 'id_Param': IdNum})
		con.commit()

		cur.execute('SELECT * FROM %s WHERE Id=:id_Param' % table, {'id_Param': IdNum})
		con.commit()
		time.sleep(1)
	
		print 'database updated!'
	

def View_Database():
	'''function will be used to enable user to view the data base data '''
	print '\n\033[1;32myou\'ve entered vdb\033[1;m'
	con = sqlite3.connect(raw_input('enter database name to open: '))
	cur = con.cursor()
	table = raw_input('enter the table name from: ' )
	cur.execute('SELECT * FROM %s' % table)
	data = cur.fetchall()
	print 'data from %r' % table
	print '-' * 26
	for row in data:
		print row

def Main():
	options = {'Create database': Create_Database,
		  'View database': View_Database,
		  'Edit database': Edit_Database}
	cntr = 0
	for opts in options:
		cntr += 1
		print '%d.' % cntr, opts
	print '-' * 18

	uipt = str(raw_input('enter option: '))
	keys = []
	for key,item in options.items():
		keys.append(key)

	if uipt == str(1) or uipt == keys[0] or uipt == 'create' or uipt == 'c':
		options['Create database']()
	
	elif uipt == str(3) or uipt == keys[2] or uipt == 'view' or uipt == 'v':
		options['View database']()

	elif uipt == str(2) or uipt == keys[1] or uipt == 'edit' or uipt == 'e':
		options['Edit database']()
	
	else:
		print '''\n\033[1;32myou can\'t use chopsticks? GO HOME! :(\033[1;m\n'''


if __name__ == '__main__':
	Main()
