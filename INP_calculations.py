# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:51:13 2015

@author: eejvt


Code developed by Jesus Vergara Temprado
Contact email eejvt@leeds.ac.uk
University of Leeds 2015


"""

import numpy as np
import sys
import matplotlib.pyplot as plt
#sys.path.append('C:\opencv\build\x64\vc12\bin')

from glob import glob
import os
import csv
#flow=12.5
import random


#folder='C:\Users\eejvt\Mace head 2015\Experiments\ul-assay\\'
folder='//foe-data-10/a86/shared/Mace Head 15/'

day='150828'
os.chdir(folder+day)
a=glob('*\\')
#fig=plt.figure()
#ax=plt.subplot(211)
#bx=plt.subplot()
awnser_blank=0

def f(x, A, B): # this is your 'straight line' y=f(x)
    return np.exp(-B*x + A)


print 'Substract same day blanks: 2 \nSubstract big blank: 1 \nNo blanks: 0:No'
awnser_blank= int(raw_input())
if awnser_blank==2:
    os.chdir(folder+day+'\\blanks')
    reader = csv.reader(open('parameterization.csv', 'rb'))
    blank_param = dict(x for x in reader)
elif awnser_blank==1:
    os.chdir(folder+'\\big_blank')
    reader = csv.reader(open('parameterization.csv', 'rb'))
    blank_param = dict(x for x in reader)
#%%


fig=plt.figure(figsize=(20, 15))
ax=plt.subplot(121)
bx=plt.subplot(122)

for ifile in range (len(a)):
    if a[ifile]=='blanks\\':
        continue
    os.chdir(folder+day+'\\'+a[ifile])
    print 'Read? 1:Yes 0:No'
    print a[ifile][12:][:-1]
    awnser= int(raw_input())
    if not awnser:
        continue
    #events=np.genfromtxt('events_frame.csv',delimiter=',')
    temps=np.genfromtxt('temps.csv',delimiter=',')
    ff=np.genfromtxt('ff.csv',delimiter=',')
    if os.path.isfile('sampling_log.csv'):
        sampling_log=np.genfromtxt('sampling_log.csv',delimiter=',',dtype=None)
        flow=float(sampling_log[0,1])
        st_h=float(sampling_log[1,1][:2])
        st_m=float(sampling_log[1,1][3:5])
        end_h=float(sampling_log[2,1][:2])
        end_m=float(sampling_log[2,1][3:5])
        minutes=(end_h-st_h)*60+end_m-st_m
        mass_full=float(sampling_log[3,1])
        mass_empty=float(sampling_log[4,1])
        water_mass=mass_full-mass_empty
        water_volume=water_mass#ml

        print 'minutes sampling', minutes

        total_volume=minutes*flow
        
        print 'volume of air (l)',total_volume
        
        air_per_ml=total_volume/water_volume
        
        print 'liters of air per ml',air_per_ml        
        #1ml=1000ul
        air_per_ul=air_per_ml/1000
        print 'liters of air per ul',air_per_ul
        #sampling_log
        INPconc=-np.log(1-ff)/air_per_ul#INP/l
        print 'INP calculated','L^{-1}'
        if awnser_blank:
            substraction=f(temps,float(blank_param['A']),float(blank_param['B']))
            errsub=substraction-f(temps,float(blank_param['A'])-float(blank_param['errA']),float(blank_param['B'])-float(blank_param['errB']))
            INPconc=(INPconc*air_per_ul-substraction)/air_per_ul#Check this substraction
            #INPconc[INPconc<0]=0
            for i in range(len(INPconc)-1):
                if INPconc[i+1]<INPconc[i]:
                    INPconc[i+1]=INPconc[i]
        N=len(temps)
        '''
        #ff_std=np.sqrt(((1-ff)**2*ff*N+ff**2*(1-ff)*N)/N)
        ff_std=np.sqrt(N*ff*(1-ff))/N    
        #ff_std=np.sqrt(((1-ff)**2*ff*N+ff**2*(1-ff)*N)/N)   
        ff_up=ff+1.96*ff_std
        ff_down=ff-1.96*ff_std
        errff=1.96*ff_std        
        err_air_per_ul=air_per_ul*0.1
        #std=np.sqrt(np.log(INPconc)/ff*len(events))
        err_up=(1+1.96/(np.sqrt(ff*len(events)-1)))*ff*len(events)/air_per_ul
        err_down=(1-1.96/(np.sqrt(ff*len(events)-1)))*ff*len(events)/air_per_ul
        INP_err_sub=1/air_per_ul*errsub
        INP_err_ff=1/(air_per_ml*(1-ff))*errff
        INP_err_v=-(-substraction+np.log(1-ff))/air_per_ul**2*err_air_per_ul
        INP_err_total=INP_err_ff+INP_err_sub+INP_err_v
        r = lambda: random.randint(0,255)
        c1,c2,c3=r(),r(),r()
        INP_up=INPconc+INP_err_total#err_up#np.exp(np.log(INPconc)+std)
        INP_down=INPconc-INP_err_total#err_down#np.exp(np.log(INPconc)-std)

        bx.plot(temps,INP_up,'--',c='#%02X%02X%02X' % (c1,c2,c3),lw=2)
        bx.plot(temps,INP_down,'--',c='#%02X%02X%02X' % (c1,c2,c3),lw=2)
        '''
        bx.plot(temps,INPconc,label=a[ifile][12:][:-1],lw=2)#c='#%02X%02X%02X' % (c1,c2,c3))
        bx.set_xlabel('Temperature')
        bx.set_ylabel('$INP (L^{-1})$')
        bx.set_yscale('log')
        observation=1
        np.savetxt('INP.csv',INPconc,delimiter=',')
    N=len(temps)
    '''    
    ff_std=np.sqrt(N*ff*(1-ff))/N    
    #ff_std=np.sqrt(((1-ff)**2*ff*N+ff**2*(1-ff)*N)/N)   
    ff_up=ff+1.96*ff_std
    ff_down=ff-1.96*ff_std
    errff=1.96*ff_std

    ax.plot(temps,ff_up,'--')
    ax.plot(temps,ff_down,'--')
    '''
    ax.plot(temps,ff,'o',label=a[ifile][12:][:-1])

    ax.set_xlabel('Temperature')
    ax.set_ylabel('Fraction frozen')
    
big_title='Mace Head Day %s/%s/20%s'%(day[-2:],day[2:4],day[:2])
plt.figtext(0.40,0.95,big_title,fontsize=20)
ax.legend(loc='best', fontsize = 'small')
#ax.set_xlim(-30,-10)
bx.legend(loc='best', fontsize = 'small')
bx.set_xlim(-30,-10)
os.chdir(folder+day)
plt.savefig('INP_day_%s.png'%day)
    #if observation



            