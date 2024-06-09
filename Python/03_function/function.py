# 함수 정의

# def 키워드를 사용해 함수를 정의하고 함수 이름, 다음에 괄호와 콜론을 작성한다.

def myfunction(): 
    print("hello")

myfunction()

def addNum(num1, num2): 
    print(num1 + num2)

addNum(2, 4)

def multiplyNum(num1): 
    return num1 * 0

result = multiplyNum(8)
print(result)


# 1. 위치 인자 = 위치로 매칭하는 방법
# 2. 키워드 인자 = 매개변수 이름으로 매칭하는 방법

def func(a, b): 
    print(a, b, sep=" ")

# 위치 매칭 
func('hello', 'world')

# 키워드 매칭
func(b='world', a='hello')

# 매개변수 기본 값 지정
def func2(a, b=3):
    return a + b

print(func2(10, 10))
print(func2(10))


# 가변 인자 (*args)
def add_many(*args): 
    result = 0
    for i in args:
        result = result + i 
    return result

print(add_many(1, 2, 3, 4, 5, 6, 6, 7, 7, 3, 4, 3, 4, 3, 43))


# 언패킹 인자
def sum(a, b, c): 
    return a + b + c

numbers = [1, 2, 3]

print(sum(*numbers))


# 람다 표현식

# 매개변수로 함수를 전달하기 위해 함수 구문을 사용하는 것이 번거롭고 
# 코드 낭비라고 생각될 때 함수를 간단하고 쉽게 선언하는 방법 

# 람다 기본식 예시
add = lambda x, y: x + y 
print(add(3, 5))


# Map
numers1 =  [1,2,3,4,5]
squared_numbers = map(lambda x : x**2, numers1)
print(list(squared_numbers))

#  Filter 조건에 맞는 요소 필터링 
numers2 = [1,2,3,4,5,6]
even_number = filter(lambda x: x%2 ==0, numers2)
print(list(even_number))

# 정렬 // 리스트 안에 튜플 정렬
# sorted(객체or배열, 정렬조건)
points = [(1,2),(3,1),(5,-1)]
# 튜플의 각 첫번째 인덱스 기준으로 정렬을 한다 . 
sorted_pintes = sorted(points,key=lambda x:x[1])
print(sorted_pintes)

