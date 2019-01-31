#include <linux/init.h>
#include <linux/module.h>

static int hello_start(void)
{
    printk(KERN_ALERT "Loading hello module...\n");
    return 0;
}

static void hello_end(void)
{
    printk(KERN_ALERT "Goodbye Mr.\n");
}

module_init(hello_start);
module_exit(hello_end);

