import sys
import Main.Utils as STB


def start_test(dev=None):
    if device is None:
        while True:
            STB.rewind(dev, 15)
            STB.play(dev, 3)
            STB.pause(dev, 3)
            STB.play(dev, 3)
            STB.fast_forward(dev, 3)
            STB.play(dev, 3)
            STB.rewind(dev, 3)
            STB.play(dev, 3)


if __name__ == '__main__':
    device = sys.argv[1]
    start_test(device)
