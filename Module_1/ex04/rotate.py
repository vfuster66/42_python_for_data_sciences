import os
import numpy as np
import matplotlib.pyplot as plt
from ex02.load_image import ft_load

def save_image(image: np.ndarray, filename: str):
    """Sauvegarde l'image transposée dans le dossier ex04."""
    try:
        # Utiliser un chemin relatif simple, comme dans ex05
        output_path = f"ex04/{filename}"
        plt.imsave(output_path, image, cmap='gray')
        print(f"💾 Image enregistrée : {output_path}")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde de l'image : {e}")

def ft_rotate() -> np.ndarray | None:
    """
    Charge une image, découpe une zone carrée, transpose manuellement
    et sauvegarde l'image. Affiche la forme et les pixels avant/après rotation.
    """
    # Utiliser un chemin relatif simple comme dans ex05
    path = "ex04/animal.jpeg"
    
    img_array = ft_load(path)
    if img_array is None:
        print("❌ Impossible de charger l'image.")
        return None
    
    print(f"The shape of image is: {img_array.shape}")
    print(img_array)
    
    # Extraire un carré 400x400 centré, et ne garder qu'un seul canal (R)
    center_y, center_x = img_array.shape[0] // 2, img_array.shape[1] // 2
    size = 400
    square = img_array[
        center_y - size // 2:center_y + size // 2,
        center_x - size // 2:center_x + size // 2,
        0:1
    ] # shape = (400, 400, 1)
    
    print(f"New shape after Transpose: {square.shape[:2]}")
    
    # Transposition manuelle (on supprime la dernière dimension)
    channel = square[:, :, 0] # shape = (400, 400)
    transposed = np.array([[channel[j][i] for j in range(channel.shape[0])]
                          for i in range(channel.shape[1])])
    
    print(transposed)
    save_image(transposed, "transposed_image.png")
    
    return transposed