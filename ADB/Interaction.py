import ADB.ADB as ADB

def TapScreen(x, y):
    """Taps the emulator screen at the specified coordinates.

    Args:
        x (int): The X coordinate.
        y (int): The Y coordinate.
    """
    ADB.ScreenToDevice(x, y)
    print(f"Tapping at ({x}, {y})...")
    ADB.RunADBCommand(f"shell input tap {x} {y}")