# -*- coding: utf-8 -*-
import re
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time
from firebase import firebase



firebase = firebase.FirebaseApplication('https://tempandhum-4e7f3.firebaseio.com/', None)

HEATER_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(HEATER_PIN, GPIO.OUT)
GPIO.output(HEATER_PIN,GPIO.HIGH)
def readValues_Sensor():
    tempfar_coffee = firebase.get('/Coffee Temperature',None)
    tempfar_coffee_optimum = firebase.get('/Optimum Coffee Temperature',None)
    Altitude = firebase.get('/Sensor Readings/Altitude',None)
    Pressure = firebase.get('/Sensor Readings/Pressure',None)
    temp_coffee = float(re.search(r'\d+\.\d+', tempfar_coffee).group())
    temp_coffee_optimum = float(re.search(r'\d+\.\d+',tempfar_coffee_optimum).group())
    return temp_coffee, temp_coffee_optimum
while(True):
    
    result=firebase.get('/System Status',None)
    if result =='1':
        print('Smart Heater is ON')
        temp_current,temp_optimum=readValues_Sensor()
        if temp_current < temp_optimum:
            print('Switch On the Heater!!')
            GPIO.output(HEATER_PIN,GPIO.LOW)
            for i in range(1,10):
                time.sleep(60)
                temp_current,temp_optimum=readValues_Sensor()
                resultnew=firebase.get('/System Status',None)     
                if temp_current < temp_optimum and resultnew=='1':
                    print('Still Needs Heating')
                    
                else:
                    print('Heated to Optimum Temperature...or System Switched OFF..... Switching Off Heater')
                    GPIO.output(HEATER_PIN,GPIO.HIGH)
                    break 
        else:
            print('Heater remains OFF as Coffee is at Optimum Temperature')
    else:
        GPIO.output(HEATER_PIN,GPIO.HIGH)
        print ('Smart Heater is OFF')
    time.sleep(20)
