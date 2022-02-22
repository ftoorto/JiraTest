import os
import subprocess
import datetime
from apscheduler.triggers.date import DateTrigger

from apscheduler.schedulers.blocking import BlockingScheduler


def _case_ref(case_name: str):
    t = case_name
    if t[-3:] != ".py":
        t = t + ".py"
    if t.find("-"):
        t = t.replace("-", "_")
    t = "../ASTBSW/" + t
    return t


def _file_ref(file_name: str):
    t = file_name
    if t[-3:] != ".py":
        t = t + ".py"
    t = "../OtherPlatform/" + t
    return t


def _device_ref(dev: str):
    d = dev
    if d.find(":5555") == -1:
        d = d.strip() + ":5555"
    return d


"""
    1. 所有任务必须适配：任务名+设备名，且均为全称
    2. OtherPlatform case
"""


class CommonTask:
    proc = None

    def __init__(self, test_file, test_device):
        self.file = test_file
        self.device = test_device

    def start_task(self):
        file = _file_ref(self.file)
        device = _device_ref(self.device)
        self.proc = subprocess.Popen("python " + file + " " + device)
        return self.proc.stdout

    def terminate_task(self):
        if self.proc is None:
            print("任务进程未在运行，终止失败")
        else:
            self.proc.kill()
            print("任务终止")



"""
    1. 所有任务必须适配：任务名+设备名，且均为全称
    2. ASTBSW case
"""


class ASTBSWTask:
    proc = None

    def __init__(self, test_case, test_device):
        self.case = test_case
        self.device = test_device

    def start_task(self):
        case = _case_ref(self.case)
        device = _device_ref(self.device)
        self.proc = subprocess.Popen("python " + case + " " + device)
        return self.proc.stdout

    def terminate_task(self):
        if self.proc is None:
            print("任务进程未在运行，终止失败")
        else:
            self.proc.kill()
            print("任务终止")


if __name__ == '__main__':
    # task1 = astbsw_task("ASTBSW-3014", "192.168.1.104")
    # res = task1.start_task()
    # print(res.read())
    task1 = CommonTask("test", "192.168.144.62")
    date_task_start = DateTrigger(datetime.datetime(2022, 2, 22, 17, 55, 10), timezone='Asia/Shanghai')
    date_task_finish = DateTrigger(datetime.datetime(2022, 2, 22, 17,55, 30), timezone='Asia/Shanghai')
    scheduler = BlockingScheduler()
    scheduler.add_job(task1.start_task, date_task_start)
    scheduler.add_job(task1.terminate_task, date_task_finish)
    try:
        scheduler.start()
        print("已结束")
    except(KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
