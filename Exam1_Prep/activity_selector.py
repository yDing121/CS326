# def activity_select(s, f, k, n):
#     assert n == len(s) and n == len(f)
#
#     # Find the next activity that starts after the last one finishes
#     m = k + 1
#     while m < n and s[m] < f[k]:  # Correct the index and condition
#         m += 1
#
#     # If a valid next activity is found, recurse
#     if m <= n:
#         return {m} | activity_select(s, f, m, n)  # Union the sets
#     else:
#         return set()  # If no more activities can be selected, return an empty set

def activity_select(s, f, k, n):
    """
    Activity selection function based on CLRS4.
    s: array of start times
    f: array of finish times
    k: current index (typically starts with 0)
    n: total number of activities
    """
    # Initialize the list to hold the selected activities
    selected_activities = []

    # First, add the initial activity
    selected_activities.append(k+1)

    # Initialize the last activity index to the first selected activity
    last_activity = k

    # Iterate through the remaining activities
    for m in range(k + 1, n):
        # If the start time of activity m is greater than or equal to the finish
        # time of the last selected activity, select it
        if s[m] >= f[last_activity]:
            selected_activities.append(m+1)
            last_activity = m

    return selected_activities



if __name__ == '__main__':
    s = [1, 3, 0, 5, 3,5,6,7,8,2,12]
    f = [4,5,6,7,9,9,10,11,12,14,16]
    s = activity_select(s, f, 0, len(s))
    print(s)

    # s = [1, 3, 0, 5, 8, 5]  # Start times
    # f = [2, 4, 6, 7, 9, 9]  # Finish times
    # n = len(s)
    #
    # selected_activities = activity_select(s, f, 0, n)
    # print("Selected activities:", selected_activities)


