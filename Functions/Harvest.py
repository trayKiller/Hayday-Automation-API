from python_imagesearch.imagesearch import imagesearch

import time
import Functions.Images.ImageLocations as image

def IsSiloFull(tolerance=0.4):
    """ 
    Determines if the silo is full by searching for the image on the screen.

    Args:
        tolerance (float): The similarity threshold for image search (default is 0.4). 
                           Higher values make the search more precise but less tolerant to variations.

    Returns:
        bool: True if the silo is full (image is detected), False otherwise.

    Notes:
        - The function is in harvest as the function can only determine if silo is full from the harvest popup.
        - I know others will cause this popup. I'll end up moving this out to a general location if the chance comes.
    """
    pos = imagesearch(image.InventoryFullSilo, tolerance)
    
    if pos[0] != -1:
        return True
    else:
        return False