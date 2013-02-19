import ctypes
import ctypes.util

from nfc_types import *

lib = ctypes.CDLL(ctypes.util.find_library('nfc'))

nfc_init = lib.nfc_init
nfc_version = lib.nfc_version
nfc_version.restype = ctypes.c_char_p

nfc_open = lib.nfc_open
nfc_open.restype = ctypes.POINTER(Device)

nfc_initiator_init = lib.nfc_initiator_init
nfc_initiator_init.argtypes = (ctypes.POINTER(Device),)
nfc_initiator_init.restype = ctypes.c_int

nfc_device_get_name = lib.nfc_device_get_name
nfc_device_get_name.argtypes = (ctypes.POINTER(Device),)
nfc_device_get_name.restype = ctypes.c_char_p

nfc_initiator_poll_target = lib.nfc_initiator_poll_target
#nfc_initiator_poll_target.argtypes = (ctypes.POINTER(Device), ctypes.POINTER(Modulation), ctypes.c_size_t, ctypes.c_uint8, ctypes.c_uint8, ctypes.POINTER(Target))
nfc_initiator_poll_target.restype = ctypes.c_int

nfc_initiator_select_passive_target = lib.nfc_initiator_select_passive_target
