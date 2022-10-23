# 모듈 사용 방법
"""
C:\doit 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자. 명령 프롬프트 창에서 파이썬 셸을 열어 이 모듈을 import해서
사용할 수 있는 방법을 모두 기술하시오. (즉 다음과 같이 import mymod를 수행할 때 오류가 없어야 한다.)
"""

# 1. sys 모듈 사용하기
# 다음과 같이 sys.path에 c:\doit 이라는 디렉터리를 추가하면 C:\doit 이라는 디렉터리에 있는 mymod 모듈을 사용할 수 있게 된다.
import sys
sys.path.append("c:/doit")
import mymod

# 2. PYTHONAPATH 환경 변수 사용하기
# 다음처럼 PYTHONPATH 환경 변수에 C:\doit 디렉터리를 지정하면 C:\doit 디렉터리에 있는 mymod 모듈을 사용할 수 있게 된다.
set PYTHONPATH=c:\doit
python
import mymod

# 3. 현재 디렉터리 사용하기
# 파이썬 셸을 mymod.py가 있는 위치로 이동하여 실행해도 mymod 모듈을 사용할 수 있게 된다. 왜냐하면 sys.path 에는 현재 디렉터리인 .이 항상 포함되어 있기 때문이다.
c:\doit
python
import mymod


