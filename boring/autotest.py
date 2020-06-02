import pandas as pd
import numpy as np
import glob
import sys
import os

os.chdir("D:\\")

#퐇더 경로 지정

all_data = pd.DataFrame()
for f in glob.glob('C.xls'):
    df = pd.read_excel(f)
    all_data = all_data.append(df, ignore_index=True)

#데이터갯수확인
print(all_data.shape)
#데이터 잘 들어오는지 확인