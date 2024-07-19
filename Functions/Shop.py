import time

import ADB.Settings as Settings
import ADB.Interaction as Interact

from python_imagesearch.imagesearch import imagesearch

def WheatSelling():
    print("Selling wheat...")

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
        distanceX (int): The horizontal distance to scroll. Positive values scroll
                         to the left, and negative values scroll to the right.
        distanceY (int): The vertical distance to scroll. Positive values scroll
                         upwards, and negative values scroll downwards.
        speed (int, optional): The duration of the swipe in milliseconds. Default is 500ms.
    
    Notes:
        - The swipe is performed from the center of the screen to a point calculated 
          by subtracting the specified distances from the center coordinates.
    """
    CenterX = Settings.Monitor_Screen_Width / 2
    CenterY = Settings.Monitor_Screen_Height / 2
    
    Interact.SwipeScreen(CenterX, CenterY, CenterX - distanceX, CenterY - DistanceY, speed)

def SellItem(plant):
    """
    Sells an item by invoking the appropriate selling function based on the plant name.

    Args:
        plant (str): The name of the plant to sell. Such as 'wheat', 'corn', or 'soybean'.

    Returns:
        None: Calls the corresponding selling function if it exists, otherwise prints an error message if the function is not found.
    """
    plant = plant.lower()
    
    sell_function = SELL_FUNCTIONS.get(plant)
    
    if sell_function:
        sell_function() 
    else:
        print(f"Error: No selling function defined for {plant}. Make sure you typed or correctly, no white space, or supported.")