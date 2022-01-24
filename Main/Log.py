import datetime


def _ref_msg(msg):
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+msg


def _error(msg):
    return "Error! "+_ref_msg(msg)+"\n"


def _warning(msg):
    return "Warning! "+_ref_msg(msg)+"\n"


def _info(msg):
    return "Information! "+_ref_msg(msg)+"\n"


switch = {"error": _error, "warning": _warning, "info": _info}


def Log(msg, flag):
    return switch.get(flag)(msg)
