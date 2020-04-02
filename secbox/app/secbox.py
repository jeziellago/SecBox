import os
from time import sleep
from .actionbox import extract_apk, decompile_only_sources, decompile_only_resources, decompile_all, recompile_apk

class SecBox:

    def __init__(self):
        self.__create_states__()
        self.menu_options = []

        self.__add_menu_option__('Extract apk from device', extract_apk)
        self.__add_menu_option__('Decompile only sources from apk', decompile_only_sources)
        self.__add_menu_option__('Decompile only resources from apk', decompile_only_resources)
        self.__add_menu_option__('Decompile all from apk', decompile_all) 
        self.__add_menu_option__('Recompile modified apk from folder', recompile_apk)

    def start(self):
        try:
            self.current_state = self.STATE_IDLE

            while True:
                self.__draw_header__()
                self.__handle_state__()
        except KeyboardInterrupt:
            print('\n<!> Exiting... Bye :)')
            exit()

    def __handle_state__(self):
        if self.current_state == self.STATE_IDLE:
            self.__draw_menu__()
            option = input('\n\n::> ')
            self.__select_menu_option__(option)
        else: pass

    def __select_menu_option__(self, option):
        action = None
        for menu in self.menu_options:
            if option == str(menu["id"]):
                action = menu["action"]
                break

        if action:
            self.current_state = self.STATE_PROCESSING
            action()
            self.current_state = self.STATE_IDLE
            input('\n[!] Press any key to [MENU]::>')
            
    def __create_states__(self):
        self.STATE_IDLE = 0
        self.STATE_PROCESSING = 1

    def __add_menu_option__(self, option, action):
        next_option_id = len(self.menu_options) + 1
        self.menu_options.append({
            "id": next_option_id, 
            "description": option, 
            "action": action
        })

    def __draw_header__(self):
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

    def __draw_menu__(self):

        print('\t[ MENU ]')
        
        for menu in self.menu_options:
            print('\t[ %s ] %s' % (menu["id"], menu["description"]))
