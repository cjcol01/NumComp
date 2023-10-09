import numpy as np

def piSquared(n):
    sum = 0.0  # Use a float for proper division
    for k in range(1, n + 1):  # Note that Python's range is exclusive, so we need n + 1 to include n.
        sum += 1 / (k ** 2)
    return sum

def table(list_n):
    pi_constant = (1 / 6) * (np.pi ** 2)
    
    print("Power\t\tConstant\t\tCalculated\t\tError")
    print("-----\t\t--------\t\t----------\t\t-----")

    for n in list_n:
        calculated = piSquared(n)
        pi_error = abs(calculated - pi_constant)
        
        # print(f"{n}\t\t{np.float64(pi_constant)}\t{np.float64(calculated)}\t{np.float64(pi_error)}") # float 64, but messes up table
        print(f"{n:<15}{pi_constant:<25.15f}{calculated:<25.15f}{pi_error:<25.15f}") # sorts table

if __name__ == "__main__":
    list_n = [10, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8, 10 ** 9]
    table(list_n)
