"""stopwatch_prettier.py
A simple stopwatch program
with colors and space
"""
import time
import pyperclip


class colors:
    red = "\033[31m"
    yello = "\033[33m"
    blue = "\033[34m"
    reset = "\033[0m"


print((
    "Press ENTER to begin. Afterward, press ENTER "
    "to \"click\" the stopwatch. Press Ctrl-C to quit"
))
input()  # press Enter to begin
print(f"{colors.red}Started{colors.reset}")
start_time = time.time()  # get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times
outputs = []
try:
    while True:
        input()
        cur_time = time.time()
        lap_time = round(cur_time - last_time, 2)
        total_time = round(cur_time - start_time, 2)

        output_plain = f"Lap #{lap_num:2}: {total_time:5.2f}({lap_time:5.2f})"
        output_colors = (
            f"Lap {colors.yello}#{lap_num:2}{colors.reset}: "
            f"{total_time:5.2f}({colors.blue}{lap_time:5.2f}{colors.reset})"
        )
        print(output_colors, end="")
        outputs.append(output_plain)
        lap_num += 1
        last_time = cur_time  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying
    pyperclip.copy("\n".join(outputs))
    print(f"\n{colors.red}Done{colors.reset}")
