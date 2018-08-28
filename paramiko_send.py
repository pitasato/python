import paramiko



s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect("bartex1996.e-kei.pl",22,username='bartex1996',password='FErrari12',timeout=4)

sftp = s.open_sftp()
sftp.put('c:\\test.txt', 'xfile.txt')
