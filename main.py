import ADB.ADB as ADB
import ADB.Settings as Settings
import ADB.Interaction as Interaction

import Functions.Harvest as Harvest
import Functions.Shop as Shop

import Functions.Images.ImageLocations as image

Settings.IP = '127.0.0.1:5555'

Settings.Monitor_Screen_Width   = 1920
Settings.Monitor_Screen_Height  = 1080

def main():
    ADB.ConnectADB()
    Settings.Emulator_Screen_Width, Settings.Emulator_Screen_Height = ADB.GetEmulatorSize()
    
    while True:
        if Shop.IsShopOpen(image.RoadSideShop):
            location, found = Shop.GetEmptySlot(image.CreateNewSale)
            
            while found:
                Interaction.TapScreen(location[0], location[1])
                Shop.SellItem('wheat', 'high')
main()
ADB.DisconnectADB()