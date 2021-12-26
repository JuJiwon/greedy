# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = number[:]

    index = 0
    while index != len(answer)-1 and k != 0 :
        if int(answer[index]) < int(answer[index+1]) :
            answer = answer[:index]+answer[index+1:]
            if index != 0 : index -= 1
            k -= 1
        else :
            index += 1
    if k != 0 :
        answer = answer[:len(answer)-k]

    return answer

print(str(solution('1924', 2))+', 94')
print(str(solution('1231234', 3))+', 3234')
print(str(solution('4177252841', 4))+', 775841')