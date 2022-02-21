import sys
import time
from Main import Utils as STB


def start_test(device):
    try:
        times = 0
        while True:
            times = times + 1
            for j in range(15):
                if not STB.adb_check(device):
                    return -1
                else:
                    # 打开settings
                    STB.settings()
                    time.sleep(3)
                    # 进入settings菜单
                    for i in range(5):
                        STB.down()
                    STB.up()
                    STB.ok()
                    # 进入display菜单
                    # 也有可能是10
                    # jade 是11

                    for i in range(11):
                        STB.down()
                    STB.ok()
                    # 选择resolution
                    STB.ok()
                    l = j % 15
                    if l == 0:
                        STB.ok()
                    else:
                        for k in range(l):
                            STB.down()
                            # 选定
                        STB.ok()
                    STB.down()
                    STB.ok()

                    # 返回桌面
                    # STB.back()
                    # STB.back()
                    # STB.back()
                    # STB.back()
                    # 准备重启,android 10 以上
                    STB.right()
                    STB.ok()
                    time.sleep(120)
                    print("第", times, "次重启")
                    if times > 1000:
                        return
    except KeyboardInterrupt:
        print("测试中断")


if __name__ == "__main__":
    # dev = sys.argv[1]
    dev = "192.168.1.107:5555"
    start_test(dev)
