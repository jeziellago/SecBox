import os
from time import sleep
from adb_dump_app import list_packages, dump_apk
from apktool_wrapper import decompile, recompile

MENU_OPTIONS = ["1", "2", "3", "4", "5"]
SELECTED_OPTION = None

def draw_menu_header():
    os.system('clear')
    print(
    """ Welcome to
        _________            ___.                 
        /   _____/ ____   ____\_ |__   _______  ___
        \_____  \_/ __ \_/ ___\| __ \ /  _ \  \/  /
        /        \  ___/\  \___| \_\ (  <_> >    < 
        /_______  /\___  >\___  >___  /\____/__/\_ \\
                \/     \/     \/    \/            \/
                                powered by @jeziellago
    """)    
# ------------------------------------------------------- #
def back_to_menu():
    input('\n[!] Press any key to [MENU]::>')
# ------------------------------------------------------- #
def extract_apk():
    draw_menu_header()
    apk_key_word = input('[-] Insert a key word to search for apk |> ')
    if list_packages(apk_key_word):
        apk_package = input('\n[-] Copy and paste the apk package here |> ')
        target_dir_to_save = input('\n[-] Where whould like to save apk file? |> ')
        dump_apk(apk_package, target_dir_to_save)
        sleep(3)
    
    back_to_menu()
# ------------------------------------------------------- #
def apktool_decompile(option):
    draw_menu_header()
    apk_path = input('[-] Insert the apk file |> ')
    where_decompile = input('[-] Where should decompile? (default dir=\'.\') |> ')

    if len(where_decompile) == 0:
        where_decompile = '.'
    
    if option == 2:
        decompile(apk_path, '-r', where_decompile)
    elif option == 3:
        decompile(apk_path, '-s', where_decompile)
    elif option == 4:
        decompile(apk_path, '', where_decompile)
    
    print('\n[>] %s decompiled in %s.' % (apk_path, where_decompile))
    back_to_menu()
# ------------------------------------------------------- #
def draw_menu():
    print(
        """ 
        [ MENU ]
        [ 1 ] Extract apk from device
        [ 2 ] Decompile only sources from apk
        [ 3 ] Decompile only resources from apk
        [ 4 ] Decompile all from apk
        [ 5 ] Recompile modified apk from folder
        """
    )
# ------------------------------------------------------- #
def check_selected_option(option: str):
    if option in MENU_OPTIONS:
        SELECTED_OPTION = option
        if SELECTED_OPTION == MENU_OPTIONS[0]:
            extract_apk()
        elif SELECTED_OPTION in MENU_OPTIONS[1:4]:
            apktool_decompile(int(option))
        else:
            pass
    else:
        SELECTED_OPTION = None
# ------------------------------------------------------- #
def main():
    try:
        while True:
            draw_menu_header()
            if not SELECTED_OPTION: draw_menu()
            option = input('::> ')
            check_selected_option(option)
            sleep(2)
    except KeyboardInterrupt:
        draw_menu_header()
        print('<!> Exiting... Bye :)')
        exit()

if __name__ == '__main__':
    main()