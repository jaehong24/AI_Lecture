# ### **문제 2: 학생 성적 관리 프로그램**

# 학생들의 성적을 관리하는 프로그램을 작성하세요. 프로그램은 다음 기능을 포함해야 합니다:

# 1. 학생의 이름과 성적을 입력 받아 저장합니다.
# 2. 특정 학생의 성적을 조회합니다.
# 3. 모든 학생의 평균 성적을 계산하여 출력합니다.
# 4. 성적이 특정 점수 이상인 학생들의 이름을 출력합니다.

studentGrade = {}
while(True): 
    print("1. 학생 이름 성적 저장 , 2. 특정학생 성적 조회, 3. 모든학생 평균, 4. 특정 점수 이상 학생 조회")
    choice = int(input())


    match choice :
        case 1:
            while(True) :
                print("학생이름을 입력하세요.")
                name = input()

                print("점수를 입력하세요.")
                score =int(input())

                studentGrade[name] = score
                print("성적을 그만입력 하시려면 q를 누르세요 계속하려면 아무키나")
                quit = input()
                if quit == 'q' :
                    break

        case 2:
            print("특정학생을 입력하세요. ")
        
            oneStudent = input()

            print(studentGrade.get(oneStudent, "학생을 찾을수 없습니다."))


        case 3:
            if studentGrade :
                tmp = 0
                for score in studentGrade.values() :
                    tmp +=score
                    avg = score / len(studentGrade)
                print("학생 평균 = " , avg)
            else:
                print("저장된 학생 정보가 없습니다.")

        case 4:
            print("특정 점수를 입력하세요 ")
            tmpScore = int(input())     

        
            for name, score in studentGrade.items() : 
                if score>=tmpScore:
                    print(f"학생 : {name}, 점수 : {score}")
                else:
                    print("학생이 없습니다.")

        case _ :
            print("잘못된 선택입니다")














