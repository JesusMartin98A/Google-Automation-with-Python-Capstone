# Use the PIL library to update all images within ~/supplier-data/images directory. Change image resolution from 3000x2000 to 600x400 pixel and hange image format from .TIFF to .JPEG

#!/usr/bin/env python3

import os
from PIL import Image

def changeit(dir):
    for file in os.listdir(dir):
        if file.endswith(".tiff"):
            with Image.open(dir + file) as im:
                im.convert("RGB").resize((600,400)).save(dir + os.path.splitext(file)[0] + ".jpeg", "JPEG") # First, I convert RGBA 4-channel format to RGB 3-channel

changeit("supplier-data/images/")
