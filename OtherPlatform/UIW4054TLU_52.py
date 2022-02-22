import Main.Utils as STB


def start_test(device):
    i = 1
    while True:
        STB.power_on(device, 60)
        STB.power_off(device, 60)
        print("已循环%d次" % i)
        i = i + 1
        if i > 10000:
            return


if __name__ == '__main__':
    start_test("192.168.0.100")

