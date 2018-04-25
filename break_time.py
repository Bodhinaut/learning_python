import time
import webbrowser
# Author: Kyle M. Shive
'''
This program is meant to act as a
Pomodor Break, so it will go off every 25 min
for 1 hour 
'''
total_breaks = 4
break_count = 0

print("This program started on " + time.ctime() )
while(break_count < total_breaks):
    time.sleep(25 * 60) # sleep takes in seconds, want a break every 25 min
    webbrowser.open("https://www.youtube.com/watch?v=1GGxzSPP0J0")
    break_count += 1


