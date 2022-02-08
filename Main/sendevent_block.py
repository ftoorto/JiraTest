import Utils as STB

def fast_forward(device=None):
original_cmd1 = "adb shell sendevent /dev/input/event6: 0004 0004 000c0045"
original_cmd2 = "adb shell sendevent /dev/input/event6: 0001 006a 00000001"
original_cmd3 = "adb shell sendevent /dev/input/event6: 0000 0000 00000000"
original_cmd4 = "adb shell sendevent /dev/input/event6: 0004 0004 000c0045"
original_cmd5 = "adb shell sendevent /dev/input/event6: 0001 006a 00000000"
original_cmd6 = "adb shell sendevent /dev/input/event6: 0000 0000 00000000"

cmd1=STB._cmd_device(original_cmd1)
