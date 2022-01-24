import datetime

import Main.qqmail as qqmail


class RegLog(object):
    def __init__(self, hardware, software, subject, msg, *logs):
        self.hw = hardware
        self.sw = software
        self.subject = subject
        self.msg = msg
        self.logs = logs

    def send_mail(self):
        subject = self.subject
        msg = "HW:" + self.hw + "\nSW:" + self.sw + "\n时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n"+self.msg
        logs = self.logs
        qqmail.send_mail(msg, subject, ['ye.yuan5@jgdt.com'], logs)


if __name__ == '__main__':
    a = RegLog("jade", "sw0.08", "测试标题","测试内容",'daily.log')
    a.send_mail()
