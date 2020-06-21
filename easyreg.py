import sys
if tuple(sys.version_info)[0] < 3:
    import _winreg as winreg
else:
    import winreg
import os.path as path

def Get(key: str):
    key = key.replace("/", "\\")
    p1 = key.split('\\')[0]
    p2 = path.split(key)[1]
    truekey = key[len(p1) + 1:-(len(p2) + 1)]
    if p1 == "HKLM" or p1 == "HKEY_LOCAL_MACHINE": partition = winreg.HKEY_LOCAL_MACHINE
    elif p1 == "HKCR" or p1 == "HKEY_CLASSES_ROOT": partition = winreg.HKEY_CLASSES_ROOT
    elif p1 == "HKCU" or p1 == "HKEY_CURRENT_USER": partition = winreg.HKEY_CURRENT_USER
    elif p1 == "HKU" or p1 == "HKEY_USERS": partition = winreg.HKEY_USERS
    elif p1 == "HKCC" or p1 == "HKEY_CURRENT_CONFIG": partition = winreg.HKEY_CURRENT_CONFIG
    else: raise Exception("unknown partition")
    key = winreg.OpenKeyEx(partition, truekey)
    return winreg.QueryValueEx(key, p2)

def Set(key: str, value: str, Type=winreg.REG_SZ):
    key = key.replace("/", "\\")
    p1 = key.split('\\')[0]
    p2 = path.split(key)[1]
    truekey = key[len(p1) + 1:-(len(p2) + 1)]
    if p1 == "HKLM" or p1 == "HKEY_LOCAL_MACHINE": partition = winreg.HKEY_LOCAL_MACHINE
    elif p1 == "HKCR" or p1 == "HKEY_CLASSES_ROOT": partition = winreg.HKEY_CLASSES_ROOT
    elif p1 == "HKCU" or p1 == "HKEY_CURRENT_USER": partition = winreg.HKEY_CURRENT_USER
    elif p1 == "HKU" or p1 == "HKEY_USERS": partition = winreg.HKEY_USERS
    elif p1 == "HKCC" or p1 == "HKEY_CURRENT_CONFIG": partition = winreg.HKEY_CURRENT_CONFIG
    try:
        key = winreg.OpenKeyEx(partition, truekey)
    except:
        key = winreg.CreateKeyEx(partition, truekey)
    winreg.SetValueEx(key, p2, 0, Type, value)

def Rem(key: str):
    key = key.replace("/", "\\")
    p1 = key.split('\\')[0]
    p2 = path.split(key)[1]
    truekey = key[len(p1) + 1:-(len(p2) + 1)]
    if p1 == "HKLM" or p1 == "HKEY_LOCAL_MACHINE": partition = winreg.HKEY_LOCAL_MACHINE
    elif p1 == "HKCR" or p1 == "HKEY_CLASSES_ROOT": partition = winreg.HKEY_CLASSES_ROOT
    elif p1 == "HKCU" or p1 == "HKEY_CURRENT_USER": partition = winreg.HKEY_CURRENT_USER
    elif p1 == "HKU" or p1 == "HKEY_USERS": partition = winreg.HKEY_USERS
    elif p1 == "HKCC" or p1 == "HKEY_CURRENT_CONFIG": partition = winreg.HKEY_CURRENT_CONFIG
    key = winreg.OpenKeyEx(partition, truekey)
    try:
        winreg.DeleteValue(key, p2)
    except:
        winreg.DeleteKey(key, truekey)