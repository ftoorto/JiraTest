import sys
import time
from Main import Utils as STB


def start_test(device):
    try:
        times = 0
        while True:
            times = times + 1
            for j in range(4,15):
                if STB.adb_check(device):
                    # 打开settings
                    STB.settings()
                    time.sleep(3)
                    # 进入settings菜单
                    for i in range(5):
                        STB.down()
                    STB.up()
                    STB.ok()
                    # 进入display菜单
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
                    time.sleep(90)
                    print("第", j, "次重启")
                    if times > 1000:
                        return
    except KeyboardInterrupt:
        print("测试中断")


if __name__ == "__main__":
    # dev = sys.argv[1]
    dev = "192.168.1.104:5555"
    start_test(dev)
