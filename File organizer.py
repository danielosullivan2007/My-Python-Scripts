# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:59:43 2015

@author: Daniel
"""

#This will work for 3 levels of folders.... e.g. /campaign/date/experiment/

#%%
from glob import glob
import os
import shutil
import numpy as np


#%% Initialise inputs
folder='G:/All Mace Head/'
outfold= 'C:/Users/eardo/Desktop/Test/'
date='150904/'
ifile='log.csv'
 


#%% Dig down into current folders, extract ff, temps and totals and save. Then copy to 
#%% Then copy to output folder
os.chdir(folder)
a=glob('*//')
print "Current working dir : %s" % os.getcwd() 
    
for sfold in range (len(a)):
    os.chdir(folder+a[sfold])
    b=glob('*//')
    for ssfold in range (len(b)):
        try:
            
            os.chdir(folder+a[sfold]+b[ssfold])
            temps=np.genfromtxt('temps.csv',delimiter=',')
            ff=np.genfromtxt('ff.csv',delimiter=',')
            total=np.transpose(np.vstack((temps, ff)));
            np.savetxt("totals.csv", total , delimiter=",")
            shutil.copy((folder+a[sfold]+b[ssfold]+'totals.csv'), outfold+b[ssfold][:-1]+'.csv')
        except (IOError):
            print "Files missing from"+(folder+a[sfold]+b[ssfold])
            continue


#%%
import glob
filelist = []
os.chdir('C:/Users/eardo/Desktop/Test')
for counter, files in enumerate(glob.glob("*.csv")):
    filelist.append(files)


#%% Create dictionary
for fileitem in filelist:
    print fileitem

database={}
for n in range (len(filelist)):
    database[n]= np.genfromtxt(filelist[n],delimiter =',')
 
#%% LOOP ON PLOT   
import matplotlib.pylab as plt
import os


os.chdir("C:\Users\eardo\Desktop\Test")

# -*- coding: utf-8 -*-
"""

"""
#   CODE REQUIRES THAT FILEORGANIZER IS RUN FIRST
#    j is a key phrase in the filelist you're interested in 

#Create PlOT:
j="bubble"
k="150908"
plt.figure(facecolor='white')

degree_sign= u'\N{DEGREE SIGN}'
plt.title(j+" runs")
plt.xlabel('T ('+degree_sign+'C)',fontsize = 14)
plt.ylabel('Fraction Frozen',fontsize = 14)
plt.minorticks_on
#pylab.legend(loc=9, bbox_to_anchor=(0.5, -0.1))

indices = [i for i, x in enumerate(filelist) if j in x if k in x]
for n in indices:
        
        
        xn="x"+str(n)
        yn="y"+str(n)
        [xn,yn]=(database[n][:,0],database[n][:,1])
        fig=plt.plot(xn,yn, 'o',  markersize=6, label=filelist[n][:-4])
        plt.legend(fontsize ='x-small',loc='best')#, bbox_to_anchor=(0.5, -0.1))
#        
#        
##       

