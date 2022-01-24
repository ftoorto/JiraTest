import time

from Main import Utils as STB


def start_test():
    i = 0
    while True:
        i = i + 1
        STB.ok()
        print("第", i, "次按ok")
        time.sleep(5)
        if i > 1000000:
            break


if __name__ == "__main__":
    start_test()
