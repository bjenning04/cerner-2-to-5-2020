#!/usr/bin/env python

"""
battery_info: Tool to parse battery information out of Android logs and output in an easy to read format.
Usage:
  battery_info <log file>
"""
import sys

with open(sys.argv[1]) as oldfile, open(sys.argv[2], 'w') as newfile:
    for line in oldfile:
        if 'healthd: battery l=' in line:
            x = line.split('[')[1].lstrip().split()
            offset = x[0].replace(']', '')
            level = [k for k in x if 'l=' in k][0].split('=')[1]
            voltage = [k for k in x if 'v=' in k][0].split('=')[1]
            temp = [k for k in x if 't=' in k][0].split('=')[1]
            current = [k for k in x if 'c=' in k][0].split('=')[1]
            newfile.write(offset + "," + level + "," + voltage + "," + temp + "," + current + ',\n')
# cerner_2^5_2020