
def diagonalDifference(arr):
    mainDiagonal = sum([ arr[i][i] for i in range(len(arr[0])) ])
    secondDiagonal = sum([ arr[i][len(arr[0]) - i - 1]  for i in range(len(arr[0])) ])
    
    return abs(secondDiagonal - mainDiagonal)
if __name__ == '__main__':
    print(diagonalDifference(
        [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]
        ]
    ))
