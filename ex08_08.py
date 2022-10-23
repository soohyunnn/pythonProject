# 역순 저장
"""
파일 객체의 readlines를 사용하여 모든 라인을 읽은 후에 reversed를 사용하여
역순으로 정렬한 다음 다시 파일에 저장한다.
AAA
BBB
CCC
DDD
EEE
"""

f = open('abc.txt', 'r')
lines = f.readlines() # 모든 라인을 읽음
f.close()

lines.reverse() # 읽은 라인을 역순으로 정렬

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()     # 포함되어 있는 줄 바꿈 문자 제거
    f.write(line)
    f.write('\n')       # 줄 바꿈 문자 삽입
f.close()

"""
변경 후 파일
EEE
DDD
CCC
BBB
AAA
"""


