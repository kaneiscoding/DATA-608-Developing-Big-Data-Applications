
import pandas as pd
import os

def convert_csv_to_parquet(src, dst):
    # print(f"Converting {src} to {dst}")
    df = pd.read_csv(src, low_memory=False)
    df.to_parquet(dst, compression='none')

def file_conversion(file_list):
    for ind, src in enumerate(file_list):
        print(f"{len(file_list)-ind} ", end='')
        dest = str(src.with_suffix('.parquet'))
        convert_csv_to_parquet(src, dest)
    print()
 
