
# 입 출력
# file open 종류
# 1. r = 읽기모드, 파일을 읽기만 할 떄 사용한다.
# 2  w = 쓰기모드, 파일에 내용을 쓸 때 사용한다.
# 3. a = 추가모드, 파일에 마지막 새로운 내용을 추가 할 떄 사용한다.
# 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고
# 해당 파일이 존재하지 안흥면 새롱누 파일이 생성된다.

# 기본 문법 
f = open("newFile.txt", 'w')
f.close()


# C: python / test 안에 생성 
f = open("C:/AILecture/Python/test/newFile.txt", 'w')
f.close()



f = open("newFile.txt", 'w')
for i in range(1,11):
    data = '%d 번째 줄입니다 \n' % i
    f.write(data)
f.close() 

# 파일을 읽는 방법 

# 1. readline 사용하기 
f = open("C:/AILecture/Python/newFile.txt", 'r')
line = f.readline()
print(line)
f.close

# 반복문 이용 모든 내용 읽ㄱ
f = open("C:/AILecture/Python/newFile.txt", 'r')
while True :
    line = f.readline()
    if line =='':
        break
    print(line)

f.close

# 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴 
f = open("C:/AILecture/Python/newFile.txt", 'r')
lines = f.readlines()
for line in lines :
    print(line)
f.close

# for 문 자체 사용
f = open("C:/AILecture/Python/newFile.txt", 'r')
for line in f :
    print(line)
f.close()


# 파일에 새로운 내용 추가하기 
f = open("C:/AILecture/Python/newFile.txt", 'a')
for i in range(11,15) :
    data = '%d 번째 줄 입니다. \n' % i
    f.write(data)
f.close()


# with 문 
# 파일을 열면 항상 닫아 줘야 한다. (open -> close)
# 이렇게 파일을 열고 닫는 것을 자동으로 처리하는 역할을 with 이 해준다
# with과 as는 같이 쓴다. 
with open('newfile2.txt', 'w' ) as f :
    f.write("Life is too shorts, you need python")

