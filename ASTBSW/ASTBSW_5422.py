from Main import Utils as STB
import time


def start_test(i):
    j = 0
    while True:
        STB.home()
        [STB.up() for _ in range(4)]
        STB.down()
        [STB.left() for _ in range(4)]
        STB.right()
        STB.ok()
        time.sleep(30)

        STB.home()
        [STB.up() for _ in range(4)]
        STB.down()
        [STB.left() for _ in range(4)]
        [STB.right() for _ in range(2)]
        STB.ok()
        STB.ok()
        STB.ok()
        time.sleep(20)
        STB.play(1)
        time.sleep(30)
        STB.play(1)
        time.sleep(30)
        STB.play(1)
        time.sleep(30)
        j=j+1
        print("完成"+str(j)+"次切换")
        if j > i:
            break


if __name__ == "__main__":
    start_test(10000)
