# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0

    people.sort(reverse = True)
    remaining = list(range(len(people)))
    departed = list()
    
    while len(remaining) > 1 :
        i = remaining[0]
        for j in remaining[1:] :
            if people[remaining[0]] + people[j] <= limit :
                remaining.remove(j)
                departed.append(j)
                break
        remaining.remove(i)
        departed.append(i)
        answer += 1
    if len(remaining) == 1 : answer += 1
    return answer

print(str(solution([70, 50, 80, 50], 100))+', 3')
print(str(solution([70, 80, 50], 100))+', 3')