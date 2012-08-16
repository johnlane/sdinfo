#!/usr/bin/env python
# Read SD card Card Specific Data register bits for the erase block size
# NOT valid for Multi Media Cards!

# Debian GNU/Linux
# Copyright (C) 2011 Free Software Foundation, Inc.
# This is free software;  for copying, see the GNU General Public
# License version 2, or (at your option) any later version.
# There is NO warranty.
#
# Sourced from: http://www.systemateka.com/usbboot.html

import sys

def unstuff(x, start, size):
    return (x >> start) & (2**size - 1)

def main(name, args):
    if len(args) != 1:
        print "Syntax: %s <>" % (name, )
        print "Example: %s /sys/class/block/mmcblk0/device/csd" % (name, )
        return 100

    # read in 128 bits of csd register
    csd = int(file(args[0]).read(), 16)

    write_block_size = 2**unstuff(csd,22,4)
    erase_sector_size = unstuff(csd,39,7)+1
    erase_block_size = write_block_size*(erase_sector_size)
    print "Erase block size is %d bytes." % (erase_block_size)

sys.exit(main(sys.argv[0], sys.argv[1:]))
