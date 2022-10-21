# time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
# 2018/04/03 17:20:32

import time
result = time.strftime("%Y/%m/%d %H:%M:%S") # %Y:년, %m:월, %d:일, %H:시, %M:분, %S:초
print(result)



