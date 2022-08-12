

def plusMinus(arr):
    """ total = len(arr)

    negatives = 0
    positives = 0
    zeros = 0

    for i in arr:
        if(not i):
            zeros += 1
        elif(i < 0):
            negatives += 1
        else:
            positives += 1

    print(f"{(positives/total):.6f}")
    print(f"{(negatives/total):.6f}")
    print(f"{(zeros/total):.6f}") """

    total = len(arr)
    sorted_array = sorted(arr)

    negatives = 0
    zeros = 0

    middle_point = (total - 1) // 2
    actual_index = middle_point

    # COUNT NEGATIVES
    if(sorted_array[middle_point] >= 0 and middle_point > 0):
        for index in range(actual_index, -1, -1):
            if(sorted_array[index] < 0):
                break

            actual_index = index

        negatives = len(sorted_array[:actual_index])
        sorted_array = sorted_array[actual_index:]

    elif (sorted_array[middle_point] < 0 and middle_point < len(sorted_array) - 1):
        for index in range(len(sorted_array)):
            if(sorted_array[index] >= 0):
                break

            actual_index = index

        negatives = len(sorted_array[:actual_index+1])
        sorted_array = sorted_array[actual_index+1:]

    # count zeros
    if(not sorted_array[0]):
        actual_index = 0
        for index in range(len(sorted_array)):
            if(sorted_array[index] > 0):
                break

            actual_index = index

        zeros = len(sorted_array[:actual_index+1])
        sorted_array = sorted_array[actual_index+1:]

    positives = len(sorted_array)

    print(f"{(positives/total):.6f}")
    print(f"{(negatives/total):.6f}")
    print(f"{(zeros/total):.6f}")


if __name__ == '__main__':
    plusMinus([0, -67, -74, -38, -72, -53, 0, -13, -95, -91, -100, -59, 0, -10, -68, -71, -62, -21, 0, -42, -57, -16, -66, -23, 0, -80, -63, -68, -65, -71, 0, -71, -15, -32, -
              26, -8, 0, -6, -51, -87, -19, -71, 0, -93, -26, -35, -56, -89, 0, -21, -74, -39, -57, -8, 0, -69, -29, -24, -99, -53, 0, -65, -42, -72, -18, -4, 0, -73, -46, -63, -78, -87])
