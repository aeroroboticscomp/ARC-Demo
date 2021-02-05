# Demo fibonnaci sequence

num_seq = 10

F1 = 1
F0 = 0

for i in range(num_seq):
    F2 = F1 + F0

    # shift numbers
    F0 = F1
    F1 = F2
    print(F2)

    