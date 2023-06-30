import os
import time
import reset_lib

config_hash = reset_lib.config_file_hash()
ssid_prefix = config_hash['ssid_prefix']
reboot_required = False


reboot_required = reset_lib.wpa_check_activate(config_hash['wpa_enabled'], config_hash['wpa_key'])

reboot_required = reset_lib.update_ssid(ssid_prefix)

if reboot_required == True:
    os.system('reboot')