def birthday(s, d, m):
    total = 0
 

    if(len(s) == 1 and m == 1 and d == s[0]): total += 1 

    for index in range(len(s)-1):
        totalSquares = s[index : index+m]
        print(totalSquares)        
        if(len(totalSquares) != m): pass
        
        if(sum(totalSquares) == d): total += 1
        
    return total

print(birthday([4], 1, 4))
