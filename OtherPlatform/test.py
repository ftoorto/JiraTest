import time
from Main import Utils as STB
import os


def temp_test(address="192.168.1.107:5555", i=50):
    j = 0
    time_list = []
    while True:
        time_now = time.time()
        if STB.adb_check(address, False, False):
            print("adb 依然可连接")
            time.sleep(30)
        else:
            while not STB.adb_check(address, False, False):
                os.system("WolCmd e037178b2388 192.168.1.107 255.255.255.0 4343")
                print("尝试唤醒")
                time.sleep(3)
            time_then = time.time()
            time_list.append(time_then - time_now)
            print("本次standby持续", (time_then - time_now), "秒")
            print("唤醒STB")
            STB.power_off(5)
            print("Standby STB")
            j = j + 1
            print("第", j, "次networkstandby")
            if j > i:
                print("全部standby时间:" + time_list)
                print("平均standby时间" + sum(time_list) / j)
                return


if __name__ == "__main__":
    temp_test("192.168.1.107:5555")
