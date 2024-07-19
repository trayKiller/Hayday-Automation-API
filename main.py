import ADB.ADB as ADB
import ADB.Settings as Settings
import ADB.Interaction as Interaction
import Functions.Shop as Shop

Settings.IP = '127.0.0.1:5555'

Settings.Monitor_Screen_Width   = 1920
Settings.Monitor_Screen_Height  = 1080

def main():
    ADB.ConnectADB()
    Settings.Emulator_Screen_Width, Settings.Emulator_Screen_Height = ADB.GetEmulatorSize()
    
main()
ADB.DisconnectADB()