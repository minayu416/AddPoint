import os,sys
from shutil import copyfile
import csv, sqlite3
from datetime import datetime, timedelta

def historycopy():
	copyfile(os.getenv("APPDATA") + '\..\Local\Google\Chrome\User Data\Default\history', os.getenv("APPDATA") + '\..\history1')

def historycatch():
	connection = sqlite3.connect(os.getenv("APPDATA") + "\..\history1")
	connection.text_factory = str
	cur = connection.cursor()
	output_file = open('chrome_history.csv', 'wb')
	csv_writer = csv.writer(output_file)
	headers = ('URL', 'Title', 'Visit Count', 'Date (GMT)')
	csv_writer.writerow(headers)
	epoch = datetime(1601, 1, 1)
	for row in (cur.execute('select url, title, visit_count, last_visit_time from urls')):
		row = list(row)
		url_time = epoch + timedelta(microseconds=row[3])
		row[3] = url_time
		csv_writer.writerow(row)
		
def readcatch():
	with open('chrome_history.csv') as fs:
		lastN=list(fs)[-50:]
	file=open('filter.pickle','w')
	file.write(','.join(str(num)for num in lastN))
	file.write('\n')
	file.close()
	


historycopy()
historycatch()
readcatch()
	
sys.exit()
