#!/bin/sh

# If you would like to do some extra provisioning you may
# add any commands you wish to this file and they will
# be run after the Homestead machine is provisioned.

wget -O - https://gist.github.com/rdok/005b5dbcf057a9a9fe4d209290793ee9/raw/949b34fb389bfd41c7e1fab96460fd32cf6615e2/setup_dev.sh | bash
wget -O - https://gist.githubusercontent.com/rdok/4e9b7a589f63c3d8219f/raw/617f720a4915ce7267ea4c47acf3eb35d3bcd0fb/prepare_vm.sh | bash


