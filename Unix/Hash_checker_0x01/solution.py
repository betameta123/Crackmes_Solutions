import os
from tqdm import tqdm
[0 if os.popen('./crackme ' + f"{i:06d}").read().strip() == "Wrong key!" else print(f"{i:06d}") for i in tqdm(range(1000000)) ]
