def fcfs(queue,head):
    curr_head = head 
    track_movements = 0
    for x in queue:
        track_movements += abs(curr_head - x)
        curr_head = x
    
    return track_movements


def main():
    head = 60
    queue = [98, 67, 78, 30, 10, 45, 180, 20, 150, 35]
    print(fcfs(queue,head))

if __name__ == '__main__':
    main()