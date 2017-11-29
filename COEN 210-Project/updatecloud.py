# -*- coding: utf-8 -*-
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time
import os
import glob
import PresAlt
import geolocation
import math
from firebase import firebase



firebase = firebase.FirebaseApplication('https://tempandhum-4e7f3.firebaseio.com/', None)


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f



#MOTOR_PIN = 
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(MOTOR_PIN, GPIO.OUT)

#while(True):
 #   result=firebase.get('/IoT/lightOn',None)
 #   if result==1:
  #      GPIO.output(LIGHT_PIN,GPIO.LOW)
#       print "light is on"
 #   else:
 # pr             GPIO.output(LIGHT_PIN,GPIO.HIGH)
#       print "light is off"     
    #firebase.put('/IoT','lightOn', 553453434)
  
while(True):

    print ('Updating Cloud')
    h,t = dht.read_retry(dht.DHT22, 17)
    temp =  '{0:0.1f}'.format(t)
    tempfar =float(temp) * 1.8 + 32
    tempfar1 = str(tempfar)+'℉'
    humidity = '{0:0.1f}'.format(h)
    hum= '{0:0.1f}%'.format(h)
    tempcoffee = read_temp()
    tempcoffee_far = str(tempcoffee)+'℉'
    alt = geolocation.alt
    pressure = PresAlt.Pressure
    P1 = PresAlt.Pressureraw
    ht = geolocation.altraw
    P2 = float(P1) * pow((1 - 0.00002255 * float(ht)), 5.266)
    x =float(P2) /float(P1)
    T1 = 373    #boiling point at 0 height
    T2 = float(T1) * (4890.56) / (4890.56 -float(T1) * (math.log(x)))
    temp_coffee_optimum_c = T2-273
    temp_coffee_optimum_f = temp_coffee_optimum_c * 1.8 + 32
    temp_coffee_opt_f = '{0:0.2f}'.format(temp_coffee_optimum_f)
    temp_opt_cof= str(temp_coffee_opt_f)+'℉'
    firebase.put ('/Sensor Readings','/Temperature',tempfar1)
    firebase.put ('/Sensor Readings','/Humidity',hum)
    firebase.put ('/','Coffee Temperature',tempcoffee_far)
    firebase.put ('/Sensor Readings','/Altitude',alt)
    firebase.put ('/Sensor Readings','/Pressure',pressure)
    firebase.put ('/','Optimum Coffee Temperature',temp_opt_cof)
    
    
    print('Updated Cloud')
    time.sleep(30)   

#if __name__ == '__main__':
    
