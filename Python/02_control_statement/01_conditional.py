#  if  문 
# if 조건식 : 
#   실행 내용


x = int(input("정수하나를 입력해주세요")) # scanner, buffereader  

if x > 0 :
    print('입력하신 %d 는 양수입니다' %x)

elif x ==0 : 
    print('입력하신 %d는 0 입니다' %x)
else :   
    print('입력하신 %d는 음수입니다.' %x)


# 자바의 switich  - > mathcn 문
# 주어진 값을 case 블록의 값과 비교해 일치하는 case만 실행

print("=== vending marchin ===")
print(" 사이다(500) 콜라(600) 환타(700) 밀키스(1000)")
print("원하시는 음료를 선택 해주 세요 ")
drink = input()
price =0
match drink :
    case "사이다":
        print('사이다 선택')
        price=500
    case "콜라" :
        print("콜라를 선택했네요")
        price = 600

    case "환타" :
         print("환타를 선택했네요")
         price = 700
    
    case "밀키스" :
        print("밀키스를 선택했네요")
        price = 1000
    case _:
        print("저희가 제공하는 음료가 아닙니다")



print(str(price) + "원을 투입 해주세요 ")





