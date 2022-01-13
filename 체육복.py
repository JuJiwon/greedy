# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve) :
    answer = 0
    
    # 여분이 있는 도난당한 학생들은 제외
    for v in set(lost).intersection(set(reserve)) :
        lost.remove(v)
        reserve.remove(v)
    # answer = 전체 학생 수-도난당한 학생
    answer = n-len(lost)
    
    stop = False
    # 한 명에게만 체육복을 빌릴 수 있는 학생이 없다면 while break
    while stop == False :
        stop = True
        for lostNumber in lost :
            # 한 명에게만 체육복을 빌릴 수 있다면
            if not (lostNumber-1 in reserve and lostNumber+1 in reserve) and (lostNumber-1 in reserve or lostNumber+1 in reserve) :
                stop = False
                # 빌림 처리
                lost.remove(lostNumber)
                answer += 1
                reserve.remove(lostNumber-1 if lostNumber-1 in reserve else lostNumber+1)
    
    # 빌리지 못한 학생들은 아예 빌리지 못하거나 빌릴 학생이 2명이므로 일괄 처리
    for lostNumber in lost :
        if lostNumber-1 in reserve or lostNumber+1 in reserve :
            answer += 1
    
    return answer