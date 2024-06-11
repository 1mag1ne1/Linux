# coding = utf-8



import smtplib
from email.header import Header
from email.mime.text import MIMEText

from config import gol


class SendMail(object):
    def __init__(self):
        """ 初始化邮箱模块 """
        try:
            self.mail_host = gol.get_value("mail_host")  # 邮箱服22务器
            self.mail_port = gol.get_value("mail_port")  # 邮箱服务端端口
            self.mail_user = gol.get_value("mail_user")  # 邮箱用户名
            self.mail_pwd = gol.get_value("mail_pwd")  # 邮箱密码
            self.mail_receivers = gol.get_value("mail_receivers").split(',')  # 收件人,以逗号分隔成列表
            smtp = smtplib.SMTP()
            smtp.connect(self.mail_host, self.mail_port)
            smtp.login(self.mail_user, self.mail_pwd)
            self.smtp = smtp
            print(self.smtp)
        except:
            print('发邮件---->初始化失败!请检查用户名和密码是否正确!')
            raise

    def send_mails(self, content):
        """ 发送邮件 """
        try:
            print("content:"+ content)
            message = MIMEText(content, 'plain', 'utf-8')
            message['From'] = "Yi <2567250824@qq.com>"
            message['To'] = Header("receiver", 'utf-8')
            subject = '日志信息'
            message['Subject'] = Header(subject, 'utf-8')
            self.smtp.sendmail(self.mail_user, self.mail_receivers, message.as_string())
            print('发送邮件成功!')
        except Exception as e:
            print('发邮件---->失败!原因:', e)
            raise

    def mail_close(self):
        """ 关闭邮箱资源 """
        self.smtp.close()
