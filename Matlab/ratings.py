def countTeams(rating, queries):

    # HackerRank is organizing a chess tournament for its employees. There are n employees, having IDs 1, 2, ., n, where the ith employee has a rating of rating[i]. Two employees can form a team if they have the same rating, and one employee can be in at most one team.
    # There are q queries, each of the form (1, r). For each query, find the number of teams that can be formed from employees with IDs between / and r, inclusive. All queries are independent of each other.

    resultArray = []

    for query in queries:
        l = query[0]
        r = query[1]
        count = 0
        for i in range(l, r+1):
            for j in range(i+1, r+1):
                for k in range(j+1, r+1):
                    if rating[i-1] < rating[j-1] < rating[k-1] or rating[i-1] > rating[j-1] > rating[k-1]:
                        count += 1
        resultArray.append(count)

    return resultArray

if __name__ == '__main__':
    rating = [2, 3, 4, 2]
    queries = [[1, 4], [3, 4]]
    print(countTeams(rating, queries))  # 4
    rating = [1,1]
    queries = [[1,2], [1, 1]]
    print(countTeams(rating, queries))  # 1

    # for query in queries:
    #     joinedMembers = []
    #     if rating[query[0]-1] == rating[query[1]-1] and query[0] != query[1]:
    #         if query[0] not in joinedMembers and query[1] not in joinedMembers:
    #             joinedMembers.append(query[0])
    #             joinedMembers.append(query[1])
    #             resultArray.append(1)
    #         else:
    #             resultArray.append(0)
    #     else:
    #         resultArray.append(0)