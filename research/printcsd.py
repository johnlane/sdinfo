#!/usr/bin/env python2
import sys

def unstuff(x, start, size):
    return (x >> start) & (2**size - 1)

def main(name, args):
    if len(args) != 1:
        print "Syntax: %s <card>" % (name, )
        print "Example: %s mmcblk0" % (name, )
        return 100

    card = args[0]
    dev = "/sys/class/block/%s/device/csd" % (card, )
    csd = int(file(dev).read(), 16)
    write_block_size = 2**unstuff(csd,22,4)
    erase_block_size = write_block_size*(unstuff(csd,39,7)+1)
    print "Erase block size of %s is %d bytes." % (card, erase_block_size)

sys.exit(main(sys.argv[0], sys.argv[1:]))
