# SDInfo

SDInfo will display information about an SD card. It is non-destructive
(i.e. data is safe).

## Usage

    $ sdinfo.py mmcblk0

## Status

This is very much a work in progress and should be considered incomplete.
It is made available in the hope that others may find it useful.

Written on Arch Linux.

The latest version is available at ...

## License

MIT License. See LICENSE file.

## Further information

The 'research' directory contains scripts and information collected in the
course of writing SDInfo.

### flashbench

FlashBench is a benchmarking tool for sd cards. Obtain from [origin](http://git.linaro.org/gitweb?p=people/arnd/flashbench.git;a=summary). It is also in the [Arch Linux AUR](http://aur.archlinux.org/packages.php?ID=46684).

For details refer to its [README](http://git.linaro.org/gitweb?p=people/arnd/flashbench.git;a=blob;f=README;h=3cb632cb83f0db934b7c112f8650f8e0718495e9;hb=2e30b1968a66147412f21002ea844122a0d5e2f0).

run_test.sh is a wrapper for flashbench, located in the research directory.

#### Results example

This result is for a card that I have, I don't know wnat to make of this output.
Nothing drastic seems to happen until we hit the 8K boundary.

    # flashbench -a /dev/mmcblk0  --blocksize=1024
    align 2147483648	pre 1.61ms	on 2.23ms	post 1.98ms	diff 433µs
    align 1073741824	pre 1.31ms	on 1.68ms	post 1.51ms	diff 274µs
    align 536870912	pre 1.42ms	on 1.87ms	post 1.73ms	diff 291µs
    align 268435456	pre 1.5ms	on 1.98ms	post 1.74ms	diff 358µs
    align 134217728	pre 1.53ms	on 2.09ms	post 1.93ms	diff 360µs
    align 67108864	pre 1.42ms	on 1.88ms	post 1.7ms	diff 315µs
    align 33554432	pre 1.62ms	on 2.49ms	post 2.24ms	diff 565µs
    align 16777216	pre 1.82ms	on 2.47ms	post 2.27ms	diff 428µs
    align 8388608	pre 1.68ms	on 2.62ms	post 2.38ms	diff 584µs
    align 4194304	pre 1.88ms	on 2.61ms	post 2.34ms	diff 500µs
    align 2097152	pre 1.79ms	on 2.39ms	post 2.24ms	diff 372µs
    align 1048576	pre 1.78ms	on 2.5ms	post 2.11ms	diff 558µs
    align 524288	pre 1.83ms	on 2.46ms	post 2.23ms	diff 432µs
    align 262144	pre 1.75ms	on 2.47ms	post 2.25ms	diff 471µs
    align 131072	pre 1.79ms	on 2.35ms	post 2.25ms	diff 330µs
    align 65536		pre 1.78ms	on 2.53ms	post 2.24ms	diff 520µs
    align 32768		pre 1.75ms	on 2.43ms	post 2.15ms	diff 478µs
    align 16384		pre 1.77ms	on 2.37ms	post 2.18ms	diff 399µs
    align 8192		pre 2.06ms	on 1.95ms	post 2.02ms	diff -90026n
    align 4096		pre 2.17ms	on 2.19ms	post 2.11ms	diff 51.3µs
    align 2048		pre 2.15ms	on 2.26ms	post 2.19ms	diff 83.9µs
    
    # ./run_test.sh /dev/mmcblk0
    Making sure the device has no mounted partitions
    name 00000
    oemid 0x534d
    manfid 0x00001b
    hwrev 0x1
    fwrev 0x0
    Running flashbench
    4MiB    3.34M/s 
    2MiB    3.55M/s 
    1MiB    1.84M/s 
    512KiB  868K/s  
    256KiB  429K/s  
    128KiB  212K/s  
    64KiB   106K/s  
    32KiB   53.1K/s 
    16KiB   26.7K/s 
    8KiB    26.5K/s 
    4KiB    25.9K/s 

