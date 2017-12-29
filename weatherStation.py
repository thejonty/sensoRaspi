from am2320 import AM2320
from time import sleep
import datetime
import csv
from pandas import HDFStore, DataFrame, date_range

filename = 'humidity_temp_log.h5'

#store = {} #dictionary to store objects
#hdf = store = {} #dictionary to store objects

am2320 = AM2320(1)

while(1):
    
    hdf = HDFStore(filename)
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
    #df = DataFrame(store1,columns=('Year', 'Month', 'Day', 'Time', 'Temp', 'Humidity'))
    df = DataFrame(store1,index=date_range(start=curr_time, periods=12,freq='300S'), columns=('Temp', 'Humidity'))

    hdf.append('Weather1', df, format='table', data_columns=True)
#    print hdf['Weather1'].shape



