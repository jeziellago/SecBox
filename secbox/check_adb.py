import os
import subprocess
import urllib3
import shutil
import sys

from zipfile import ZipFile

PLATFORM_TOOLS_LINUX_URL= "https://dl.google.com/android/repository/platform-tools_r29.0.6-linux.zip"
PLATFORM_TOOLS_MAC_URL = "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip"

def get_platformtools_url_from_system():
    if sys.platform.startswith('linux'):
        return PLATFORM_TOOLS_LINUX_URL
    else:
        return PLATFORM_TOOLS_MAC_URL


def has_adb_installed(command):
    try:
        proc = subprocess.Popen([command, "--version"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        proc.wait()
        return True
    except:
        return False


def download_platform_tools():
    print('[*] Downloading platform-tools ...')
    pm = urllib3.PoolManager()
    request = pm.request('GET', get_platformtools_url_from_system(), preload_content=False)
    filename = "platform-tools.zip"
    with request, open(filename, 'wb') as out_file:
        shutil.copyfileobj(request, out_file)
        print('[-] Download platform-tools finished')

    with ZipFile(filename, 'r') as zipObj:
        print('[-] Extracting ' + filename)
        zipObj.extractall()
        print('[-] File "%s" extracted.' % filename)
    
    os.system('chmod +x platform-tools/adb')

    if has_adb_installed('platform-tools/adb'):
        print("[>>] Android Debug Bridge (ADB) installed!")


def check_adb():
    print("[!] Checking installation of Android Debug Bridge (ADB) ...")
    adb = 'adb'
    platform_tools_adb = 'platform-tools/adb'

    if has_adb_installed(adb):
        print("[>>] Android Debug Bridge (ADB) from environment [OK]")
        return adb
    elif has_adb_installed(platform_tools_adb):
        print("[>>] Android Debug Bridge (ADB) from %s [OK]" % platform_tools_adb)
        return platform_tools_adb
    else:
        print("[x] Android Debug Bridge (ADB) Not Found!")
        download_platform_tools()
        return platform_tools_adb