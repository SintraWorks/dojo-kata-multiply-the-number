import math

def multiply(n):
    input_length = int(math.log10(abs(n))) + 1 if n != 0 else 0
    return n * 5 ** input_length
