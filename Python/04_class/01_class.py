

# 메소드의 self : 필드 및 메소드에 접근하는 객체를 의미한다. 
# 객체를 통해 접근 시 호출되는 메소드의 첫 번째 인자로 항상 self 를 넘겨 주어야 한다.

class Person:
    national = 'korea'
    language = 'korean'

    def greeting(self):
        return 'hello this is python'
    
    def information(self):
        return "i'm from " + self.national + "amd i use " + self.language
    
    def favorate(self, color):
        return "i love " + color
    


# 생성자 : __init__ : 객체가 생성될 때 자동으로 호출된다. 매개변수를 전달 받아 인스턴스 속성을 초기화 할 수 있다.


class Student:
    total_students = 0      # 모든 인스턴스가 공유

    def __init__(self,name,score):
        self.name = name        # 각 인스턴스가 별도로 가짐
        self.score = score      # 각 인스턴스가 별도로 가짐
        Student.total_students += 1

    def display_info(self):
        print(f'student name : {self.name}')
        print(f'score : {self.score}')
        print(f'total students : {Student.total_students}')


# 객체 생성
student1 = Student("Alice", 95)
student2 = Student("bob", 88)

student1.display_info()
student2.display_info()




# 전역 네임스페이스  /
variable = "global variable"
print("전역 : ", variable)

def outer_function():
    # 외부 함수 네임스페이스
    variable = "outer variable"
    print("지역(외부 함수) : ", variable)

    def inner_function():
        variable = "inner variable"
        print("지역(내부 함수) : ", variable)

    inner_function()

outer_function()

class Test_class:
    variable = "class variable"

    def __init__(self, value):
        self.variable = value # 인스턴스 네임스페이스

    def class_function(self):
        variable = "local variable"
        print("클래스 지역 : ", variable)

obj = Test_class("instance variable")
obj.class_function()


# global

g_variable = "global variable"

def modify_global():
    global g_variable
    g_variable = "global modified in function" 


print(g_variable)
modify_global()
print(g_variable)


# nonlocal
# 중첩 함수에서 바깥 함수의 변수를 이용할 때 사용

def outer_function():
    variable = "outer variable"

    def inner_function():
        nonlocal variable
        variable = "outer modified in inner function"

    print(variable)
    inner_function()
    print(variable)

outer_function()



# 파이썬은 priavte를 지원하지 않는다

class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number    # 공개 속성
        self.__balance = balance                # __비공개 속성(그냥 약속이다)

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("입금 금액은 양수여야 합니다.")
        
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("잔액이 부족하거나 잘못된 출금 금액입니다.")
        

# 계좌 생성
my_account = BankAccount("123-456-789", 100000)

print("계좌번호 : ", my_account.account_number)
# print("잔액 : ", my_account.__balance)
print(my_account._BankAccount__balance)

# __ 로 시작하는 속성은 완전한 의미의 private 는 아니지만, 어느 정도 보호되는 속성으로 취급
# 이를 name magling 이라고 함
# 속성의 이름을 내부적으로 변경하여 클래스 외부에서 직접 접근하는 것을 어렵게 만듦
# `__a` 는 `_클래스명__a`  로 이름이 내부적으로 바뀜
# 비공개 속성에 접근하는 메소드 사용
print("잔액 : " , my_account.get_balance())

# 입금
my_account.deposit(50000)
print("입금 후 잔액  : "  , my_account.get_balance())

# 출금
my_account.withdraw(30000)
print("출금 후 잔액 : " , my_account.get_balance())

# 잘못된 금액으로 출금 시대 
try : 
    my_account.withdraw(15999)
except ValueError as e :
    print('오류',e)

# 상속 
# 파이썬도 클래스의 상속을 지원한다.
# 자식 클래스는 부모 클래스의 필드와 메서드를 사용할 수 있다.
class Person :
    national = 'korea'

    def greeting(self):
        return 'hello , this is python'

# 상속받기
class Student(Person) : 
    pass  # 구문 상 필요는 하지만 프로그램이 아무 작업도 하지 않을 떄 사용 

student3 = Student()
print(student3.greeting()) # 부모 메서드 호출 


# 다중 상속
class Learner :
    def greeting(self):
        return 'hello i am Learner'
    
    def learn(self) :
        return 'i am learning python'


class Student1(Person, Learner):
    pass


student4 = Student1()

print(student4.greeting())
print(student4.learn())


# 부모 클래스의 속성을 오버라이딩 할 수 있다.
class Person1:
    national = 'korea'
    def greeting(self) :
        return 'hello, this is python'


class Learner1(Person1):
    def __init__(self,subject):
        self.subject = subject

    def learn(self) : 
        return ' i am learlng ' + self.subject
    

class Student2(Learner1) : 
    def __init__(self, name, subject):
        Learner1.__init__(self,subject)  # 이 부분 머지 
        self.name =name

    def greeting(self):
        return "hello, my name is " +self.name
    

student5 = Student2('홍길동','python')
print(student5.greeting())
print(student5.learn())

