# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0

    people.sort(reverse = True)

    while len(people) > 0 :
        i = people[0]
        if i <= limit/2 :
            answer += len(people)//2 + len(people)%2
            break
        else :
            j = people[-1]
            people.remove(i)
            if i+j <= limit : people.remove(j)
            answer += 1
                
    return answer

print(str(solution([70, 50, 80, 50], 100))+', 3')
print(str(solution([70, 80, 50], 100))+', 3')