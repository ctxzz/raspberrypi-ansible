# Raspberry Pi Ansible

## Bootstrapping

$ sudo pip3 install ansible

## Configuation

- set your IP in `hosts`
- set Mac address in `roles/common/vars/main.yml`

## Running the playbook

$ sudo ansible-playbook site.yml 

## After running the playbook

1. sudo passwd [USERNAME]
2. sudo reboot
3. // usermod --lock pi // grovepi need pi user

## Setting up GrovePi

[GrovePi setup](https://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/)

1. $ curl -kL dexterindustries.com/update_grovepi | bash
2. $ sudo reboot
3. $ cd /home/pi/Dexter/GrovePi/Script
4. $ bash ./update_grovepi.sh
5. $ sudo reboot
6. Now when the Raspberry pi is powered down, stack the Grove Pi on top of the Raspberry Pi. 
7. $ sudo i2cdetect -y 1 # check

## Run InfluxDB Client

1. Edit `grove-influxdb-client.py` to add a token, bucket, org, measurement and sensors.
2. $ python3 grove-influxdb-client.py # python >= 3.6

## Credits

I established this playbook referring to the following user's repositories.

* [https://github.com/glennklockwood/rpi-ansible](https://github.com/glennklockwood/rpi-ansible)