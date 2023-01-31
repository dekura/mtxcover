"""
Author: Guojin Chen @ CUHK-CSE
Homepage: https://gjchen.me
Date: 2023-01-31 13:03:45
LastEditTime: 2023-01-31 13:48:44
Contact: cgjcuhk@gmail.com
Description: get stitches and conflicts
"""
from config import start, end




for i in range(start, end):
    print("="*50)
    print(i)
    fp = f'/home/gjchen21/phd/projects/mtxcover/gpuresults/s{i}.txt'
    all_arr = []
    with open(fp) as f:
        l = f.readlines()
        l = l[0]
        l = l.strip('\n')
        l = l.split(' ')
        while '' in l:
            l.remove('')
        n_arr = []
        for n in l:
            n_arr.append(int(n))
        new_arr = None
        for n in n_arr:
            if n == 1:
                if new_arr is not None:
                    all_arr.append(new_arr)
                new_arr = []
                new_arr.append(n)
                continue
            else:
                new_arr.append(n)
        # print(all_arr)
        print(f'total: {len(all_arr)}')
        # l_arr = l.strip(' ')
    # print(l_arr)
    # for n in l_arr:
        # print(n)