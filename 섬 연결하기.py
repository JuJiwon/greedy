# https://programmers.co.kr/learn/courses/30/lessons/42861
# kruskal algorithm

def findParent(costs, parent) :

    tempParent = parent[:]
    for cost in costs :
        nodes = sorted(cost[:2])
        if tempParent[nodes[0]] < tempParent[nodes[1]] : tempParent[nodes[1]] = tempParent[nodes[0]]
        elif tempParent[nodes[0]] > tempParent[nodes[1]] : tempParent[nodes[0]] = tempParent[nodes[1]]

    if tempParent == parent : return parent
    else : return findParent(costs, tempParent)

def minimumCost(costs, parent, n, index) :

    slicedCosts = costs[:index] if index==len(costs)-1 else costs[:index]+costs[index+1:]
    index -= 1
    if index < 0 : return list(map(lambda x : x[2], costs))
    elif parent == findParent(slicedCosts, list(map(lambda x : x, range(n)))) : return minimumCost(slicedCosts, parent, n, index)
    else : return minimumCost(costs, parent, n, index)

def solution(n, costs) :

    answer = 0
    costs.sort(key = lambda x : x[2])
    print(costs)

    parent = findParent(costs, list(map(lambda x : x, range(n))))
    answer = sum(minimumCost(costs, parent, n, len(costs)-1))

    return answer

# print(str(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))+', 4')
print(str(solution(7, [[3,6,13],[0,6,12],[0,3,28],[4,6,73],[1,3,24],[1,0,67],[0,4,17],[1,4,62],[4,5,45],[2,4,20],[2,5,37]]))+', 123')