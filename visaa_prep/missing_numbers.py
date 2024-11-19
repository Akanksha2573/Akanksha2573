def missingNumbers(arr, brr):
    # Write your code here
    freq_arr = {}
    freq_brr = {}
    for num in arr:
        freq_arr[num] = freq_arr.get(num, 0) + 1
    for num in brr:
        freq_brr[num] = freq_brr.get(num, 0) + 1
    missing = []
    for num in freq_brr:
        if freq_brr[num] > freq_arr.get(num, 0):
            missing.append(num)
    return sorted(missing)
