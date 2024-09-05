######## input
# 1 11
# 2 3
# 3 6
# 4 6
# 10 13
######## output
# processor 1: 1-11
# processor 2: 2-3 4-6 10-13
# processor 3: 3-6

def getMinCores(start, end):
    # Combine start and end times with an indicator of whether it's a start (1) or end (-1)
    events = []
    for i in range(len(start)):
        events.append((start[i], 1))  # Task starts
        events.append((end[i], -1))   # Task ends

    # Sort events by time, breaking ties by having task end (-1) before task start (1)
    events.sort(key=lambda x: (x[0], x[1]))

    maxCores = 0
    currentCores = 0

    # Process all events
    for event in events:
        currentCores += event[1]  # Add 1 for a start, subtract 1 for an end
        maxCores = max(maxCores, currentCores)  # Track the maximum number of cores used

    return maxCores

start = [1, 2, 3, 6, 10]
end = [11, 3, 6, 6, 13]
print(getMinCores(start, end))  # Output: 3
