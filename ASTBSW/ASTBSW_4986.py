from Main import Utils as STB
import time


def start_test(time_flag):
    current_time = time.time()
    while time.time() < current_time + time_flag:
        STB.play(4)
        STB.fast_forward()
        STB.fast_forward()
        STB.fast_forward()
        STB.play(4)
        STB.fast_forward()
        STB.fast_forward()
        STB.fast_forward()
        STB.play(4)


if __name__ == "__main__":
    start_test(30)
