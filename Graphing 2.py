import matplotlib.pylab as plt
import os


os.chdir("/Users/Daniel/Desktop/Test")

# -*- coding: utf-8 -*-
"""

"""
#   CODE REQUIRES THAT FILEORGANIZER IS RUN FIRST
#    j is a key phrase in the filelist you're interested in 

#Create PlOT:
j="on mast"
k="150908"
plt.figure(facecolor='white')

degree_sign= u'\N{DEGREE SIGN}'
plt.title(j+" runs")
plt.xlabel('T ('+degree_sign+'C)',fontsize = 14)
plt.ylabel('Fraction Frozen',fontsize = 14)
plt.minorticks_on
#pylab.legend(loc=9, bbox_to_anchor=(0.5, -0.1))

#%% LOOP ON PLOT
indices = [i for i, x in enumerate(filelist) if j in x if k in x]
for n in indices:
        
        
        xn="x"+str(n)
        yn="y"+str(n)
        [xn,yn]=(database[n][:,0],database[n][:,1])
        fig=plt.plot(xn,yn, 'o',  markersize=6, label=filelist[n][:-4])
        plt.legend(fontsize ='x-small',loc=9, bbox_to_anchor=(0.5, -0.1))
#        
#        
##       
