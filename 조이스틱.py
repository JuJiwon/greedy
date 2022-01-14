# https://programmers.co.kr/learn/courses/30/lessons/42860

def getMoves(target) :
    if target <= 26-target :
        return target
    else :
        return 26-target

def solution(name) :
    print(name)
    answer = 0

    # int 데이터로 변환
    nameIdx = list()
    for data in name :
        nameIdx.append(ord(data)-65)
    incorrectCharIdx = list()

    for idx, inputChar in enumerate(nameIdx) :
        if inputChar != 0 :
            answer += getMoves(inputChar)
            incorrectCharIdx.append(idx)

    if len(incorrectCharIdx) != 0 :
        currentCursor = 0
        while len(incorrectCharIdx) != 0 :
            smallistDistance = float('inf')
            nextIdx = 0
            for charIdx in incorrectCharIdx :
                distanceA, distanceB = abs(currentCursor-charIdx), abs(currentCursor)+abs(len(nameIdx)-charIdx-1)+1
                if distanceA < smallistDistance or distanceB < smallistDistance :
                    smallistDistance = distanceA if distanceA < distanceB else distanceB
                    nextIdx = charIdx
            answer += smallistDistance
            currentCursor = nextIdx
            incorrectCharIdx.remove(currentCursor)

    return answer

# print(str(solution("AKKAAAAAAAKKK"))+', 57')
# print(str(solution("KAAKKKKAAA"))+', 56')
print(str(solution("KKKAAK"))+', 44')
