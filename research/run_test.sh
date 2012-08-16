#!/bin/bash

DEVFPATH=$1
DEV=`basename ${DEVFPATH}`

ERASESIZE=`cat /sys/block/${DEV}/device/preferred_erase_size 2>/dev/null`

if mount | grep "^${DEVFPATH}.* / " ; then
    echo Refusing to run on root filesystem
    exit 1
fi
echo Making sure the device has no mounted partitions
umount ${DEVFPATH}p* 

for F in name oemid manfid hwrev fwrev; do
    echo $F `cat /sys/block/${DEV}/device/${F}` 
done
echo Running flashbench
flashbench --open-au --open-au-nr=5 --random --blocksize=4096 \
    --erasesize=${ERASESIZE:-4194304} ${DEVFPATH}

