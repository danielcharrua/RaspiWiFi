import os
import sys

if os.getuid():
    sys.exit('You need root access to install!')

print()
print()
print("#################################")
print("##### Installing RaspiWiFi  #####")
print("#################################")
print()
print()

# Install prereqs
os.system('apt update')
os.system('apt install python3 python3-pip dnsmasq hostapd -y')
print("Installing Flask web server...")
print()
os.system('pip3 install flask pyopenssl')

# Copy configs
os.system('mkdir /usr/lib/raspiwifi')
os.system('mkdir /etc/raspiwifi')
os.system('cp -a libs/* /usr/lib/raspiwifi/')
os.system('mv /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.original')
os.system('rm -f ./tmp/*')
os.system('mv /etc/dnsmasq.conf /etc/dnsmasq.conf.original')
os.system('cp /usr/lib/raspiwifi/reset_device/static_files/dnsmasq.conf /etc/')
os.system('cp /usr/lib/raspiwifi/reset_device/static_files/hostapd.conf /etc/hostapd/hostapd.conf')
os.system('systemctl unmask hostapd')
os.system('mv /etc/dhcpcd.conf /etc/dhcpcd.conf.original')
os.system('cp /usr/lib/raspiwifi/reset_device/static_files/dhcpcd.conf /etc/')
os.system('mkdir /etc/cron.raspiwifi')
os.system('cp /usr/lib/raspiwifi/reset_device/static_files/aphost_bootstrapper /etc/cron.raspiwifi')
os.system('chmod +x /etc/cron.raspiwifi/aphost_bootstrapper')
os.system('echo "# RaspiWiFi Startup" >> /etc/crontab')
os.system('echo "@reboot root run-parts /etc/cron.raspiwifi/" >> /etc/crontab')
os.system('mv /usr/lib/raspiwifi/reset_device/static_files/raspiwifi.conf /etc/raspiwifi')
os.system('touch /etc/raspiwifi/host_mode')

print()
print()
print("#####################################")
print("##### RaspiWiFi Setup Complete  #####")
print("#####################################")
print()
print()
print("Initial setup is complete. A reboot is required to start in WiFi configuration mode...")
reboot_ans = input("Would you like to do that now? [y/N]: ")

if reboot_ans.lower() == 'y':
	os.system('reboot')
