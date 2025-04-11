# RV Thomas G Thompson netplan configuration for static IP that bypasses the captive portal

# Let NetworkManager manage all devices on this system

```
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    enp44s0:
      dhcp4: no
      addresses:
        - 10.43.25.59/24   # Get from res tech
      routes:
      - to: default
        via: 10.43.25.1
      nameservers:
        addresses: [10.43.11.5, 10.43.25.5, 10.43.30.5]
```
