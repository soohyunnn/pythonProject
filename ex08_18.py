# 문자열 검색
# 다음 코드의 결과값은 무엇일까?
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
result = m.start() + m.end()

print(result)   # 10 출력

"""
정규식 [a-z]+은 소문자로 이루어진 단어를 뜻하므로 5 python 문자열에서 python과 매치될 것이다.
따라서 python 문자열의 인덱스 범위는 m.start()에서 m.end() 까지이므로 10이 출력된다.
"""

# "5 python" 문자열에서 n이 7번째 문자여서 m.end()의 값이 7이 나올것 같지만 다음과 같은 슬라이싱 규칙을 보면 이해가 쉽다.
a = "5 python"
print("a[2:8] :: " + a[2:8])
print("a[2:7] :: " + a[2:7])





