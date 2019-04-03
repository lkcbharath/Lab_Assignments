def fifo(frame_size,ref_list):
    ram = [-1 for i in range(frame_size)]
    hit_or_miss = []
    i = 0
    for x in ref_list:
        # miss
        if x not in ram:
            ram[i] = x
            i = (i+1)%frame_size
            hit_or_miss.append('M')
        else:
            hit_or_miss.append('H')
    
    return hit_or_miss


def main():
    frame_size = 3
    ref_list = [9,2,1,2,0,5,0,4,2,3,0,3,1,2,9,0,5,3,4,0]
    l = fifo(frame_size,ref_list)

    print(l.count('M'))
    print(l.count('H'))

if __name__ == '__main__':
    main()