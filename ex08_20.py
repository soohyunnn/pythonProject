# 전방 탐색
"""
아래는 이메일 주소를 나타내는 정규식이다. 이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr등과 매치된다.
긍정형 전방 탐색 기법을 사용하여 .com, .net이 아닌 이메일 주소는 제외시키는 정규식을 작성하시오.

.*[@].*[.].*$

"""
import re

# .com과 .net에 해당되는 이메일 주소만을 매치하기 위해서 이메일 주소의 도메인 부분에 다음과 같은 긍정형 전방탐색 패턴을 적용한다.
pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))

"""
실행결과 :
<re.Match object; span=(0, 16), match='pahkey@gmail.com'>
<re.Match object; span=(0, 12), match='kim@daum.net'>
None
"""