def simpleArraySum(ar):
    last_digit = ar[-1]
    total = 0
    even = len(ar) % 2 == 0
    size = len(ar) if even else len(ar) -1
    
    for i in range(0, size, 2):
        total += sum(ar[i:i+2])
        
    if(not even):
        total += last_digit
    
    return total
    
if __name__ == "__main__":
    print(simpleArraySum([1, 2, 3, 4, 10, 11]))
