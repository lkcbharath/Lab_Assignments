def result(t1,t2,type):
    print("Average waiting time of " + type + " is " + str(t1))
    print("Average turnaround time of " + type + " is " + str(t2))

def fcfs(p):
    n = len(p)
    wait_times = [0 for i in range(n)]
    avg_wait_time = 0
    avg_turn_time = 0

    for i in range(1,n):
        wait_times[i] = wait_times[i-1] + p[i-1]
    
    for i in range(n):
        avg_wait_time += wait_times[i]
        avg_turn_time += wait_times[i] + p[i]
    
    avg_wait_time = avg_wait_time/n
    avg_turn_time = avg_turn_time/n

    result(avg_wait_time,avg_turn_time,'FCFS')

def sjf(p1):
    p = p1[::]
    p.sort()
    
    n = len(p)
    wait_times = [0 for i in range(n)]
    avg_wait_time = 0
    avg_turn_time = 0

    for i in range(1,n):
        wait_times[i] = wait_times[i-1] + p[i-1]

    for i in range(n):
        avg_wait_time += wait_times[i]
        avg_turn_time += wait_times[i] + p[i]
    
    avg_wait_time = avg_wait_time/n
    avg_turn_time = avg_turn_time/n

    result(avg_wait_time,avg_turn_time,'SJF')

def rr(p,quantum):

    rem_burst_times = p[::]
    t = 0
    n = len(p)
    wait_times = [0 for i in range(n)]
    
    while True:
        done = True

        for i in range(n):
            if rem_burst_times[i]:
                done = False

                if rem_burst_times[i] > quantum:
                    t += quantum
                    rem_burst_times[i] -= quantum
                else:
                    t += rem_burst_times[i]
                    wait_times[i] = t - p[i]
                    rem_burst_times[i]  = 0
        if done:
            break
    
    turn_times = [(p[i] + wait_times[i]) for i in range(n)]

    sum_wait = 0
    sum_turn = 0
    for i in range(n):
        sum_wait += wait_times[i]
        sum_turn += turn_times[i]
    
    sum_wait = (sum_wait)/n
    sum_turn = (sum_turn)/n
    
    result(sum_wait,sum_turn,'RR')


def main():
    # processes = list(input("Enter the Burst times of processes"))
    processes = []
    processes.append(10)
    processes.append(29)
    processes.append(3)
    processes.append(7)
    processes.append(12)

    fcfs(processes)
    sjf(processes)
    rr(processes,5)



if __name__ == '__main__':
    main()