from Main import Utils as STB
import time


def start_test(i, dev=None):
    power_on_off(i, dev)
    print("开关完成")
    # reboot(i,dev)
    # print("重启完成")


def power_on_off(i, dev=None):
    iteration = 0
    while True:
        iteration += 1
        print("第%d开关屏"%iteration)
        STB.power_on(dev, 10)
        STB.power_off(dev, 10)
        if iteration > i:
            break


def reboot(i, dev=None):
    iteration = 0
    while True:
        iteration += 1
        print("第%d次重启"%i)
        STB.adb_check(dev)
        STB.power_on(dev, 10)
        STB.reboot(dev)
        if iteration > i:
            break


if __name__ == '__main__':
    start_test(200000, "192.168.1.108:5555")
