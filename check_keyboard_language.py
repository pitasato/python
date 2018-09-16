import ctypes

user32 = ctypes.WinDLL('user32', use_last_error=True)
curr_window = user32.GetForegroundWindow()

thread_id = user32.GetWindowThreadProcessId(curr_window, 0)

klid = user32.GetKeyboardLayout(thread_id)
lid = klid & (2**16 - 1)



lid_hex = hex(lid);
print lid_hex;