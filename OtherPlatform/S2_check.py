import os
import time
import Main.Regular_log as RL

def start_test(device):
    start_time = time.time()
    total=0
    i = 0
    j = 0  # 中断flag
    k = 0  # 中断后连接flag

    while True:
        t1 = time.time()
        result = os.popen("ping %s" % device).read()
        if result.find("TTL") == -1:
            j = j + 1
            print("连接已断开")
            rl=RL.RegLog("jade21","0.09userdebug","netowrk standby 唤醒后wifi关闭","已进入network standby 模式")
            rl.send_mail()
        if result.find("TTL") != -1 and j > 5:
            k = k + 1
            print("连接已建立")
            if k > 3:
                print("盒子自动进入S0.5状态，测试中止")
                return -1
        i = i + 1
        t2 = time.time()
        print("已ping%d次，本次花费时间%f秒" % (i, t2 - t1))
        total=total+t2-t1
        if i > 10000:
            return 0


if __name__ == '__main__':
    res = start_test("192.168.1.102")
    if res == 0:
        print("测试成功")
    else:
        print("测试失败")
