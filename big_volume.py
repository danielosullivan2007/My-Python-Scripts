# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:54:39 2015

@author: eejvt


Code developed by Jesus Vergara Temprado
Contact email eejvt@leeds.ac.uk
University of Leeds 2015

"""

import numpy as np
import sys
#sys.path.append('C:\opencv\build\x64\vc12\bin')
import cv2
from glob import glob
import os
import matplotlib.pyplot as plt


folder='C:\\Users\\eejvt\\big_volume\\'
day='150828'
os.chdir(folder+day)
a=glob('*\\')
file1='150729 1640 100ul milliq.csv'
file1='log.csv'
#columns=20
def first_arg_less(array,value):
    if not any(array<value):
        return 0
    else:
        
        for i in range(len(array)):
            if array[i]<value:
                break
                print i
        
        return i



for ifile in range (len(a)):
    os.chdir(folder+day+'\\'+a[ifile])
    if not a[ifile]== 'blanks\\':
        print a[ifile][7:][:-1]
        print 'Read? 1:Yes 0:No'
        if os.path.isfile('temps.csv'):
            print '"temps.csv" file existing'
        if os.path.isfile('ff.csv'):
            print '"ff.csv" file existing'
        awnser= int(raw_input())
        if not awnser:
            continue
    data=np.genfromtxt(file1,delimiter=',',dtype=float)
    data=data[2:,1:]#columns+1]
    print data.shape
    #%%
        
    
    data_derived=data[:-1,:]-data[1:,:]
    frezz_temp=np.zeros(len(data_derived[0,:]))
    
    detectors=len(data[0,:])
    delete=np.zeros(detectors)
    for i in range(detectors):
        print detectors-1
        it_frezz=first_arg_less(data_derived[:,i],-1)
        print it_frezz
        if it_frezz==0:
            delete[i]=1
    #data_derived=np.delete(data_derived,delete.tolist())
    #data=np.delete(data,delete.tolist())
    
    for i in range(len(data[0,:])):
        print i
        it_frezz=first_arg_less(data_derived[:,i],-1)
        print it_frezz
        #if it_frezz==0:
        #    data=np.delete(data,i,1)
        #    i=i-1
        #    continue
        if it_frezz:
    
            frezz_temp[i]=np.min(data[:it_frezz+3,i])
            it_frezz=np.argmin(data[:it_frezz+3,i])
            print it_frezz
            plt.axvline(it_frezz,c='k',ls='--')
        plt.plot(data_derived[:,i])
        
        plt.plot(data[:,i])
    plt.show()
    
    plt.savefig('analisis_plot')
    plt.close()
    #%%
    delete_index=np.argwhere(delete==1)
    frezz_temp=np.delete(frezz_temp,delete_index)#check this!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #%%
    frezz_temp=np.sort(frezz_temp)
    frezz_temp[:] = frezz_temp[::-1]
    frezzing_events=np.arange(1,len(frezz_temp)+1,1)
    ff=frezzing_events/float(len(frezz_temp))
    np.savetxt('ff.csv',ff,delimiter=',')
    np.savetxt('temps.csv',frezz_temp,delimiter=',')
    plt.plot(frezz_temp,ff,'o')
    plt.ylabel('Fraction frozen')
    plt.xlabel('T (C)')
    plt.savefig('fraction_frozen.png')
    plt.close()
#%%
#if any (temps<90):
#    print 'sgffd'
