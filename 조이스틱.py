# https://programmers.co.kr/learn/courses/30/lessons/42860

from collections import namedtuple
from turtle import back


def counter(target) :
    if target <= 26-target :
        return target
    else :
        return 26-target

def searchLargestAlpha(nameData) :

    # A 모두 찾고 인덱스 저장하기
    alphaList = list()
    wasAlpha = False
    alphaStart = 0
    alphaEnd = 0
    for i in range(len(nameData)) :
        if nameData[i] == 0 :
            if not wasAlpha :
                alphaStart = i
                alphaEnd = i
                wasAlpha = True
            else :
                alphaEnd = i
        else :
            if wasAlpha :
                alphaList.append([alphaStart, alphaEnd])
                wasAlpha = False
    if alphaEnd == len(nameData)-1 :
        alphaList.append([alphaStart, alphaEnd])

    # 큰 A 찾기
    largestAlpha = alphaList[0]
    for alpha in alphaList : 
        if largestAlpha[1]-largestAlpha[0]+1 < alpha[1]-alpha[0]+1 : largestAlpha = alpha
    return largestAlpha

def solution(name) :
    answer = 0
    nameData = list()

    # 인덱스 데이터로 변환
    for data in name :
        nameData.append(ord(data)-65)
    
    # nameData의 첫 데이터 처리
    answer += counter(nameData[0])

    if 0 not in nameData :
        del nameData[0]
        for data in nameData :
            answer += counter(data)+1
    else :
        # largestAlpha 찾음
        largestAlpha = searchLargestAlpha(nameData)

        # largestAlpha가 한쪽 끝에 붙어있다면 최소 이동 방향으로 처리함.
        if largestAlpha[0] <= 1 :
            del nameData[:largestAlpha[1]+1]
            for data in list(reversed(nameData)) :
                answer += counter(data)+1
        elif largestAlpha[1] == len(nameData)-1 :
            del nameData[largestAlpha[0]:]
            del nameData[0]
            for data in nameData :
                answer += counter(data)+1
        else :
            frontDistance = ((largestAlpha[0]-1)*2)
            backDistance = (len(nameData)-largestAlpha[1]-1)*2-1
            # largestAlpha가 되돌아가는 횟수보다 작다면 처리함.
            if largestAlpha[1] <= frontDistance and len(nameData)-largestAlpha[0] <= backDistance :
                del nameData[0]
                for data in nameData :
                    answer += counter(data)+1
            # largestAlpha가 되돌아가는 횟수보다 크므로 최소 이동 방향으로 처리한 뒤 되돌아가야 함.
            else :
                del nameData[0]
                if frontDistance <= backDistance :
                    for data in nameData[:largestAlpha[0]-1] :
                        answer += counter(data)
                    answer += frontDistance
                    del nameData[:largestAlpha[1]]
                    for data in list(reversed(nameData)) :
                        answer += counter(data)+1
                else :
                    for data in nameData[largestAlpha[1]:] :
                        answer += counter(data)
                    answer += backDistance+1
                    del nameData[largestAlpha[0]-1:]
                    for data in nameData :
                        answer += counter(data)+1
                

    return answer

print(str(solution("AKKAAAAAAAKKK"))+', 57')
print(str(solution("KAAKKKKAAA"))+', 56')
print(str(solution("KKKAAK"))+', 44')