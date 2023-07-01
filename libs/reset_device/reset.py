import os
import time
import reset_lib

config_hash = reset_lib.config_file_hash()
newtok_ssid = config_hash['newtok_ssid']
reboot_required = False

reboot_required = reset_lib.update_ssid(newtok_ssid)

if reboot_required == True:
    os.system('reboot')