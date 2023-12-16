import math


# Variant 5
def evaluate():
    start = 1
    end = 2
    step = 0.2

    i = start
    while i <= end:
        print(math.cos(i) * math.pow(math.e, -i))
        i += step


evaluate()
