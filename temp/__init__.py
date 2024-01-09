

from os import fdopen, system
from os import remove as delete_tempfile
from os import system as create_save
from os import path
from os import getenv

import tempfile


_name,_pkexec = "Name of the file is: %s","pkexec %s %s %s "

_save_directory='temporary.save'
_save='cp %s /tmp/%s/%s'







class temp:
	
	_proc=''
	
	
	def __create_savefile():
		
		tmp_dir, temp_file = path.split(filename)
		create_save (_save % (filename,_save_directory, '%s.save' % temp_file))
	
	def mv2(path, 
	deleted='true', user=''):
	
		proc= 'cp' if deleted == 'false' else 'mv' 
		
		system ('cd /tmp && mkdir %s > /dev/null 2>1' % _save_directory)
		"""setapp: kurtarma dizini /tmp/temporary.save """
		system (_pkexec % (proc, filename, path) if user == 'root' else "%s %s %s" % (proc, filename, path))
		"""path: usr/share/applications/test.desktop"""


		if proc == "cp":
			temp.__create_savefile()
	def delete(filename): 
			delete_tempfile(filename)
			
	class pkexec:
		def mv2(path, 
		deleted='true', user='root'):
			

			
			return temp.mv2(path, deleted, user)
def filetouch(content):
	global filename
	 
	tmp, filename = tempfile.mkstemp()
	with fdopen(tmp, 'w') as tmp: tmp.write(content)

	return temp, filename


