def max_subarray(arr):
    s = [arr[0]]

    for i in range(1, len(arr[1:])):
        s.append(max(s[i-1] + arr[i], arr[i]))
        # print(s)
    m = s[0]

    for i in s[1:]:
        if i > m:
            m = i

    return m

def max_subarray_backtrack(arr):
    cursum = arr[0]
    maxsum = arr[0]
    start = 0
    end = 0
    start_tmp = 0

    for i in range(1, len(arr)):
        if arr[i] > cursum + arr[i]:
            cursum = arr[i]
            start_tmp = i
        else:
            cursum += arr[i]

        if cursum > maxsum:
            maxsum = cursum
            start = start_tmp
            end = i
    print(f"Max sum:\t{maxsum}\nIndices (inclusive):\t{[start, end]}")
    return maxsum, start, end

if __name__ == '__main__':
    arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    # print(max_subarray(arr))
    max_subarray_backtrack(arr)