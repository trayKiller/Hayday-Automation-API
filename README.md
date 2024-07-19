### Requirements
+ 1920 x 1080 resolution as images are taken in such.

### Soon to be added
+ Multiple Resolutions

### Features
+ Harvest
+ Shop
+ Utilizes ADB
+ No memory editing

### How to use (basics)
```python
import ADB.ADB as ADB
import ADB.Settings as Settings

Settings.IP = '127.0.0.1:5555'

Settings.Monitor_Screen_Width   = 1920
Settings.Monitor_Screen_Height  = 1080

def main():
    ADB.ConnectADB()
    Settings.Emulator_Screen_Width, Settings.Emulator_Screen_Height = ADB.GetEmulatorSize()
    
main()
ADB.DisconnectADB()
```
This code is how you get the basics of it working.
1. You need to declare your ADB ip
2. declare your monitor X/Y (default 1920x1080)
3. Connect to ADB
4. declare emulator x/y (default 1600x900)
5. disconnect from ADB when you're done with the program to avoid any problems or worries

### Shop Support
+ Wheat

### Harvest Support
+ Wheat
