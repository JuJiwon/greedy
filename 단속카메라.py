# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):

    answer = 0
    routes.sort(key = lambda x: x[1])

    while len(routes) > 0 :
        answer += 1
        i = 1
        while i < len(routes) :
            route = routes[i]
            if route[0] <= routes[0][1] : del routes[i]
            else : i += 1
        del routes[0]

    return answer

print(str(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))+', 2')