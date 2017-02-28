# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:56:07 2015

@author: eejvt


Code developed by Jesus Vergara Temprado
Contact email eejvt@leeds.ac.uk
University of Leeds 2015


"""

import numpy as np
import sys
import matplotlib.pyplot as plt
#sys.path.append('C:\opencv\build\x64\vc12\bin')
import cv2
from glob import glob
import os
from scipy import stats


from scipy.optimize import curve_fit

def f(x, A, B): # this is your 'straight line' y=f(x)
    return np.exp(-B*x + A)


folder='C:\Users\eejvt\Mace head 2015\Experiments\ul-assay\\'
day='150818'
os.chdir(folder+day)
a=glob('*\\')
#fig=plt.figure()
if not os.path.isdir("blanks"):
    os.mkdir('blanks')
#%%
a_blanks=[]
#total

for file_name in a:
    if 'blank' in file_name:
        if not file_name=='blanks\\':
            print 'Use %s? \n 1:Yes 0:No'%file_name
            awnser_blank= int(raw_input())
            if awnser_blank:
                a_blanks.append(file_name)
temps_total=np.array([])
ff_total=np.array([])
lam_total=np.array([])
for file_name in a_blanks:
    os.chdir(folder+day+'\\'+file_name)
    temps=np.genfromtxt('temps.csv',delimiter=',')
    ff=np.genfromtxt('ff.csv',delimiter=',')
    temps_total=np.concatenate((temps_total,temps))
    ff_total=np.concatenate((ff_total,ff))
    ff09=ff
    ff09[ff09==1]=0.99
    lam=-np.log(1-ff09)
    lam_total=np.concatenate((lam_total,lam))

os.chdir(folder+day+'\\blanks')
np.savetxt('temps.csv',temps_total,delimiter=',')
np.savetxt('ff.csv',ff_total,delimiter=',')
np.savetxt('lamda.csv',lam_total,delimiter=',')
fig=plt.figure()
ax=plt.subplot(111)
plt.plot(temps_total,lam_total,'o')
log_lam=np.log(lam_total)
plt.yscale('log')
plt.show()
popt,pcov = curve_fit(f, temps_total, lam_total)
#popt=np.array([-18.59897567,   1.10249526])
#pcov=np.array([[ 0.50795402, -0.02496729],[-0.02496729,  0.00123657]])
perr = np.sqrt(np.diag(pcov))
ci = 0.95
pp = (1. + ci) / 2.
nstd = stats.norm.ppf(pp)
popt_up = popt + nstd * perr
popt_dw = popt - nstd * perr
temps_plot=np.linspace(temps_total.min(),temps_total.max(),100)
lam_fitted=f(temps_plot,popt[0],popt[1])
lam_low=f(temps_plot,*popt_dw)
lam_high=f(temps_plot,*popt_up)
plt.plot(temps_plot,lam_fitted,'k-',lw=3)
plt.plot(temps_plot,lam_high,'k--')
plt.plot(temps_plot,lam_low,'k--')
plt.xlabel('Temperature')
plt.ylabel('Expected value')
plt.text(0.8, 0.95,'Function $n_s=e^{(A-B*T)}$', ha='center', va='center', transform=ax.transAxes)
plt.text(0.8, 0.9,'$A=%.6f\pm%.6f$'%(popt[0],nstd*perr[0]), ha='center', va='center', transform=ax.transAxes)
plt.text(0.8, 0.85,'$B=%.6f\pm%.6f$'%(popt[1],nstd*perr[1]), ha='center', va='center', transform=ax.transAxes)
plt.text(0.8, 0.8,'95% confidence interval', ha='center', va='center', transform=ax.transAxes)
plt.title('Blank day %s'%day)
plt.savefig('Plot')
#%%
param={}
param['A']=popt[0]
param['errA']=nstd*perr[0]
param['B']=popt[1]
param['errB']=nstd*perr[1]
import csv
file_param= open('parameterization.csv', 'wb')
writer = csv.writer(file_param)
for key, value in param.items():
   writer.writerow([key, value])
file_param.close()
#%%
   




#%%
    