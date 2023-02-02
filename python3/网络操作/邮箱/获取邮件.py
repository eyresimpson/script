import zmail

server = zmail.server('xxx@xxx.com', '123', config='qq')

mail = server.get_mail(7)
print(server.stat())
zmail.show(mail)
print(mail['Subject'])
zmail.save_attachment(mail, target_path=r"D:\Data", overwrite=True)
zmail.save(mail)
