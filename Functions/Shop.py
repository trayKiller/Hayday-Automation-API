import ADB.Settings as Settings
import ADB.Interaction as Interact
import ADB.ADB as ADB

import Functions.Images.ImageLocations as image

from python_imagesearch.imagesearch import imagesearch

def WheatSelling(price):
    wheatPos = imagesearch(image.WheatPlantSell)
    
    if wheatPos[0] != -1:
        Interact.TapScreen(wheatPos[0], wheatPos[1])
        
        LessPos = imagesearch(image.LessPriceButton)
        
        if LessPos[0] != -1: # Item is selected
            if price == 'high':
                pos = imagesearch(image.MaxPriceButton, 0.6)
                pos = ADB.ScreenToDevice(pos[0], pos[1])
                Interact.TapScreen(pos[0], pos[1])
            elif price == 'low':
                pos = imagesearch(image.LessPriceButton, 0.6)
                pos = ADB.ScreenToDevice(pos[0], pos[1])
                Interact.TapScreen(pos[0], pos[1])
                
            

def CornSelling():
    print("Selling corn...")

def SoybeanSelling():
    print("Selling soybean...")

SELL_FUNCTIONS = {
    'wheat': WheatSelling,
    'corn': CornSelling,
    'soybean': SoybeanSelling,
}

def ScrollShop(distanceX, DistanceY, speed=500):
    """
    Scrolls through the shop interface by swiping from the center of the screen 
    in a specified direction.

    Args:
        distanceX (int): The horizontal distance to scroll. Positive values scroll to the left, and negative values scroll to the right.
        distanceY (int): The vertical distance to scroll. Positive values scroll upwards, and negative values scroll downwards.
        speed (int, optional): The duration of the swipe in milliseconds. Default is 500ms.
    
    Notes:
        - The swipe is performed from the center of the emulator to a point calculated by subtracting the specified distances from the center coordinates.
    """
    CenterX = Settings.Emulator_Screen_Width / 2
    CenterY = Settings.Emulator_Screen_Height / 2
    
    Interact.SwipeScreen(CenterX, CenterY, CenterX - distanceX, CenterY - DistanceY, speed)
    
def IsShopOpen(image, tolerance=0.8):
    """
    Checks if the roadside shop is open by searching for the image on the screen.

    Args:
        tolerance (float): The similarity threshold for the image search (default is 0.8). 
                           Higher values make the search more precise but less tolerant to variations.

    Returns:
        bool: True if the shop is open (image is detected), False otherwise.
    """
    pos = imagesearch(image, tolerance)
    
    if pos[0] != -1:
        return True
    else:
        return False

def CheckForSales(image, tolerance=0.8):
    """
    Checks if the roadside shop has any sales by the image on the screen.

    Args:
        tolerance (float): The similarity threshold for the image search (default is 0.8). 
                           Higher values make the search more precise but less tolerant to variations.

    Returns:
        bool: True if the shop is open (image is detected), False otherwise.
    """
    pos = imagesearch(image, tolerance)

    if pos[0] != -1:
        return True
    else:
        return False

def GetEmptySlot(image_path, tolerance=0.8):
    """
    Finds all occurrences of the specified image on the screen and indicates if any slots are found.

    Args:
        image_path (str): Path to the image file to search for.
        tolerance (float): Similarity threshold for the image search (default is 0.8).
                           Higher values make the search more precise but less tolerant to variations.

    Returns:
        tuple: A tuple where the first element is a list of positions (x, y) where the image is found,
               and the second element is a boolean indicating whether any slots were found.
    """
    positions = imagesearch(image_path, tolerance)
    
    if positions:
        return positions, True
    else:
        return [], False

def SellItem(plant, price):
    """
    Sells an item by invoking the appropriate selling function based on the plant name and price type.

    Args:
        plant (str): The name of the plant to sell, such as 'wheat', 'corn', or 'soybean'.
        price (str): 'high' for max price, 'low' for the least price.

    Returns:
        None: Calls the corresponding selling function if it exists, otherwise prints an error message if the function is not found.
    """
    plant = plant.lower()
    
    # Check if the price type is valid
    if price not in ['low', 'high']:
        print(f"Error: Invalid price type '{price}'. Must be 'high' or 'low'.")
        return
    
    # Retrieve the selling function
    sell_function = SELL_FUNCTIONS.get(plant)
    
    if sell_function:
        sell_function(price)  # Pass the price type to the selling function
    else:
        print(f"Error: No selling function defined for {plant}.")