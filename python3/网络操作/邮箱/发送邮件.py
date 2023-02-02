# 首先必须要导入yagmail库
import yagmail

# 准备凭证（密码或密钥，此处使用密码）
# user 代表用户名
# password 代表邮箱密码
# host 代表发信服务器
yag = yagmail.SMTP(user="xxx@xxx.com", password="xxx", host='smtp.126.com')
# 发送邮件
yag.send(
    # to 收件人，如果一个收件人用字符串，多个收件人用列表即可
    to=['xxx@xxx.com', 'xxx@xxx.com'],
    # cc 抄送，含义和传统抄送一致，使用方法和to 参数一致
    cc='xxx@qq.com',
    # subject 邮件主题（也称为标题）
    subject='邮件主题',
    # contents 邮件正文
    contents='邮件正文',
    # attachments 附件，和收件人一致，如果一个附件用字符串，多个附件用列表
    attachments=[r'c://text.txt', r'd://mmp.exe'])
yag.close()
