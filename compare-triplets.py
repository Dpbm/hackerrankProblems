def compareTriplets(a, b):
    # a and b are arrays
    alice = 0
    bob   = 0
    
    for i in range(3):
        if(a[i] > b[i]):
            alice += 1
        elif (a[i] < b[i]):
            bob += 1

    return [alice, bob]
    

if __name__ == '__main__':
    print(compareTriplets([1, 2, 3], [3, 2, 1]))
