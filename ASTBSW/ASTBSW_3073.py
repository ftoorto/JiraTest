import Main.Utils as STB


def start_test(device=None):
    i = 1
    while True:
        STB.power_off(device,60)
        STB.power_on(device,60)
        print(r"已循环%d次" % i)
        if(i>100000):
            return
        i=i+1


if __name__ == '__main__':
    start_test("192.168.1.107")
