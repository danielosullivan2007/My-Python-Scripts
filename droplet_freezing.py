# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:13:19 2015

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

folder='C:\Users\eejvt\Mace head 2015\Experiments\ul-assay\\'
day='150827'
os.chdir(folder+day)
a=glob('*\\')

def getSec(s):
    l = s.split(':')
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

def run_video(ini_speed=1,name='Cold Plate',delay=0,temp_frame=0,low_info=0):
    cap = cv2.VideoCapture('run.avi')
    

            
    print cap.isOpened()
    iframe=1
    events=[]
    speed=ini_speed#ms
    font = cv2.FONT_HERSHEY_SIMPLEX
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    while(cap.isOpened()):
        
        cap.set(cv2.CAP_PROP_POS_FRAMES,iframe)
        ret, frame = cap.read()
        if not ret:
            break
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #print 
        '''
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if iframe>save_frames:
            for j in range(save_frames):
                if j==0:
                    olds[:,:,j]=frame
                else:
                    olds[:,:,j]=olds[:,:,j-1]
        '''
        color=(255,50,0)
        st_events=str(events).strip('[]')
        if not low_info:
            cv2.putText(frame,name,(10,120), font, 1,color,2,cv2.LINE_AA)
            if not isinstance(temp_frame,int):
                cv2.putText(frame,'T= %1.2f C'%temp_frame[iframe],(900,200), font, 2,color,2,cv2.LINE_AA)            
            cv2.putText(frame,'Pause: p - Back: b - Forward: n - Event: spacebar - Delete: d - Faster/play: h,f - Slower: s - 200ms speed: j',(10,25), font, 0.6,color,2,cv2.LINE_AA)
            cv2.putText(frame,'50 frames back: 1 - 10 frames back: 2 - 10 frames forward: 3 - 50 frames forward: 4 - Low info: l',(10,75), font, 0.6,color,2,cv2.LINE_AA)
            cv2.putText(frame,'Frame %i'%iframe,(10,200), font, 2,color,2,cv2.LINE_AA)
            cv2.putText(frame,'Speed %i ms'%speed,(10,300), font, 1,color,2,cv2.LINE_AA)
            cv2.putText(frame,'Events %i'%len(events),(10,400), font, 1,color,2,cv2.LINE_AA)
        else:
            cv2.putText(frame,'Fr %i'%iframe,(10,200), font, 1.5,color,2,cv2.LINE_AA)
            cv2.putText(frame,'Sp %i'%speed,(10,300), font, 0.8,color,2,cv2.LINE_AA)
            cv2.putText(frame,'Ev %i'%len(events),(10,400), font, 0.8,color,2,cv2.LINE_AA)
        if len(st_events)<100:
            cv2.putText(frame,'%s'%st_events,(10,700), font, 0.5,color,2,cv2.LINE_AA)
        else:
            cv2.putText(frame,'%s'%st_events[:100],(10,700), font, 0.5,color,2,cv2.LINE_AA)
            cv2.putText(frame,'%s'%st_events[100:],(10,750), font, 0.5,color,2,cv2.LINE_AA)
        cv2.imshow('Droplet freezing',frame)
        #cv2.waitKey(speed)
        #print iframe
        k = cv2.waitKey(speed)
        if k == 27:         # wait for ESC key to exit
            
            cv2.destroyAllWindows()
            break
        
        elif k == ord(' '): # wait for 's' key to save and exit
            events.append(iframe-delay)
            continue

#            cv2.waitKey(speed)
            

    #    if cv2.waitKey(1) & 0xFF == ord('q'):
    #        break
        elif k == ord('l'):
            low_info=int(np.logical_not(low_info))
            continue
        elif k == ord('s'):
            speed=speed*2
            cv2.waitKey(speed)
        elif k == ord('f'):
            speed=speed/2
            if speed==0:
                speed=1
            cv2.waitKey(speed)
        elif k == ord('h'):
            speed=speed/2
            if speed==0:
                speed=1
            cv2.waitKey(speed)        
        elif k == ord('j'):
            speed=200
        elif k == ord('d'):
            if len(events)!=0:
                
                events.pop()
                continue
            #cv2.waitKey(speed)

        elif k == ord('p'):
            
            cv2.waitKey(0)
        elif k == ord('1'):
            iframe=iframe-50
            continue
        elif k == ord('2'):
            iframe=iframe-10
            continue
        elif k == ord('3'):
            iframe=iframe+10
            continue
        elif k == ord('4'):
            iframe=iframe+50
            continue
            
            
            cv2.waitKey(0)
        elif k == ord('b'):
            iframe=iframe-1
            speed=0
            continue
        '''
        elif k == ord('r'):
            iframe=iframe-save_frames
            for iold in range(save_frames):
                cv2.putText(olds[:,:,save_frames-iold-1],name,(10,100), font, 1,color,2,cv2.LINE_AA)
    
                cv2.putText(olds[:,:,save_frames-iold-1],'Frame %i'%iframe,(10,200), font, 1,color,2,cv2.LINE_AA)
                cv2.putText(olds[:,:,save_frames-iold-1],'Speed %i ms'%speed,(10,300), font, 1,color,2,cv2.LINE_AA)
                cv2.putText(olds[:,:,save_frames-iold-1],'Events %i'%len(events),(10,400), font, 0.5,color,2,cv2.LINE_AA)
                if len(st_events)<10:
                    cv2.putText(olds[:,:,save_frames-iold-1],'%s'%st_events,(10,500), font, 0.5,color,2,cv2.LINE_AA)
                else:
                    cv2.putText(olds[:,:,save_frames-iold-1],'%s'%st_events[:10],(10,500), font, 0.5,color,2,cv2.LINE_AA)
                    cv2.putText(olds[:,:,save_frames-iold-1],'%s'%st_events[10:],(10,600), font, 0.5,color,2,cv2.LINE_AA)
                    
                cv2.imshow('Droplet freezing',olds[:,:,save_frames-iold-1])
                k = cv2.waitKey(500)
                if k == 27:         # wait for ESC key to exit
                    
                    cv2.destroyAllWindows()
                    break
                
                elif k == ord(' '): # wait for 's' key to save and exit
                    events.append(iframe-delay)
                    if first_time:
                        speed=200
                        first_time=0
                    cv2.waitKey(speed)
                iframe=iframe+1
            '''
    #    if cv2.waitKey(1) & 0xFF == ord('q'):
    #        break
        
        iframe=iframe+1
    print 
    cap.release()
    cv2.destroyAllWindows()
    return events


#%%
#fig=plt.figure()
#ax=plt.subplot(211)
#bx=plt.subplot()
#%%
for ifile in range (len(a)):
    os.chdir(folder+day+'\\'+a[ifile])
    if not a[ifile]== 'blanks\\':
        print a[ifile][7:][:-1]
        print 'Read? 1:Yes 0:No'
        if os.path.isfile('events_frame.csv'):
            print '"events_frame.csv" file existing'
        if os.path.isfile('temps.csv'):
            print '"temps.csv" file existing'
        if os.path.isfile('ff.csv'):
            print '"ff.csv" file existing'
        awnser= int(raw_input())
        if not awnser:
            continue
    else:
        continue
    
    data=np.genfromtxt('log.csv',delimiter=',',dtype=None)#converters = {1: getSec})
    headers=data[0,:]    
    data=data[1:,:]
    run_times=np.genfromtxt('run',skip_header=1,dtype=None)




    
    temp_frame=np.linspace(0,len(run_times),len(run_times))
    i=0
    #run_times=getSec(run_times)
    for i in range(len(run_times)):
        if run_times[i] in data[:,1]:
            temp_frame[i]=data[data[:,1].tolist().index(run_times[i]),2]
        else:
            if int(run_times[i][-1])>0:
                run_times[i]=run_times[i][:(len(run_times[i])-1)]+str(int(run_times[i][-1])-1)
            else :
                run_times[i]=run_times[i][:(len(run_times[i])-1)]+str(int(run_times[i][-1])+1)
        if run_times[i] in data[:,1]:
            temp_frame[i]=data[data[:,1].tolist().index(run_times[i]),2]
        else:
            temp_frame[i]=999



    print 'Events input: \n 1: video analisys \n 2: .csv:'
    

    awnser= int(raw_input())
    if awnser==1:
        
        events=run_video(name=a[ifile][12:][:-1],temp_frame=temp_frame)
        np.savetxt('events_frame.csv',events,delimiter=',')
        print '\'events_frame.csv\' saved/overwritted \n \n'
        #print 'REPEAT VIDEO? 0=NO 1=YES'
        #nb = int(raw_input())
        #if nb:
        #    events=run_video()
    else:
        events=np.genfromtxt('events_frame.csv',delimiter=',',dtype=None)
    
    np.savetxt('events_frame.csv',events,delimiter=',')
    particles=len(events)
    frezz_events=np.linspace(0,len(events),len(events))
    ff=frezz_events/float(particles)
    temps=np.zeros(len(events))
    i=0
    #run_times=getSec(run_times)
    for i in range(len(events)):
        if run_times[events[i]] in data[:,1]:
            temps[i]=data[data[:,1].tolist().index(run_times[events[i]]),2]
        else:
            if int(run_times[events[i]][-1])>0:
                run_times[events[i]]=run_times[events[i]][:(len(run_times[events[i]])-1)]+str(int(run_times[events[i]][-1])-1)
            else :
                run_times[events[i]]=run_times[events[i]][:(len(run_times[events[i]])-1)]+str(int(run_times[events[i]][-1])+1)
            temps[i]=data[data[:,1].tolist().index(run_times[events[i]]),2]
    '''        
        for itime in range(len(data[:,1])):
            if run_times[pos]==data[itime,1]:
                print run_times[pos]
                print data[itime,1]
                print pos
                print '---------------'
                temps[i]=data[itime,2].astype(float)
                
                print temps[i]
                if temps[i]==999:
                    
                    temps[i]=data[:,2].astype(float).min()
                    print 'cambiado',temps[i]
                i=i+1
            if temps[i-1]==0:
                print pos, run_times[pos],data[-1,1],data[0,1]
        '''
    np.savetxt('temps.csv',temps,delimiter=',')
    np.savetxt('ff.csv',ff,delimiter=',')

    imp=a[ifile][7:11]
    #np.save(')


    #plt.plot(temps,ff,'o',label=a[ifile][12:][:-3])
    #plt.legend()
    #plt.xlabel('Temperature')
    #plt.ylabel('Fraction frozen')








