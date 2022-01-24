from subprocess import STDOUT, Popen
import shlex

# p = Popen(shlex.split("python somescript.py arg1 arg2"), cwd="../src/somedir", stderr=STDOUT)

# def individual_task(name=""):
#     cmd = "python" + " /ASTBSW/" + name + ".py"
#     Popen("python" + " //ASTBSW//" + name + ".py")
#
#
# if __name__ == "__main__":
#     individual_task("ASTBSW-1028")

import os


def start_test(filename):
    for j in range(50):
        fn =  str(j) +filename
        os.system("adb shell cp /sdcard/Movies/" + filename + " /sdcard/Movies/" + fn)
        print("复制",j,"次")


if __name__ == "__main__":
    start_test("2.zip")
