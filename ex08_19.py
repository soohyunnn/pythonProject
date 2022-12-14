# 그루핑
# 문자열에서 휴대폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식 사용해서 작성
"""
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
import re

# 전화번호 패턴
pat = re.compile("\d{3}[-]\d{4}[-]\d{4}")

# 전화번호 패턴 중 뒤의 숫자 4개를 변경할 것이므로 필요한 앞부분을 아래와 같이 그루핑한다.
pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")

import re
s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)

