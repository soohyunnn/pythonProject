# os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
# 1. C:\doit 디렉터리로 이동한다.
# 2. dir 명령을 실행하고 그 결과를 변수에 담는다.
# 3. dir 명령의 결과를 출력한다.

import os
os.chdir("/Users/actbase/PycharmProjects/pythonProject")

# 윈도우는 'dir' 맥북은 'is'
result = os.popen("ls")

print(result.read())