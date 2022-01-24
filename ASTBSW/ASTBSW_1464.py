import sys

from Main import Utils as STB


def test(device):
    while True:
        STB.power()
        STB.reboot()


if __name__ == "__main__":
    dev = sys.argv[1]
    test(dev)
