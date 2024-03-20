# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:52:50 2024

@author: berth
"""

import numpy as np
import h5py
from PIL import Image
import matplotlib.pyplot as plt
import os
import glob
import shutil



listo = glob.glob("*.mat")
for j in range(len(listo)):
    count = len(glob.glob('.images/RGB/*'))
    path = listo[j]
    fiel = f"{count}_"
    Data_Main = h5py.File(path,'r')
    print(Data_Main.keys())
    
    
    
    u = Data_Main.get('rad')
    u = np.array(u) 
    print(u.size)
    
    
    for i in range(31):
        result = Data_Main['rad'][i]
        band = str(int(Data_Main['bands'][i][0]))
        
        if not os.path.exists(fiel):
            os.makedirs(fiel)
        Image.fromarray(result.astype(np.uint8)).save(f'.images/{fiel}/{fiel}{band}.png')
    
    gg = path.split('.')[0]
    shutil.move(glob.glob(f"*{gg}*.jpg")[0], f'.images/RGB/{count}.jpg')
    Data_Main = None
    os.remove(f'{path}')


# red_spectrum = Data_Main['rgb'][0]
# green_spectrum = Data_Main['rgb'][1]
# blue_spectrum = Data_Main['rgb'][2]

# result1 = np.dstack((red_spectrum, green_spectrum, blue_spectrum))
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30, 15))
# ax1.imshow(result1)