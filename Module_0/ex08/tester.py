from tqdm import tqdm
from time import sleep
from ex08.Loading import ft_tqdm


for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()