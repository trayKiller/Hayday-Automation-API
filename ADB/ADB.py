import subprocess
import re

import ADB.Settings as Settings

def ConnectADB():
    """Connects to ADB"""
    print("Connecting to ADB...")
    result = RunADBCommand(f"connect {Settings.IP}")
    if "connected to" in result:
        print("Connected to ADB successfully.")
    else:
        print("Failed to connect to ADB.")
        
def DisconnectADB():
    """Disconnects from ADB"""
    print("Disconnecting from ADB...")
    result = RunADBCommand(f"disconnect {Settings.IP}")
    if "disconnected" in result:
        print("Disconnected to ADB successfully.")
    else:
        print("Failed to disconnect to ADB.")

def RunADBCommand(command):
    """Runs an ADB command.

    Args:
        command (str): The command you want to run.
    
    Returns:
        str: The output of the command.
    """
    full_command = f"adb -s {Settings.IP} {command}"
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {full_command}")
        print(result.stderr)
    return result.stdout

def GetEmulatorSize():
    """Gets the emulator's screen size.

    Raises:
        ValueError: If the command doesn't work or the output can't be parsed.

    Returns:
        tuple: The width and height of the emulator's screen.
    """
    result = RunADBCommand(f'shell wm size')
    match  = re.search(r'(\d+)x(\d+)', result)
    
    if match:
        width  = int(match.group(1))
        height = int(match.group(2))
        return width, height
    else:
        raise ValueError("Could not parse screen resolution from adb output.")

def ScreenToDevice(x, y):
    """Converts coordinates on your screen to the emulator for accurate ADB interaction.

    Args:
        x (int): The X coordinate on the screen.
        y (int): The Y coordinate on the screen.

    Returns:
        tuple: The corresponding (X, Y) coordinates on the emulator.
    """
    
    device_x = int(x * Settings.Emulator_Screen_Width / Settings.Monitor_Screen_Width)
    device_y = int(y * Settings.Emulator_Screen_Height / Settings.Monitor_Screen_Height)
    return (device_x, device_y)
