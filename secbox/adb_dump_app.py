import os 
from argparse import ArgumentParser
from check_adb import check_adb

ADB = None

def dump_apk(app_name, target_dir):
    if len(target_dir) == 0:
        print('[!] Invalid dir to save apk file!')
        return False

    ADB = check_adb()
    os.system(ADB + ' shell pm path %s >> /tmp/%s' % (app_name, app_name))
    with open('/tmp/%s' % app_name, 'r') as f:
        source=f.read().split('\n')[0].replace('package:','').replace('\n','')
        dump_command=ADB + ' pull %s %s/%s.apk' % (source, target_dir, app_name)
        finished = os.system(dump_command) == 0
        if finished:
            os.system('rm -rf /tmp/%s' % app_name) 
            print('\n[>] %s.apk extracted to %s' % (app_name, target_dir))
        return finished

def list_packages(app_name):
    ADB = check_adb()
    print('\n')
    return os.system(ADB + ' shell pm list packages | grep %s' % app_name) == 0
