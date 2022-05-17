import Main.Utils as STB
def start_test(device):
    i=1
    while True:
        STB.ok(device,10)
        STB.ok(device,10)
        print("已循环%s次"%i)
        if i>100000:
            return
        i=i+1

if __name__ == '__main__':
    start_test("192.168.1.107")