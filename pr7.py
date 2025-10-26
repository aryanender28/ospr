# Priority Scheduling (Preemptive and Non-Preemptive)

def priority_scheduling(processes, preemptive=False):
    n = len(processes)
    time = 0
    completed = 0
    gantt = []
    waiting = [0]*n
    turnaround = [0]*n
    remaining = [p[2] for p in processes]  # burst times
    start_time = [-1]*n

    while completed != n:
        # Find available processes
        available = [i for i in range(n) if processes[i][1] <= time and remaining[i] > 0]
        if available:
            # Select highest priority (lower value = higher priority)
            idx = min(available, key=lambda i: processes[i][3])
            if start_time[idx] == -1:
                start_time[idx] = time
            gantt.append(processes[idx][0])

            remaining[idx] -= 1
            time += 1

            if remaining[idx] == 0:
                completed += 1
                finish_time = time
                turnaround[idx] = finish_time - processes[idx][1]
                waiting[idx] = turnaround[idx] - processes[idx][2]
            elif not preemptive:  # Non-preemptive → run fully
                time += remaining[idx]
                remaining[idx] = 0
                completed += 1
                finish_time = time
                turnaround[idx] = finish_time - processes[idx][1]
                waiting[idx] = turnaround[idx] - processes[idx][2]
        else:
            time += 1  # idle time

    print("\nPr\tAT\tBT\tPR\tWT\tTAT")
    for i, p in enumerate(processes):
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{waiting[i]}\t{turnaround[i]}")

    print("\nGantt Chart:", ' -> '.join(gantt))
    print("Average Waiting Time:", sum(waiting)/n)
    print("Average Turnaround Time:", sum(turnaround)/n)


# ---- Input Section ----
# process_id, arrival_time, burst_time, priority
processes = [
    ["P1", 0, 4, 2],
    ["P2", 1, 3, 1],
    ["P3", 2, 1, 3]
]

print("=== Non-Preemptive Priority Scheduling ===")
priority_scheduling(processes, preemptive=False)

print("\n=== Preemptive Priority Scheduling ===")
priority_scheduling(processes, preemptive=True)
