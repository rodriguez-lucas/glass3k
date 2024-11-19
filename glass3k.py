import logging
from ctypes import wintypes, WinDLL, get_last_error
from enum import Enum

import keyboard


class OpacityLevel(Enum):
    PERCENT_10 = 26
    PERCENT_20 = 51
    PERCENT_30 = 77
    PERCENT_40 = 102
    PERCENT_50 = 128
    PERCENT_60 = 153
    PERCENT_70 = 179
    PERCENT_80 = 204
    PERCENT_90 = 230
    PERCENT_100 = 255


# Constants
WS_EX_LAYERED = 0x00080000
GWL_EXSTYLE = -20
LWA_ALPHA = 0x2

# Load user32.dll and set necessary function prototypes
user32 = WinDLL("user32", use_last_error=True)
user32.GetForegroundWindow.restype = wintypes.HWND
user32.SetWindowLongW.argtypes = [wintypes.HWND, wintypes.INT, wintypes.LONG]
user32.SetWindowLongW.restype = wintypes.LONG
user32.SetLayeredWindowAttributes.argtypes = [
    wintypes.HWND,
    wintypes.COLORREF,
    wintypes.BYTE,
    wintypes.DWORD,
]
user32.SetLayeredWindowAttributes.restype = wintypes.BOOL


def set_window_opacity(opacity):
    hwnd = user32.GetForegroundWindow()
    if not hwnd:
        logging.warning("No focused window detected.")
        return

    current_style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    user32.SetWindowLongW(hwnd, GWL_EXSTYLE, current_style | WS_EX_LAYERED)

    success = user32.SetLayeredWindowAttributes(hwnd, 0, opacity, LWA_ALPHA)
    if not success:
        logging.error(f"Failed to set opacity: {get_last_error()}")


def main():
    logging.info("Glass3k is running... Press CTRL+SHIFT+{0-9} to change window opacity.")

    # Avoid looping declaration here to be more explicit
    keyboard.add_hotkey(f"ctrl+shift+1", lambda: set_window_opacity(OpacityLevel.PERCENT_10.value))
    keyboard.add_hotkey(f"ctrl+shift+2", lambda: set_window_opacity(OpacityLevel.PERCENT_20.value))
    keyboard.add_hotkey(f"ctrl+shift+3", lambda: set_window_opacity(OpacityLevel.PERCENT_30.value))
    keyboard.add_hotkey(f"ctrl+shift+4", lambda: set_window_opacity(OpacityLevel.PERCENT_40.value))
    keyboard.add_hotkey(f"ctrl+shift+5", lambda: set_window_opacity(OpacityLevel.PERCENT_50.value))
    keyboard.add_hotkey(f"ctrl+shift+6", lambda: set_window_opacity(OpacityLevel.PERCENT_60.value))
    keyboard.add_hotkey(f"ctrl+shift+7", lambda: set_window_opacity(OpacityLevel.PERCENT_70.value))
    keyboard.add_hotkey(f"ctrl+shift+8", lambda: set_window_opacity(OpacityLevel.PERCENT_80.value))
    keyboard.add_hotkey(f"ctrl+shift+9", lambda: set_window_opacity(OpacityLevel.PERCENT_90.value))
    keyboard.add_hotkey(f"ctrl+shift+0", lambda: set_window_opacity(OpacityLevel.PERCENT_100.value))

    # Keep the program running
    keyboard.wait("ctrl+shift+q")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
