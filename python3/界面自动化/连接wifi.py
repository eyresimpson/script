import os

ssid = "your_ssid"
password = "your_password"

os.system(f"netsh wlan set hostednetwork mode=allow ssid={ssid} keyMaterial={password}")
os.system("netsh wlan start hostednetwork")
