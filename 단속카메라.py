# https://programmers.co.kr/learn/courses/30/lessons/42884

def combineRoutes(routes) :
    tempRoutes = routes[:]
    i = 0
    while i < len(tempRoutes) :
        j = i+1
        while j < len(tempRoutes) and tempRoutes[i][1] >= tempRoutes[j][0] :
            start, end = [tempRoutes[i], tempRoutes[j]]
            tempRoutes[i] = [end[0], start[1]] if start[1] < end[1] else [end[0], end[1]]
            del tempRoutes[j]
            print(tempRoutes)
            j += 1
        i += 1
    if tempRoutes != routes : return combineRoutes(tempRoutes)
    else :
        return len(tempRoutes)

def solution(routes):

    answer = 0
    routes.sort(key = lambda x: x[0])

    answer = combineRoutes(routes)
    return answer

print(str(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))+', 2')