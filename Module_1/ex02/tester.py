import os
from load_image import ft_load

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "landscape.jpg")

print(ft_load(image_path))