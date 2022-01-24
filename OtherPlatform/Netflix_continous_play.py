import time
import datetime
import Main.Utils as STB


def start_test(device):
    i = 0
    while True:
        STB.play(device, 2)
        time.sleep(600)
        i = i + 1
        print("每隔十分钟点击播放，已操作%d次" % i)
        if i > 30:
            print("已测试300分钟，测试结束")
            return


if __name__ == '__main__':
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        start_test("192.168.1.104:5555")
    except KeyboardInterrupt:
        end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("测试中断")
        print("start time:", start_time)
        print("end time:", end_time)
