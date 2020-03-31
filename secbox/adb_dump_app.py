import os 
from argparse import ArgumentParser
from check_adb import check_adb

ADB = None

def dump_apk(app_name):
    ADB = check_adb()
    os.system(ADB + ' shell pm path %s >> /tmp/%s' % (app_name, app_name))
    with open('/tmp/%s' % app_name, 'r') as f:
        source=f.read().split('\n')[0].replace('package:','').replace('\n','')
        dump_command=ADB + ' pull %s ./%s.apk' % (source, app_name)
        os.system(dump_command)
        os.system('rm -rf /tmp/%s' % app_name) 

def list_packages(app_name):
    ADB = check_adb()
    os.system(ADB + ' shell pm list packages | grep %s' % app_name)
