# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0

    people.sort(reverse = True)
    largestN = 0
    smallestN = len(people)-1

    while largestN < smallestN :
        i = people[largestN]
        if i <= limit/2 :
            answer += (smallestN-largestN+1)//2 + (smallestN-largestN+1)%2
            break
        else :
            j = people[smallestN]
            if i+j <= limit : smallestN -= 1
            largestN += 1
            answer += 1
    if largestN == smallestN : answer += 1
                
    return answer

print(str(solution([70, 50, 80, 50], 100))+', 3')
print(str(solution([70, 80, 50], 100))+', 3')