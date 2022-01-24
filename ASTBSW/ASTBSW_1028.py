import time
import sys
import Main.Utils as STB


def start_test(add, i=1440):
    j = 0
    while True:
        if STB.adb_check(add):
            STB.down()
            time.sleep(4)
        j = j + 1
        print(j, "次")
        if j > i:
            return


if __name__ == "__main__":
    device = sys.argv[1]
    start_test(device)
