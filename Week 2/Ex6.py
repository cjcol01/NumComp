import numpy as np

list_n = [10, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8] #10 ** 9]
list_sum = [None] * 10

def piSquared(list_n):
    

    for count, value in enumerate(list_n):
        sum = 0
        n = list_n[count]
        for k in range(1, n):
            sum += 1 / (k ** 2)
            if k % 10000000 == 0:
                print("10 million increment")

        list_sum[count] = sum
    return sum


def table():
    pi_constant = (1 / 6 * np.float64(np.pi) ** 2)

    print("power \t\t constant \t\t calculated \t\t error")
    for i in range(len(list_n)):
        pi_error = list_sum[i] - pi_constant
        print(str(list_n[i]) + "\t\t " + str(pi_constant) +"\t " + str(list_sum[i]) + "\t " + str(pi_error))
        pass

piSquared(list_n)
table()
