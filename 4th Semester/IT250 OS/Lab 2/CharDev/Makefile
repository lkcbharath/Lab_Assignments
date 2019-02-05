KDIR  := /lib/modules/$(shell uname -r)/build

obj-m += $(mname).o

all:
	$(MAKE) -C $(KDIR) M=$(shell pwd) modules
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
