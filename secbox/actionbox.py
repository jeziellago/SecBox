from adb_dump_app import list_packages, dump_apk
from apktool_wrapper import decompile, recompile


def extract_apk():
    is_finished_success = False
    apk_key_word = input('[-] Insert a key word to search for apk |> ')
    if list_packages(apk_key_word):
        apk_package = input('\n[-] Copy and paste the apk package here |> ')
        target_dir_to_save = input('\n[-] Where whould like to save apk file? |> ')
        is_finished_success = dump_apk(apk_package, target_dir_to_save)

    return is_finished_success

def apktool_decompile(option):    
    apk_path = input('[-] Insert the apk file |> ')
    where_decompile = input('[-] Where should decompile? (default dir=\'.\') |> ')

    if len(where_decompile) == 0:
        where_decompile = '.'
    
    result = None
    if option == 1:
        result = decompile(apk_path, '-r', where_decompile)
    elif option == 2:
        result = decompile(apk_path, '-s', where_decompile)
    else:
        result = decompile(apk_path, '', where_decompile)
    
    if result:
        print('\n[>] %s decompiled in %s.' % (apk_path, where_decompile))
    