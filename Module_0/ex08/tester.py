from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# Tester ft_tqdm
print("Testing ft_tqdm:")
for elem in ft_tqdm(range(333)):
    sleep(0.005)  # Simuler un délai lors de chaque itération
print()

# Tester tqdm original
print("Testing tqdm:")
for elem in tqdm(range(333)):
    sleep(0.005)  # Simuler un délai lors de chaque itération
print()
