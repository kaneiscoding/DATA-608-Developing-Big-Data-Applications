
import pandas as pd
import random

from pathlib import Path

def convert_csv_to_parquet( src, dst):
    # print(f"Converting {src} to {dst}")
    pid = os.getpid()
    ppid = os.getppid()
    str = "func1 pid={:d} ppid={:d}".format(pid, ppid)
    df = pd.read_csv(src, low_memory=False)
    df.to_parquet(dst, compression='none')
    
file_list = list(Path('address_data').glob('address_*.csv'))
# print (file_list)
random.shuffle(file_list)
