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

    targetTypes = Modulation * 5;

    targetTypes(
        Modulation(ModulationType.NMT_ISO14443A, BaudRate.NBR_106),
        Modulation(ModulationType.NMT_ISO14443B, BaudRate.NBR_106),
        Modulation(ModulationType.NMT_FELICA, BaudRate.NBR_212),
        Modulation(ModulationType.NMT_FELICA, BaudRate.NBR_424),
        Modulation(ModulationType.NMT_JEWEL, BaudRate.NBR_106))

    print targetTypes

    target = Target()

    nfc_initiator_poll_target(device, targetTypes, ctypes.c_size_t(5), ctypes.c_uint8(50), ctypes.c_uint8(10), target)
    #print lib.nfc_open(byref(context), None)

list_devices()
