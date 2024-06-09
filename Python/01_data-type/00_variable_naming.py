# 변수명 작성 규칙 

# 1. 변수명은 스네이크 케이스로 작성하며, 대소문자를 구분한다.
team_name = '오지라퍼스'
Team_name ='ohgiraffers'

print(team_name)
print(Team_name)


# 2. 영문과 숫자를 혼합해 작성할 수 있다. ( 단, 숫자를 가장 앞에 작성할 수 없음)
team_1_name = '오지라퍼스'


# 3. 한글 변수명도 지정할 수 있다.
팀명 = '오지라퍼스'

# 4. 언더바(_)를 제외한 특수문자는 사용이 불가능하다.
# team_@_name = '불가능'

# 언더바(_)
# 값을 무시하고 싶은 경우, 특정 값을 무시하기 위한 용도로 사용할 수 있다.

# 파이썬은 private이 없으니 _가 붙은 변수는 private으로 사용하자는 약속이 있음
x, *_, y={1,2,3,4,5}
print(x)
print(y)

# 숫자 값의 자릿수 구분을 위한 구분자로 사용할 수 있다.
million = 1_000_0000
print(million)


