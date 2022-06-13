import time

from Main import Utils as STB


# 测试前清除所有customize channel以保证第一排app在倒数第三排，live channel 是第一个，Netflix是第二个，Amazon第三个
def start_test(dev, i):
    times = 0
    while True:
        # 播放TV
        STB.home(dev)
        [STB.down(dev) for i in range(5)]
        [STB.up(dev) for i in range(3)]
        [STB.left(dev) for i in range(5)]
        [STB.right(dev) for i in range(1)]
        STB.ok(dev)
        time.sleep(10)
        # 播放Netflix或Amazon
        STB.home(dev)
        [STB.down(dev) for i in range(5)]
        [STB.up(dev) for i in range(3)]
        [STB.left(dev) for i in range(5)]
        # Netflix
        # [STB.right(dev) for i in range(2)]
        # Amazon
        [STB.right(dev) for i in range(3)]

        STB.ok(dev)
        STB.ok(dev)
        time.sleep(20)

        times = times + 1
        print("已循环%d次" % times)
        if times > i:
            return


if __name__ == '__main__':
    start_test("192.168.1.108:5555", 50)
