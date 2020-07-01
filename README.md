# Raspberry Pi Ansible

## Bootstrapping

$ sudo pip3 install ansible

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

## Credits

I established this playbook referring to the following user's repositories.

* [https://github.com/glennklockwood/rpi-ansible](https://github.com/glennklockwood/rpi-ansible)