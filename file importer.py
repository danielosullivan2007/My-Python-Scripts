# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:55:35 2015

@author: Daniel
"""
from glob import glob
import os
import numpy as np
folder='//foe-data-10/a86/shared/Mace Head 15'
date='150910'
os.chdir(folder)
a=glob('*/')

for ifolder in range (3):
    for ifile in range (1,2):
    
        os.chdir(folder+'//'+a[ifolder])
        z=str(ifile)
        temps[ifile]=np.genfromtxt(z+'.txt')
    
    
