import ctypes


def get_volume():
    # Windows API function to get the volume
    winmm = ctypes.WinDLL('winmm.dll')
    winmm.waveOutGetVolume.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    winmm.waveOutGetVolume.restype = ctypes.c_uint

    # Get the volume
    volume = ctypes.c_uint()
    winmm.waveOutGetVolume(0, ctypes.byref(volume))

    # Extract the left and right channel volumes
    left_channel = volume.value & 0xFFFF
    right_channel = volume.value >> 16

    return left_channel, right_channel


print(get_volume())
