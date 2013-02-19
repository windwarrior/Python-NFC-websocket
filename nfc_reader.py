import ctypes
import ctypes.util

from nfc_types import *
from functions import *


def list_devices():
    context = pointer(Context())

    nfc_init(byref(context))

    print nfc_version()

    device = nfc_open(context, None)

    if device:
        print "ok"
    else:
        print "no device"
        exit()

    errorcode = nfc_initiator_init(device)

    print nfc_device_get_name(device)

    target = Target()


    targetTypes = Modulation * 5;

    modulationTargets = targetTypes(
        Modulation(ModulationType.NMT_ISO14443A, BaudRate.NBR_106),
        Modulation(ModulationType.NMT_ISO14443B, BaudRate.NBR_106),
        Modulation(ModulationType.NMT_FELICA, BaudRate.NBR_212),
        Modulation(ModulationType.NMT_FELICA, BaudRate.NBR_424),
        Modulation(ModulationType.NMT_JEWEL, BaudRate.NBR_106))


    target = Target()

    print nfc_initiator_poll_target(device, byref(modulationTargets), ctypes.c_size_t(5), ctypes.c_uint8(20), ctypes.c_uint8(2), byref(target))
    
    for i in target.nti.nai.abtUid:
        print hex(i)

"""
    mod = Modulation(ModulationType.NMT_ISO14443A, BaudRate.NBR_106)
    print nfc_initiator_select_passive_target(device, mod, None, ctypes.c_size_t(0), byref(target))

    for i in target.nti.nai.abt:
        print i
"""

list_devices()


