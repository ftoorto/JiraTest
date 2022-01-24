import time

import Utils as STB


def start_test(device):
    STB.pause(device, 1)
    STB.play(device, 1)
    time.sleep(1800)


if __name__ == '__main__':
    start_test("192.168.1.101:5555")
