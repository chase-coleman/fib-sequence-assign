#F(n) = F(n-1) + F(n-2)

def fib(n):
    if n < 0: return "This is for non-negative integers only"
    fib_seq = []
    for i in range(0, n+1, 1):
        if len(fib_seq) < 2:
            fib_seq.append(i)
        else:
            new_fib = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(new_fib)
    print(fib_seq[n])


# fib_seq = [0, 1, 1, 2, 3, 5]
# last_index = fib_seq[-1]
# second_last = fib_seq[-2]

# print(f"this is the last index: {last_index}")
# print(f"this is the second to last index: {second_last}")
# print(last_index + second_last)

print(fib(7)) # == 13
print(fib(0)) # == 0
print(fib(-1)) # non-negatives only
