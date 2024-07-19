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
    
def SwipeScreen(start_x, start_y, end_x, end_y, duration=500):
    """
    Swipes on the emulator screen from the start coordinates to the end coordinates.

    Args:
        start_x (int): The X coordinate of the starting point.
        start_y (int): The Y coordinate of the starting point.
        end_x (int): The X coordinate of the ending point.
        end_y (int): The Y coordinate of the ending point.
        duration (int, optional): The duration of the swipe in milliseconds. Default is 500ms.
    """
    ADB.ScreenToDevice(start_x, start_y)
    ADB.ScreenToDevice(end_x, end_y)
    print(f"Swiping from ({start_x}, {start_y}) to ({end_x}, {end_y}) over {duration} milliseconds...")
    ADB.RunADBCommand(f"shell input swipe {start_x} {start_y} {end_x} {end_y} {duration}")
