"""stopwatch.py
A simple stopwatch program
"""
import time

print((
    "Press ENTER to begin. Afterward, press ENTER "
    "to \"click\" the stopwatch. Press Ctrl-C to quit"
))
input()  # press Enter to begin
print("Started")
start_time = time.time()  # get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times
try:
    while True:
        input()
        cur_time = time.time()
        lap_time = round(cur_time - last_time, 2)
        total_time = round(cur_time - start_time, 2)

        print(f"Lap #{lap_num}: {total_time}({lap_time})", end="")
        lap_num += 1
        last_time = cur_time  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying
    print("\nDone")
