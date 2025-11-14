L = [1,2,3,4,5,6,7,8,9]
k = 0
while k < len(L):
    x = L[k] % 2
    if x == 0:
        print(L[k])
    k += 1