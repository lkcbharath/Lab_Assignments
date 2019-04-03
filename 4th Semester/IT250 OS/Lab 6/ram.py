from fifo_ram import *
from lru_ram import *
from opt_ram import *

def main():
    frame_size = 3
    ref_list = [9,2,1,2,0,5,0,4,2,3,0,3,1,2,9,0,5,3,4,0]
    x = fifo(frame_size,ref_list)
    y = opt(frame_size,ref_list)
    z = lru(frame_size,ref_list)

    x_r = x.count('H')/x.count('M')
    y_r = y.count('H')/y.count('M')
    z_r = z.count('H')/z.count('M')

    if (x_r>=y_r) and (x_r>=z_r):
        print('Best H-M ratio is of FIFO: ',x_r)
    elif (y_r>=x_r) and (y_r>=z_r):
        print('Best H-M ratio is of Optimal: ',y_r)
    else:
        print('Best H-M ratio is of LRU: ',z_r)
    
if __name__ == '__main__':
    main()