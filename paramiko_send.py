import paramiko



s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect("nazwaserwera",22,username='',password='',timeout=4)

sftp = s.open_sftp()
sftp.put('c:\\test.txt', 'xfile.txt')
