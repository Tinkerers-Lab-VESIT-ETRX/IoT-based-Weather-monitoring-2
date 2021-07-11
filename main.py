import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports

ser = serial.Serial("COM2", 9600)
res = 1
i = 0

time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
    firebase1 = firebase.FirebaseApplication('https://weather-monitoring-12aee-default-rtdb.firebaseio.com/', None)

    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        temp = a[0]
        temp = temp[5:]
        data0 = {'date': datetime.now().strftime("%Y-%m-%d"),
                'reading': temp,
                'time': datetime.now().strftime("%H:%M:%S")
                }
        result0 = firebase1.patch('https://weather-monitoring-12aee-default-rtdb.firebaseio.com/' + '/TEMPERATURE_data/' + str(i), data0)
        print(result0)

    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        humidity = a[1]
        humidity = humidity[4:]
        data1 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': humidity,
                 'time': datetime.now().strftime("%H:%M:%S")
                 }
        result1 = firebase1.patch('https://weather-monitoring-12aee-default-rtdb.firebaseio.com/' + '/HUMIDITY_data/' + str(i), data1)
        print(result1)

    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        rain = a[2]
        rain = rain[4:]
        data2 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': rain,
                 'time': datetime.now().strftime("%H:%M:%S")
                 }
        result2 = firebase1.patch('https://weather-monitoring-12aee-default-rtdb.firebaseio.com/' + '/RAIN_data/' + str(i), data2)
        print(result2)

    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        ldr = a[3]
        ldr = ldr[4:]
        data3 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': ldr,
                 'time': datetime.now().strftime("%H:%M:%S")
                 }
        result3 = firebase1.patch('https://weather-monitoring-12aee-default-rtdb.firebaseio.com/' + '/LIGHT_INTENSITY_data/' + str(i), data3)
        print(result3)

    for i in range(0, 4):
        a = []
        htr1 = str(ser.readline())
        a = htr1.split(",")
        air = a[4]
        air = air[4:][:-5]
        data4 = {'date': datetime.now().strftime("%Y-%m-%d"),
                 'reading': air,
                 'time': datetime.now().strftime("%H:%M:%S")
                 }
        result4 = firebase1.patch('https://weather-monitoring-12aee-default-rtdb.firebaseio.com/' + '/AIR_QUALITY_data/' + str(i), data4)
        print(result4)