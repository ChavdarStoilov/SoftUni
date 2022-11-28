jobs = [int(job) for job in input().split(', ')]
index_interested = int(input())
count_cycles = 0
current_index = -1

while current_index != index_interested:
    current_index = jobs.index(min(jobs))
    current_job = min(jobs)
    jobs[current_index] = max(jobs) + 1
    count_cycles += current_job
print(count_cycles)