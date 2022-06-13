from Main import Utils as STB

import time


def start_test(dev, mac, i):
    times = 0
    while True:
        STB.power_off(dev)
        time.sleep(1200)
        recheck_times = 0
        while STB.adb_check(dev):
            recheck_times += 1
            time.sleep(60)
            if recheck_times > 3:
                print("无法进入network standby")
                return
        STB.wol(dev, mac)
        while not STB.adb_check(dev):
            recheck_times += 1
            time.sleep(60)
            if recheck_times > 3:
                print("无法重连")
                return
        times += 1
        print("network 唤醒成功%d次" % times)
        if times > i:
            print("测试完成")


if __name__ == '__main__':
    start_test("192.168.1.108", "ec937d262ec8",50)
