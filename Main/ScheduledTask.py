import os
import subprocess
import datetime
from apscheduler.triggers.date import DateTrigger

from apscheduler.schedulers.blocking import BlockingScheduler

"""
    1. 所有任务必须适配：任务名+设备名，且均为全称
"""


def _case_ref(case_name: str):
    t = case_name
    if t.find(".") == -1:
        t = t + ".py"
    if t.find("-"):
        t = t.replace("-", "_")
    t = "../ASTBSW/" + t
    return t


def _device_ref(dev: str):
    d = dev
    if d.find(":5555") == -1:
        d = d.strip() + ":5555"
    return d


class task:
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


if __name__ == '__main__':
    task1 = task("ASTBSW-3014", "192.168.1.104")
    # res = task1.start_task()
    # print(res.read())
    date_task_start = DateTrigger(datetime.datetime(2022, 1, 21, 16,8,40),timezone='Asia/Shanghai')
    date_task_finish = DateTrigger(datetime.datetime(2022, 1, 21, 14, 41) + datetime.timedelta(15))
    scheduler = BlockingScheduler()
    scheduler.add_job(task1.start_task, date_task_start)
    scheduler.add_job(task1.terminate_task, date_task_finish)
    scheduler.start()
