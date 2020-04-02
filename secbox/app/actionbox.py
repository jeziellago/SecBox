from apkextract import list_packages, dump_apk
from reveng import decompile, recompile
from os import path


def extract_apk():
    is_finished_success = False
    apk_key_word = input('[-] Insert a key word to search for apk |> ')
    if list_packages(apk_key_word):
        apk_package = input('\n[-] Copy and paste the apk package here |> ')
        target_dir_to_save = input('\n[-] Where whould like to save apk file? |> ')
        is_finished_success = dump_apk(apk_package, target_dir_to_save)

    return is_finished_success

def decompile_only_sources():
    apktool_decompile(1)

def decompile_only_resources():
    apktool_decompile(2)

def decompile_all():
    apktool_decompile(3)

def apktool_decompile(option):    
    where_decompile = input('[-] Where should decompile? (Ex.: ~/Documents/my-new-apk/) |> ')

    if path.isdir(where_decompile):
        print('\n[!] %s not found.' % where_decompile)
        return

    apk_path = input('[-] Insert the apk file path (Ex.: ~/Documents/myapp.apk) |> ')
    
    result = None
    if option == 1:
        result = decompile(apk_path, '-r', where_decompile)
    elif option == 2:
        result = decompile(apk_path, '-s', where_decompile)
    else:
        result = decompile(apk_path, '', where_decompile)
    
    if result: print('\n[>] %s decompiled in %s.' % (apk_path, where_decompile))

def recompile_apk():
    source_dir = input('[-] Absolute path from dir with modified sources |> ')

    if not path.isdir(source_dir):
        print('\n[!] %s not found.' % source_dir)
        return

    new_apk_path = input('[-] Path for create new APK file (Ex.: ~/Downloads/NewApp.apk) |> ')
    if recompile(source_dir, new_apk_path):
        print('\n[>] Finished! New recompiled apk generated in: \n[%s]' % new_apk_path)