# 기초 메타 문자
"""
다음 중 정규식 a[.]{3,}b 과 매치되는 문자열은 무엇일까?

1. acccb
2. a....b
3. aaab
4. a.cccb

=> 정답 : 2
"""
import re

p = re.compile("a[.]{3,}b")

print(p.match("acccb"))    # None
print(p.match("a....b"))   # 매치 객체 출력
print(p.match("aaab"))     # None
print(p.match("a.cccb"))   # None

"""
실행결과 : 
None
<re.Match object; span=(0, 6), match='a....b'>
None
None

"""
