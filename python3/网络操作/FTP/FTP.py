from ftplib import FTP

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('192.168.100.128', 22)
ftp.login('root', '123123')
print(ftp.getwelcome())
ftp.dir()
