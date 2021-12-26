# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0

    people.sort(reverse = True)
    remaining = list(range(len(people)))
    departed = list()

    for i in range(len(people)) :
        if i not in departed :
            remaining.remove(i)
            departed.append(i)
            for j in remaining :
                if people[i] + people[j] <= limit :
                    remaining.remove(j)
                    departed.append(j)
                    break
            answer += 1

    return answer

print(str(solution([70, 50, 80, 50], 100))+', 3')
print(str(solution([70, 80, 50], 100))+', 3')