import time

from Main import Utils as STB


def start_test(dev):
    i = 0
    while True:
        STB.pause(dev)
        time.sleep(2)
        STB.play(dev)
        i = i + 1
        print("第%d次暂停播放"%i)
        time.sleep(600)


if __name__ == '__main__':
    start_test("192.168.1.108:5555")
