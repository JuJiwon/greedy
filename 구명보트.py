# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0

    people.sort(reverse = True)

    while len(people) > 1 :
        i = people[0]
        for j in people[1:] :
            if i + j <= limit :
                people.remove(j)
                break
        people.remove(i)
        answer += 1
    if len(people) == 1 : answer += 1
    return answer

print(str(solution([70, 50, 80, 50], 100))+', 3')
print(str(solution([70, 80, 50], 100))+', 3')