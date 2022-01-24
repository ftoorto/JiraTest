import time
import Main.Regular_log as Rl
import Main.Utils as STB


def start_test(device):
    i = 0
    while True:
        j = 0
        while not STB.adb_check(device):
            time.sleep(3)
            j = j + 1
            if j > 3:
                log = Rl.RegLog("Jade21", "0.09", "软重启2天", "测试内容：软重启\n已成功重启%d次，本次adb 连接失败，已尝试重连3次," % i)
                log.send_mail()
                return
        STB.reboot()
        i = i + 1
        print("已重启%d次" % i)
        if i > 30000:
            return


if __name__ == '__main__':
    start_test("192.168.1.104:5555")
