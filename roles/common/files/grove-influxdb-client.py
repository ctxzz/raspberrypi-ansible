#!/usr/bin/python -u

from datetime import datetime
import numpy
import time
import grovepi
import math
import json
import influxdb_client
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

url = "https://us-west-2-1.aws.cloud2.influxdata.com"
token = ""
bucket = ""
org = ""
measurement = "desk"

client = InfluxDBClient(url=url, token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

light_sensor = 0  # A0
sound_sensor = 2  # A2
temp_humidity_sensor = 7  # D7

# temp_humidity_sensor_type
blue = 0  # The Blue colored sensor.

sensor_samples = 30

error_flag = False
sequence = []
backuped_sequence = []

def get_sensor():
    samples_light = []
    samples_sound = []
    samples_temp = []
    samples_humidity = []
    for i in range(sensor_samples):
        samples_light.append(grovepi.analogRead(light_sensor))
        samples_sound.append(grovepi.analogRead(sound_sensor))
        [temp, humidity] = grovepi.dht(temp_humidity_sensor, blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            samples_temp.append(temp)
            samples_humidity.append(humidity)
            time.sleep(1)
    return [numpy.median(samples_light), numpy.median(samples_sound), numpy.median(samples_temp), numpy.median(samples_humidity)]

if __name__ == '__main__':
    grovepi.pinMode(light_sensor, "INPUT")
    grovepi.pinMode(sound_sensor, "INPUT")
    grovepi.pinMode(temp_humidity_sensor, "INPUT")

    print("start!!!")
    timestamp = datetime.utcnow()

    while True:
        light, sound, temp, humidity = get_sensor()
        sequence = []
        lightPoint = Point(measurement).tag('device', 'raspberry-pi').field("light", light).time(time=timestamp).to_line_protocol()
        sequence.append(lightPoint)
        soundPoint = Point(measurement).tag('device', 'raspberry-pi').field("sound", sound).time(time=timestamp).to_line_protocol()
        sequence.append(soundPoint)
        tempPoint = Point(measurement).tag('device', 'raspberry-pi').field("temperature", temp).time(time=timestamp).to_line_protocol()
        sequence.append(tempPoint)
        humidPoint = Point(measurement).tag('device', 'raspberry-pi').field("humidity", humidity).time(time=timestamp).to_line_protocol()
        sequence.append(humidPoint)
        print(sequence)

        try:
            write_api.write(bucket, org, sequence)
            if error_flag == True:
                write_api.write(bucket, org, backuped_sequence)
                error_flag = False
                backuped_sequence = []

        except:
            error_flag = True
            backuped_sequence.extend(sequence)
