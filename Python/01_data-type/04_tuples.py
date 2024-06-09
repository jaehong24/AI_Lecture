
# Sequence Type : str, list, tuple

# 값이 연속적으로 나열된 자료형을 의미하며 다음 자료형이 해당된다.
# str :  문자열 값을 가지는 자료형
# list :  여러 값을 담을 수 있는 가변형 자료형
# tuple : 여러 값을 담을 수 있는 불변형 자료형

name = 'ohgiraffers'
print(type(name))

list = [0,1,2,3,]
print(type(list))

tuple  = (1,2,3)
print(type(tuple))


# Tuple

# phyton 에서 사용하는 자료형 중 하나로, 여러 개의 값을 하나의 데이터   구조로 묶어서
# 관리할 수 있는 불편 시퀀스다
# list 와 유사하지만 한 번 생성되면 각 요소 값을 수정하거나 삭제할 수 없다.
# 주로 데이터 집합을 안전하게 유지하거나 함수에서 여러 값을 반환 할 떄 사용된다. 

safari_tupe = ("Bear", "Korean", "Gorilla", "Pig")
print(safari_tupe)

# 튜플은 중첩으로 표현 가능
tuples = (1,2,'helllo'),('test',1,2,3,4)

# 리스트 처럼 인덱스로 접근가능
print(tuples)
print(tuples[0])
print(tuples[0][0])


# tuple 연산

# 불변 객체이므로 요소 값을 한번 할당하면 추가, 수정,삭제가 불가능하다
# tuples[0] = (1,2,3,4) -> 오류 발생

stud

testList = (1,2,3,4)
print(id(testList))

testList = (3,4,5)
print(id(testList))


# 튜플 간 연산

another_safari_tuple = ("monkey", "tiger" , "wolf")
print(another_safari_tuple + safari_tupe)
print(safari_tupe * 3)
print(len(safari_tupe + another_safari_tuple))