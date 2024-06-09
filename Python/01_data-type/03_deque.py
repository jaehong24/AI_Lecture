
# 양방향 큐 
# 컬렉션 프레임워크의 라이브러리 가지고 옴 deque 
from collections import deque  

dq = deque()

dq.append('a')
dq.append('b')
dq.append('c')

print(dq)

# 파이썬의 collections 모듈에서 제공하느 자로구조로 써 , 
# 양쪽 끝에 효율적인 삽입과 삭제가 가능하게 설계되었다.

dq.appendleft('x')
print(dq)

value = dq.pop()
print(value)
print(dq)

left_value = dq.popleft()
print(left_value)
print(dq)

