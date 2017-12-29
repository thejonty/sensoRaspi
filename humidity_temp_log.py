from am2320 import AM2320
from time import sleep
import datetime
import csv



am2320 = AM2320(1)

while(1):
    (t, h) =  am2320.readSensor()
    curr_time = datetime.datetime.now()

    with open('sensorData.csv', 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')# dialect='excel')
        filewriter.writerow([curr_time, t, h])
    csvfile.close()
  
    sleep(300)

        
