import sys
import re

avg=0.0
count=0

for line in sys.stdin:
    m = re.search(': (\d+[\.]\d+)', line)
    if m:
        avg += float(m.group(1))
        count += 1

print(f'Average CPU time: {avg/count}')