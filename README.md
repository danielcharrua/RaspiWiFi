# RaspiWiFi

RaspiWiFi is a program to headlessly configure a Raspberry Pi's WiFi connection using using any other WiFi-enabled device (much like the way a Chromecast or similar device can be configured).

It can also be used as a method to connect wirelessly point-to-point with your Pi when a network is not available or you do not want to connect to one. Just leave it in Configuration Mode, connect to the **RaspiWiFi Setup** access point. The Pi will be addressable at `https://10.0.0.1` and `https://raspiwifisetup.com` using all the normal methods you might use while connected through a network.

RaspiWiFi has been tested with the Raspberry Pi B+, Raspberry Pi 3, and Raspberry Pi Zero W.

## Script-based installation instructions:

Clone and install RaspiWiFi
```
$ cd
$ git clone https://github.com/danielcharrua/RaspiWiFi.git
$ cd RaspiWiFi
$ sudo python3 initial_setup.py
```

This script will install all necessary prerequisites and copy all necessary config and library files, then reboot. When it finishes booting it should present itself in `Configuration Mode` as a WiFi access point with the name **RaspiWiFi Setup**.

The original RaspiWiFi directory that you ran the Initial Setup is no longer needed after installation and can be safely deleted. All necessary files are copied to `/usr/lib/raspiwifi/` on setup.

## Configuration:

After installation the configuration file can be found at `/etc/raspiwifi/raspiwifi.conf`

```
newtok_ssid=RaspiWiFi Setup
auto_config=1
auto_config_delay=60
wpa_key=password
```

## Usage:

- Connect to the **RaspiWiFi Setup** access point using any other WiFi enabled device.

- Navigate to `https://10.0.0.1` or to `https://raspiwifisetup.com` using any web browser on the device you connected with.

- Select the WiFi connection you'd like your Raspberry Pi to connect to from the drop down list and enter its wireless password on the page provided. If no encryption is enabled, leave the password box blank. You may also manually specify your network information by clicking on the "manual SSID entry ->" link.

- Click the "Connect" button.

- At this point your Raspberry Pi will reboot and connect to the access point specified.

- You can view the current WPA encryption settings and change them from the main Web Configuration interface. The current settings are visible in a panel in the upper left corner of the screen. If you click the values in this display you will be taken to a page where you can change them. If you change them your device will reboot to enable the new configuration. 

- You can also use the Pi in a point-to-point connection mode by leaving it in Configuration Mode. All services will be addresible in their normal way at `10.0.0.1` while connected to the **RaspiWiFi Setup** AP.


## Resetting the device:

You can reset the device by running the manual_reset.py in the `/usr/lib/raspiwifi/reset_device` directory as root or with sudo.


## Uninstallation:

You can uninstall RaspiWiFi at any time by running:
   
```sudo python3 /usr/lib/raspiwifi/uninstall.py```

You can also run it from the `libs/` directory from a fresh clone if you've installed from a previous version and don't have `/usr/lib/raspiwifi/uninstall.py` available.