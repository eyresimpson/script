# coding=utf-8
import yagmail


class mailClient:
    username = ''
    password = ''
    host = ''
    port = ''
    serve = None

    # 用户名（必填），密码（必填），服务器地址（必填），端口号（必填），SSL（选填，默认开启）
    def __init__(self, username, password, host, port, SSL=True):
        self.serve = yagmail.SMTP(user=username, password=password, host=host, port=port, smtp_ssl=SSL)

    # 参数分别对应：收件人（string），主题（string），内容（string），附件（list[str(path),str(path)]）
    def sendmail(self, receiver, subject, contents, attachments):
        self.serve.send(receiver, subject, contents, attachments)


if __name__ == '__main__':
    passwd = input("请输入密码:")
    # 建立链接
    mail = mailClient('xxx@xxx.com', passwd, 'smtp.exmail.qq.com', '465')
    print('SMTP链接建立成功')
    # 测试邮件
    mail.sendmail('aaa@aaa.com', '这是主题', '一些内容',
                  [r'C:\Users\Tsos2\Desktop\xxx.xlsx'])
    print("邮件发送成功")
