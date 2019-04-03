def lru_index(ram,ref_list):
    return_index = -1
    least_index = len(ref_list)
    for i in range(len(ram)):
        ram_index = len(ref_list) - 1 - ref_list[::-1].index(ram[i])
        if ram_index < least_index:
            least_index = ram_index
            return_index = i
    
    return return_index

def lru(frame_size,ref_list):
    ram = []
    hit_or_miss = []
    i = 0
    for x in ref_list:
        # miss
        if x not in ram:
            if len(ram)<frame_size:
                ram.append(x)
            else:
                index = lru_index(ram,ref_list[:i])
                ram[index] = x
            hit_or_miss.append('M')

        else:
            hit_or_miss.append('H')
        
        i+=1
    
    return hit_or_miss


def main():
    frame_size = 3
    ref_list = [9,2,1,2,0,5,0,4,2,3,0,3,1,2,9,0,5,3,4,0]
    # frame_size = 4
    # ref_list = [7,0,1,2,0,3,0,4,2,3,0,3,2,1]
    l = lru(frame_size,ref_list)
    print(l.count('M'))
    print(l.count('H'))
if __name__ == '__main__':
    main()