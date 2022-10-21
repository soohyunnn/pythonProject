# 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트(C:\doit\myargv.py)를 작성해 보자.
import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)

# 터미널 실행 결과
# (python) (base) ➜  pythonProject python ex05_09.py 1 2 3 4 5 6 7 8 9 10
# 55