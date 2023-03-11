
import pandas as pd
import os

def file_conversion(file_list)
    for ind, src in enumerate(file_list):
        print(f"{len(file_list)-ind} ", end='')
        dest = str(src.with_suffix('.parquet'))
        convert_csv_to_parquet(src, dest)
    print()
    
