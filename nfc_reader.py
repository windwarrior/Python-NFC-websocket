import ctypes
import ctypes.util

from nfc_types import *
from functions import *


def list_devices():
    context = Context()

    contextpnt = pointer(context)

    nfc_init(byref(contextpnt))

    print nfc_version()

    device = nfc_open(contextpnt, None)

    if device:
        print "ok"
    else:
        print "no device"
        exit()

    errorcode = nfc_initiator_init(device)

    print nfc_device_get_name(device)

    target = Target()

    targetTypes = Modulation * 1;

    modulationTargets = targetTypes(Modulation(ModulationType.NMT_ISO14443A, BaudRate.NBR_106))

    target = Target()

    print nfc_initiator_poll_target(device, byref(modulationTargets), ctypes.c_size_t(1), ctypes.c_uint8(50), ctypes.c_uint8(2), byref(target))

    uid = " ".join([str(hex(target.nti.nai.abtUid[i])).replace("0x", "") for i in range(target.nti.nai.szUidLen)])
    
    print uid



list_devices()


