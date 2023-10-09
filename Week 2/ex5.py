import numpy as np

def f(x):
    
    final = x * (np.sqrt(x + 1)  - np.sqrt(x))
    print("f(x) final is: " + str(final))
    return final

def g(x):
    final = x / (np.sqrt(x + 1) + np.sqrt(x))
    print("g(x) final is: " + str(final))
    return final

f(np.float64(500.0))
g(np.float64(500.0))
print("\n")

f(np.float32(500.0))
g(np.float32(500.0))
print("\n")

f(np.float16(500.0))
g(np.float16(500.0))