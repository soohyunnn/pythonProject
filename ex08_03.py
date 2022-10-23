# 리스트의 더하기와 extend 함수
# 리스트 a에 +기호를 사용하는 경우에 대해서 먼저 살펴본다.
a = [1, 2, 3]
print(id(a))

# id 함수는 입력으로 받은 리스트 a의 주소 값을 돌려준다.
a = a + [4, 5]
print(a)

# 리스트 a에 4,5 를 추가한 후 주소값 확인
print(id(a))

# => 주소 값이 다르기 때문에 +를 사용하면 리스트 a의 값이 변하는 것이 아니라 두 리스트가 더해진 새로운 리스트가 반환된다는 것을 확인할 수 있따.
print("################")
# extend 사용
a = [1, 2, 3]
print(id(a))

a.extend([4,5])
print(a)
print(id(a))

# => extend를 사용하여 리스트 값을 추가해주면 주소 값이 변하지 않고 그대로 유지된다.