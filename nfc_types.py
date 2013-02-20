import ctypes
import ctypes.util
from ctypes import *

#Enum modulationtype in C
class ModulationType():
    NMT_ISO14443A = 1
    NMT_JEWEL = 2
    NMT_ISO14443B = 3
    NMT_ISO14443BI = 4
    NMT_ISO14443B2SR = 5
    NMT_ISO14443B2CT = 6
    NMT_FELICA = 7
    NMT_DEP = 8

#Enum baudrate in C
class BaudRate():
    NBR_UNDEFINED = 0
    NBR_106 = 1
    NBR_212 = 2
    NBR_424 = 3
    NBR_847 = 4

class Context(Structure):
    _fields_ = []

class Device(Structure):
    _pack_ = 1
    _fields_ = [
            ("name", ctypes.c_char),
            ("connstring", ctypes.c_char_p),
            ("bCrc", ctypes.c_bool),
            ("bPar", ctypes.c_bool),
            ("bEasyFraming", ctypes.c_bool),
            ("bAutoIso14443_4", ctypes.c_bool),
            ("btSupportByte",  ctypes.c_uint8),
            ("last_error", ctypes.c_int)]

class Modulation(Structure):
    _pack_ = 1
    _fields_ = [
            ("nmt", ctypes.c_uint),
            ("nbr", ctypes.c_uint)]

class ISO14443aInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("abtAtqa", ctypes.c_uint8 * 2),
        ("btSak", ctypes.c_uint8 ),
        ("szUidLen", ctypes.c_size_t),
        ("abtUid", ctypes.c_uint8 * 10),
        ("szAtsLen", ctypes.c_size_t),
        ("abtAts", ctypes.c_uint8 * 254)]

class FelicaInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("szLen", ctypes.c_size_t),
        ("btResCode", ctypes.c_uint8),
        ("abtId", ctypes.c_uint8 * 8),
        ("abtPad", ctypes.c_uint8 * 8),
        ("abtSysCode", ctypes.c_uint8 * 2)]

class ISO14443bInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("abtPupi", ctypes.c_uint8 * 4),
        ("abtApplicationData", ctypes.c_uint8 * 4),
        ("abtProtocolInfo", ctypes.c_uint8 * 3),
        ("ui8CardIdentifier", ctypes.c_uint8)]

class ISO14443biInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("abtDIV", ctypes.c_uint8 * 4),
        ("btVerLog", ctypes.c_uint8),
        ("btConfig", ctypes.c_uint8),
        ("szAtrLen", ctypes.c_size_t),
        ("abtAtr", ctypes.c_uint8 * 33)]

class ISO14443b2srInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("abtUID", ctypes.c_uint8 * 8)]

class ISO14443b2ctInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("abtUID", ctypes.c_uint8 * 4),
        ("btProdCode", ctypes.c_uint8),
        ("btFabCode", ctypes.c_uint8)]

class JewelInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("btSensRes", ctypes.c_uint8 * 2),
        ("btId", ctypes.c_uint8 * 4)]

class DepInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("abtNFCID3", ctypes.c_uint8 * 10),
        ("btDID", ctypes.c_uint8),
        ("btBS", ctypes.c_uint8),
        ("btBR", ctypes.c_uint8),
        ("btTO", ctypes.c_uint8),
        ("btPP", ctypes.c_uint8),
        ("abtGB", ctypes.c_uint8 * 48)]
         
class TargetInfo(Union):
    _pack_ = 1
    _fields_ = [
        ("nai", ISO14443aInfo),
        ("nfi", FelicaInfo),
        ("nbi", ISO14443bInfo),
        ("nii", ISO14443biInfo),
        ("nsi", ISO14443b2srInfo),
        ("nci", ISO14443b2ctInfo),
        ("nji", JewelInfo),
        ("ndi", DepInfo)]  

class Target(Structure):
    _pack_ = 1
    _fields_ = [
        ("nti", TargetInfo),
        ("nm", Modulation)]
