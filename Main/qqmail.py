import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


def send_mail(mail_text, mail_subject, receivers=['ye.yuan5@jgdt.com', '774898142@qq.com'], logs=None):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "2748652229@qq.com"  # 用户名
    mail_pass = "qxxicizxfjardcdd"  # 口令

    def __format_addr(addr):
        # 解析邮件地址，以保证邮有别名可以显示
        return formataddr(parseaddr(addr))

    sender = '2748652229@qq.com'
    message = MIMEMultipart()
    message.attach(MIMEText(mail_text,'plain','utf-8'))
    reformat_addr_list = []
    message['From'] = __format_addr(sender)
    for receiver in receivers:
        real_address = __format_addr(receiver)
        reformat_addr_list.append(real_address)
    message['To'] = ",".join(reformat_addr_list)

    message['Subject'] = Header(mail_subject, 'utf-8')
    if logs:
        for log in logs:
            att = MIMEText(open(log, 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename={}'.format(log.split("/")[-1])
            message.attach(att)

    try:
        smtp_server = smtplib.SMTP_SSL(mail_host, 465)
        smtp_server.login(mail_user, mail_pass)
        smtp_server.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == "__main__":
    send_mail("第二封邮件", "邮件标题", ["ye.yuan5@jgdt.com"])
