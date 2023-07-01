import os
import time
import reset_lib

config_hash = reset_lib.config_file_hash()
newtok_ssid = config_hash['newtok_ssid']
wpa_key = config_hash['wpa_key']
reboot_required = False

reboot_required = reset_lib.update_ssid(newtok_ssid)
reboot_required = reset_lib.update_wpa_password(wpa_key)

if reboot_required == True:
    os.system('reboot')