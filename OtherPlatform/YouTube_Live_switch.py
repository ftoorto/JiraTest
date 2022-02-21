import time

import Main.Utils as STB


def start_test(device):
    i = 1
    while True:
        # YouTube
        STB.home(device)
        time.sleep(1)
        [STB.down(device) for i in range(6)]
        [STB.up(device) for i in range(2)]
        [STB.left(device) for i in range(3)]
        STB.right(device)
        STB.ok(device, 1)
        STB.play(device, 1)
        time.sleep(15)
        # Live
        STB.home(device)
        time.sleep(1)
        [STB.down(device) for i in range(6)]
        [STB.up(device) for i in range(2)]
        [STB.left(device) for i in range(3)]
        [STB.right(device) for i in range(3)]
        STB.ok(device, 1)
        time.sleep(10)

        print("已循环%d次" % i)
        i = i + 1
        if i > 100000:
            print("测试结束")
            return


if __name__ == '__main__':
    start_test("192.168.1.110")
