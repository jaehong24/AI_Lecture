#파이썬은 한 줄 주석만 허용 
# 기본 자료 형 

# 1. 숫자형
#  int : 정수 값을 가지는 자료형
#  float : 소수 값을 가지는 자료형

num1 = 1
num2 = 3.14 

print(type(num1))   
print(type(num2))  

# 연산

num3 = 11
num4 = 7

print(num3 + num4)
print(num3 - num4)
print(num3 * num4)
print(num3 / num4)
print(num3 % num4)


# 몫만 구하는 연산 
print(num3 // num4) #1

# 제곱 연산 
base = 9
exponent = 2
print(base ** exponent)  #81


# 2 논리형 (Bool, bool)
bool1 = True
bool2 = False

print(type(bool1))
print(type(bool2))

# 3. 문자형 (String, str)
fruit = 'apple'
print(fruit)

capasity = str(300) # 문자열로 변환 함순
print(type(capasity))

# """ """ 텍스트를 여러줄로 제공가능
print("""              
Long 코드보다 긴건 ? 
double 코드짧은건 ?
int 패딩 
      """)

# 문자열은 index를 가지고 있어 인덱싱을 통해 원하는 위치의 문자 하나를 추출할 수 있다.
# 위치의 문자 하나를 추출 할 수 있다.
# 0부터 시작하고 띄어쓰기를 포함한다. 
address = "대한민국 서울시 서초구"
print(address[5])
print(address[9])

# 슬라이싱 
print(address[9:]) # 9번 인덱스 부터 끝까지 
print(address[5:8])
print(address[1:12:4]) # 1번 부터 12 까지 출력 할 떄 4개씩 건너 띄고 출력
print(address[::-1]) # 문자열 뒤집기 
print(address[-3:]) # 뒤에서 3번쨰 부터 끝까지 출력 서초구 출력

# 문자열 * 연산
subject = 'python'
print(subject * 3 )   #문자열을 3번 출력 해준다. 

# 문자열 관련 메소드
# 1. replace()  : 문자열을 치환하는 메소드이다.
enroll_date = '2024/12/16'
rep_enroll_date = enroll_date.replace("/","-")
print(rep_enroll_date)

# 2. strip() : 제거할 문자 집합을 지정하는 메소드
origin = 'ohgiraffers'
wit_white_space =  '      oh giraffers'

# 공백 제거 
print(wit_white_space.strip())
print(wit_white_space.strip('  o'))
print(wit_white_space.strip('  os'))


# 3. 대소문자 관련 메소드
orign_str = 'hELLO wORLD!'
print(orign_str.upper())
print(orign_str.lower())
print(orign_str.capitalize())


# 4. 문자형 포맷
# 변수 포맷을 이용하여 문자열에 변수 값을 삽입할 수 있다.
# 변수 포맷 종류 
   # %s : 문자열
   # %c : 문자
   # %d : 정수
   # %f : 실수
x = 10
print("x is %d" %x)
y = 'code'
print("y is %s" %y)

# 인덱스를 지정하고, .format(이 안에 변수들을 넣고) 뿌릴 수 있다.
print("x is {0}" .format(x))
print("x is {0} y is {1}" .format(x,y))


# 형 변환
 # 암시적 형 변환 
print(True + 3 )
print(3 + 50)
# print(3 + '5') 

 # 명시적 형 변환
print(int('3') + 4) 
print(float('3'))
print(str(1))
print(str(1.0))
print(str({1,2,3}))