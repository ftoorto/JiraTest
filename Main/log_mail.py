import datetime
import smtplib

import Main.qqmail as qqmail


def error(msg):
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mail_subject = 'Error!!! ' + dt
    mail_msg = "Error!" + '\n' + '报错时间：' + dt + '\n' + msg
    try:
        qqmail.send_mail(mail_msg, mail_subject, ['ye.yuan5@jgdt.com'])
    except smtplib.SMTPException:
        _fail('Error '+dt+msg)


def waring(msg):
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mail_subject = 'Warning!! ' + dt
    mail_msg = "Warning!" + '\n' + '警告时间：' + dt + '\n' + msg
    qqmail.send_mail(mail_msg, mail_subject, ['ye.yuan5@jgdt.com'])


def info(msg):
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mail_subject = 'Information! ' + dt
    mail_msg = "Information!" + '\n' + '消息时间：' + dt + '\n' + msg
    qqmail.send_mail(mail_msg, mail_subject, ['ye.yuan5@jgdt.com'])


def _fail(msg):
    with open("daily.log",'a+') as f:
        f.write(msg)