import sys
import time

sys.path.append("../Main")
from Main import Utils as STB


def start_test(times=100):
    i = 0
    while True:
        STB.home()
        [STB.up() for i in range(4)]
        [STB.down() for i in range(2)]
        [STB.left() for i in range(4)]
        STB.right()
        STB.ok()
        time.sleep(20)
        STB.home()
        [STB.up() for i in range(4)]
        [STB.down() for i in range(2)]
        [STB.left() for i in range(4)]
        STB.right()
        STB.right()
        STB.ok()
        time.sleep(20)
        i = i + 1
        print("已测试%d次" % i)
        if i > times:
            return


def start_test_4045tlu(device):
    i = 0
    while True:
        # Netflix
        STB.home(device)
        time.sleep(5)
        [STB.up(device) for i in range(4)]
        [STB.down(device) for i in range(2)]
        [STB.left(device) for i in range(4)]
        STB.right(device)
        STB.ok(device)
        time.sleep(20)
        # Prime video
        STB.home(device)
        time.sleep(5)
        [STB.up(device) for i in range(4)]
        [STB.down(device) for i in range(2)]
        [STB.left(device) for i in range(4)]
        STB.right(device)
        STB.right(device)
        STB.ok(device)
        time.sleep(20)

        # YouTube
        STB.home(device)
        time.sleep(5)
        [STB.up(device) for i in range(4)]
        [STB.down(device) for i in range(2)]
        [STB.left(device) for i in range(4)]
        [STB.right(device) for i in range(3)]
        STB.ok(device)
        time.sleep(20)
        i = i + 1
        print("已测试%d次" % i)
        if i > 100000:
            return


if __name__ == '__main__':
    start_test_4045tlu("192.168.1.111")
