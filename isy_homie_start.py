#!/usr/bin/env python

import time
import yaml 

from isy_homie.bridge import Bridge

try:
    with open("/etc/isy_homie.yml", 'r') as ymlfile:
        cfg = yaml.full_load(ymlfile)
except FileNotFoundError:
    with open('config.yaml', 'r') as ymlfile:
        cfg = yaml.full_load(ymlfile)


try:
    bridge = Bridge (address=cfg['isy'] ['url'], username=cfg['isy'] ['username'],password=cfg['isy'] ['password'],mqtt_settings=cfg['mqtt'])
    
    while True:
        time.sleep(10)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")     
