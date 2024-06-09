### **문제: 은행 관리 프로그램**

# 1. `Account` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행 계좌의 소유주 이름과 초기 잔액을 설정합니다.
#     - `deposit` 메서드를 사용하여 입금을 처리합니다.
#     - `withdraw` 메서드를 사용하여 출금을 처리합니다. 출금할 금액이 잔액보다 크면 출금을 허용하지 않습니다.
#     - `display_balance` 메서드를 사용하여 현재 잔액을 출력합니다.
# 2. `Bank` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행의 이름을 설정합니다.
#     - `create_account` 메서드를 사용하여 새로운 계좌를 생성합니다.
#     - `get_account` 메서드를 사용하여 계좌를 반환합니다.
#     - `display_accounts` 메서드를 사용하여 현재 은행에 있는 모든 계좌 정보를 출력합니다.
# 3. 사용자가 여러 번 계좌를 생성하고 입금, 출금, 잔액 조회 등의 작업을 수행할 수 있도록 하세요. 
# 사용자가 프로그램을 종료하고 싶을 때에는 "종료"를 입력하면 됩니다.

class Account : 

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, money) : 
        self.balance = money+self.balance
        return self.balance
    

    def withdraw(self, money) :
        if self.balance > money:
           self.balance = self.balance - money
        else :
            print('잔액이 부족합니다.')
  
        

    def display_balance(self) :
        print('현재 잔액  = ' , self.balance)


class Bank : 



    def __init__(self, bankName) : 
        self.bankName = bankName
        self.account =  []

    def create_account(self) :
        name = input("이름을 입력하세요")
        balance = 0 
        new_account = Account(name, balance)
        self.account.append(new_account)

    def get_account(self) :
        input_name = input("이름을 입력하세요")
        for one_acount in self.account :
            if(one_acount.name == input_name) :
          
                return one_acount


    def display_accounts(self) : 
        for a in self.account :
            print(a.name , a.balance)



abc = Bank('하이요')

while True :
    # quit = input("종료하려면 '종료'를 입력하세요 ")
    # if quit == '종료':
    #     break

    choice = int(input('1. 계좌생성, 2. 입금, 3. 출금 , 4. 잔액 조회'))

    match choice :

        case 1: 
            abc.create_account()

        case 2:
            tmp1 = abc.get_account()
            deposit_price = int(input('입금을 원하는 금액을 입력하세요'))
            tmp1.deposit(deposit_price)
            print(deposit_price , '금액이 입급되었습니다')

        case 3 :
            tmp2 = abc.get_account()
            withdraw_price = int(input('출금을 원하는 금액을 입력하세요'))
            
            tmp2.withdraw(withdraw_price)
            print(withdraw_price , '금액이 출금되었습니다')

        case 4: 
            tmp2 = abc.get_account()
            tmp2.display_balance()







# print(abc.account[0].deposit(19999))
# print(abc.account[0].balance)
# print(abc.get_account())


# abc.display_accounts()




