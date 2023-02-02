import ctypes
import os

CUR_PATH = os.path.dirname(__file__)
dllPath = os.path.join(CUR_PATH, "Support.dll")
print(dllPath)
mydll=ctypes.cdll.LoadLibrary(dllPath)
print(mydll)
# pDll = ctypes.WinDLL(dllPath)
# print(pDll)

pResutl = pDll.sum(1, 4)
pResult2 = pDll.sub(1, 4)
print(pResutl)
print(pResult2)
