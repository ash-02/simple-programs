def select_activities(start, finish):
    num_activities = len(start) - 1
    c = [[0 for _ in range(num_activities + 2)] for _ in range(num_activities + 2)]
    selected_activities = [[0 for _ in range(num_activities + 2)] for _ in range(num_activities + 2)]
    
    for i in range(num_activities + 1):
        c[i][i] = 0
        c[i][i + 1] = 0
    c[num_activities + 1][num_activities + 1] = 0
    
    for length in range(2, num_activities + 2):
        for i in range(num_activities - length + 2):
            j = i + length
            c[i][j] = 0
            activity_index = j - 1

            while activity_index > i and finish[i] < finish[activity_index]:
                if finish[i] <= start[activity_index] and finish[activity_index] <= start[j] and c[i][activity_index] + c[activity_index][j] + 1 > c[i][j]:
                    c[i][j] = c[i][activity_index] + c[activity_index][j] + 1
                    selected_activities[i][j] = activity_index
                activity_index = activity_index - 1
    return c, selected_activities

def output_selected_activities(selected_activities, start, end):
    activity = selected_activities[start][end]
    if activity == 0:
        return
    output_selected_activities(selected_activities, start, activity)
    print(activity)
    output_selected_activities(selected_activities, activity, end)

start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
finish = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

c, selected_activities = select_activities(start, finish) 

# print("The maximum number of activities that can be selected is", c[0][len(start) - 1])

# output_selected_activities(selected_activities, 0, len(start) - 1)