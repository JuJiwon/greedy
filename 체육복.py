# https://programmers.co.kr/learn/courses/30/lessons/42862

# 학생수 2<=n<=30, 도난학생 번호 배열 lost, 여벌학생 번호 배열 reserve
# 수업 들을 수 있는 학생수 최댓값 answer

n = 9
lost = [5,6,8,1,2]
reserve = [2,3,1,4,8,9]

answer = 0

# for lostNumber in lost.copy() :
#     if lostNumber in reserve :
#         lost.remove(lostNumber)
#         reserve.remove(lostNumber)
# answer = n - len(lost)

for v in set(lost).intersection(set(reserve)): 
    lost.remove(v)
    reserve.remove(v)
answer = n-len(lost)

stop = False
while stop == False :
    stop = True
    for lostNumber in lost :
#        빌려줄 수 있는 사람이 1명일 때
        if not (lostNumber-1 in reserve and lostNumber+1 in reserve) and (lostNumber-1 in reserve or lostNumber+1 in reserve) :
            stop = False
            lost.remove(lostNumber)
            answer += 1
            reserve.remove(lostNumber-1 if lostNumber-1 in reserve else lostNumber+1)

for lostNumber in lost :
    if lostNumber-1 in reserve and lostNumber+1 in reserve :
        answer += 1
print(answer)