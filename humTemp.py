from am2320 import AM2320
from time import sleep
import datetime
import csv
import pandas as pd

filename = 'humidity_temp_log.h5'

#store = {} #dictionary to store objects
#hdf = pd.store = {} #dictionary to store objects

am2320 = AM2320(1)

while(1):
    
    hdf = pd.HDFStore(filename)
    store1 = []
    jj = 12
    curr_time = datetime.datetime.now()
    
    while(jj>0):
        jj = jj - 1
        (t, h) =  am2320.readSensor()
        #curr_time = datetime.datetime.now()
        #yr = datetime.datetime.strftime(curr_time, "%Y")
        #mn = datetime.datetime.strftime(curr_time, "%m")
        #dy = datetime.datetime.strftime(curr_time, "%d")
        #tm = datetime.datetime.strftime(curr_time, "%H:%m")
        #store1.append([yr,mn,dy,tm,t,h])
        store1.append([t,h])
        sleep(300)
    #df = pd.DataFrame(store1,columns=('Year', 'Month', 'Day', 'Time', 'Temp', 'Humidity'))
    df = pd.DataFrame(store1,index=pd.date_range(start=curr_time, periods=12,freq='300S'), columns=('Temp', 'Humidity'))

    hdf.append('Weather1', df, format='table', data_columns=True)
#    print hdf['Weather1'].shape



