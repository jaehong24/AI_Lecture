# List

# 일련의 값이 모인 집합을 다루기 위한 자료형. 일반적인 프로그래밍
# 언어와 다르게 길이를 동적으로 조절할 수 있어 list라고 부른다.

fruit = ['orange', 'apple', 'pear', 'kiwi', 'apple']

print(fruit)
print(fruit[0])

# List 유용한 메소드

# 1. count() :  해당 리스트에 인자로 준 값이 몇 개 존재하는 지 확인하여 그 수를 반환 
print("apple : ", fruit.count('apple'))

# 2. index() :  인자로 준 값이 몇 번째 인덱스에 존재하는지 확인하여 그 인덱스를 반환한다.
# 같은 값이 리스트 내에 여러 개 존재하면 가장 처음에 존재하는 값의 인덱스를 반환한다.
print("index : ", fruit.index('apple'))

# 3번째 인덱스 뒤부터 apple이 어디에 있는지 검색
print("index : ", fruit.index('apple', 3))

# 3. reverse() : list의 값을 역으로 정렬한다.
fruit.reverse()
print(fruit)

# 4. append() : list 끝에 값을 덧붙여 추가한다.
fruit.append('pineapple')
print(fruit)

# 5. sort() : 요소를 정렬하는 메소드로 원본 list에 영향을 준다.
# 기본적으로 알파벳 첫 글자 기준으로 오름차순 정렬한다.
fruit.sort()
print(fruit)

# 내림차순 정렬
fruit.sort(reverse=True)
print(fruit)

# 단어 길이에 따라 정렬 
fruit.sort(key=len)
print(fruit)

# del 키워드
# 원본 배열 일부 요소 혹은 전체 목록을 제거할 수 있다.
abclist = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(abclist)

del abclist[0]
print(abclist)

# 1번째 부터 2까지 제거 
del abclist[1:3]
print(abclist)
