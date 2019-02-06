To execute:
$ make
$ sudo insmod chardev.c
$ dmesg
(Note down major number MN)
$ sudo mknod /dev/(yourfilename) c $MN 0
$ cat /dev/(yourfilename)

For info:
$ lsmod

To unload:
$ rmmod hello.ko
