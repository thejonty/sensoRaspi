import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
class readWeather:
    def __init__(self, filename):
        self.filename = filename


    def generatePlot(self, requestedDate):
        self.store = pd.HDFStore(self.filename)
        temp = {}
        humid = {}
        fromTime = requestedDate + " 00:00:01" 
        toTime = requestedDate + " 23:59:59" 
        where = 'index > fromTime & index < toTime'

        self.dataRequested = self.store.select('Weather1',where = where, columns = ['Temp'])
        self.dataRequested1 = self.store.select('Weather1',where = where, columns = ['Humidity'])

        self.index1 = self.dataRequested.index.values.tolist()
            
        self.index_time = [pd.to_datetime(dt).strftime("%H:%M") for dt in self.index1]

        self.index_time = list( self.index_time[i] for i in np.arange(0,len(self.index1),28))


        temp['30min'] = pd.rolling_mean(self.dataRequested['Temp'], window=6)
        temp['5min'] = self.dataRequested['Temp']
        humid['30min'] = pd.rolling_mean(self.dataRequested1['Humidity'], window=6)
        humid['5min'] = self.dataRequested1['Humidity']

        x = np.arange(len(self.index1))

        x1 = np.arange(0,len(self.index1),28)
        plt.xkcd()
        fig, [ax_temp, ax_hum] = plt.subplots(2,1, figsize=(8,7))        
        fig.suptitle('Temperature, Humidity on '+ requestedDate, fontsize = 15)

        ax_temp.plot(x, temp['30min'], label = '30min_movAvg')
        ax_temp.plot(x, temp['5min'], 'r--', label = '5min_interval')
        #ax_temp.set_title('Temperature on '+ requestedDate)
        ax_temp.legend(loc='best')
        #ax_temp.set_xlabel("Time", fontsize = 12)
        ax_temp.set_ylabel("Temp (C)", fontsize = 12)
        #plt.xticks(x1, self.index_time, rotation = 45)
        #ax_temp.tick_params(labelsize=10)

        ax_hum.plot(x, humid['30min'], label = '30min_movAvg')
        ax_hum.plot(x, humid['5min'], 'r--', label = '5min_interval')
        #ax_hum.set_title('Humidity on '+ requestedDate)
        ax_hum.legend(loc='best')
        ax_hum.set_xlabel("Time", fontsize = 12)
        ax_hum.set_ylabel("Humidity (%)", fontsize = 12)
        plt.xticks(x1, self.index_time, rotation = 45)
        ax_hum.tick_params(labelsize=10)
        #make x-axis ticks invisible for temp
        plt.setp(ax_temp.get_xticklabels(), visible=False)

        #plt.xticks(x1, self.index_time, rotation = 45)
        plt.savefig('static/temp_humid_' + requestedDate + '.png')
        
        self.store.close()

    def generateTempPlot(self, requestedDate):
        self.store = pd.HDFStore(self.filename)
        temp = {}
        fromTime = requestedDate + " 00:00:01" 
        toTime = requestedDate + " 23:59:59" 
        where = 'index > fromTime & index < toTime'
        self.dataRequested = self.store.select('Weather1',where = where, columns = ['Temp'])

        self.index1 = self.dataRequested.index.values.tolist()

            
        self.index_time = [pd.to_datetime(dt).strftime("%H:%M") for dt in self.index1]

        self.index_time = list( self.index_time[i] for i in np.arange(0,len(self.index1),28))

        temp['30min'] = pd.rolling_mean(self.dataRequested['Temp'], window=6)
        temp['5min'] = self.dataRequested['Temp']

        x = np.arange(len(self.index1))

        x1 = np.arange(0,len(self.index1),28)
        plt.xkcd()
        plt.plot(x, temp['30min'], label = '5min_interval')
        plt.plot(x, temp['5min'], label = '30min_movAvg')
        plt.xticks(x1, self.index_time)
        plt.title('Temperature on '+ requestedDate)
        plt.legend()
        plt.savefig('static/temp' + requestedDate + '.png')
        
        self.store.close()
        #return self.dataRequested

    def generateHumidPlot(self, requestedDate):
        self.store = pd.HDFStore(self.filename)
        humid = {}
        fromTime = requestedDate + " 00:00:01" 
        toTime = requestedDate + " 23:59:59" 
        where = 'index > fromTime & index < toTime'
        self.dataRequested = self.store.select('Weather1',where = where, columns = ['Humidity'])

        self.index1 = self.dataRequested.index.values.tolist()

            
        self.index_time = [pd.to_datetime(dt).strftime("%H:%M") for dt in self.index1]

        self.index_time = list( self.index_time[i] for i in np.arange(0,len(self.index1),28))

        humid['30min'] = pd.rolling_mean(self.dataRequested['Humidity'], window=6)
        humid['5min'] = self.dataRequested['Humidity']

        x = np.arange(len(self.index1))

        x1 = np.arange(0,len(self.index1),28)
        plt.plot(x, humid['30min'], label = '5min_interval')
        plt.plot(x, humid['5min'], label = '30min_movAvg')
        plt.xticks(x1, self.index_time)
        plt.title('Humidity on '+ requestedDate)
        plt.legend()
        plt.savefig('static/humidity' + requestedDate + '.png')
        
        self.store.close()

if __name__ == '__main__':

    filename = 'humidity_temp_log.h5'
    readWeather = readWeather(filename)
    #readWeather.generateTempPlot("20170806")    
    #readWeather.generateHumidPlot("20170806")    
    readWeather.generatePlot("20171208")    
