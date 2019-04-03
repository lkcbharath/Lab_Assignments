def opt_index(ram,ref_list):
    ram_in_ref_list = []
    for i in range(len(ram)):
        if ram[i] in ref_list and ref_list.index(ram[i]):
            ram_in_ref_list.append(ref_list.index(ram[i]))
        else:
            ram_in_ref_list.append(-1)
    
    if -1 in ram_in_ref_list:
        return ram_in_ref_list.index(-1)

    return ram_in_ref_list.index(max(ram_in_ref_list))
    

def opt(frame_size,ref_list):
    ram = []
    hit_or_miss = []
    # index of ref_list
    i = 0
    for x in ref_list:

        if x not in ram:
            if len(ram)<frame_size:
                ram.append(x)
            else:
                index = opt_index(ram,ref_list[i::])
                ram[index] = x

            hit_or_miss.append('M')

        else:
            hit_or_miss.append('H')

        i += 1


    return hit_or_miss


def main():
    frame_size = 3
    ref_list = [9,2,1,2,0,5,0,4,2,3,0,3,1,2,9,0,5,3,4,0]
    # frame_size = 4
    # ref_list = [7,0,1,2,0,3,0,4,2,3,0,3,2,1]
    # ref_list = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    l = opt(frame_size,ref_list)
    print(l.count('M'))
    print(l.count('H'))

if __name__ == '__main__':
    main()