import Log as Log


def _log_to_mail(text, log_flag):
    pass


def _log_to_file(text, log_flag):
    pass


def _log_to_console(text, log_flag):
    print(Log.Log(text, log_flag))


switch = {1: _log_to_mail, 2: _log_to_file, 3: _log_to_console}


def logging(text, flag, log_flag):
    switch.get(flag)(text, log_flag)
