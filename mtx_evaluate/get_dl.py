"""
Author: Guojin Chen @ CUHK-CSE
Homepage: https://gjchen.me
Date: 2023-01-31 13:03:45
LastEditTime: 2023-01-31 13:49:38
Contact: cgjcuhk@gmail.com
Description: get stitches and conflicts
"""
from config import start, end





for i in range(start, end):
    print("="*50)
    print(i)
    fp = f'/home/gjchen21/phd/projects/mtxcover/dlresults/s{i}.txt'
    all_arr = []
    with open(fp) as f:
        for l in f.readlines():
            l = l.strip('\n')
            l_arr = l.split(' ')
            while '' in l_arr:
                l_arr.remove('')
            n_arr = []
            for n in l_arr:
                n_arr.append(int(n))
            all_arr.append(n_arr)
    # print(all_arr)
    print(f'totol: {len(all_arr)}')
    print('='*50)
