import sys

sys.path.append("../Main")
from Main import Utils as STB


def start_test(device=None):
    if device is None:
        while True:
            STB.rewind(15)
            STB.play(device, 3)
            STB.pause(device, 3)
            STB.play(device, 3)
            STB.fast_forward(3)
            STB.play(device, 3)
            STB.rewind(3)
            STB.play(device, 3)


if __name__ == '__main__':
    start_test()
