
class User:

    def __init__(self, name):
        self.name = name
        self.money = 200000
        self.mental = 100
        self.SeongMoLoan=False

    def Rock_Paper_Scissors(self):
        pass

    def Reverse_Typing(self):
        import time
        Q=["파이선 다음은 장고","커피 몇잔째더라","오늘 팀플은 몇시까지 할까","돈이 0이 되면","재미있는 이벤트가 생긴다"]
        right=0
        wrong=0
        print("-"*8, "문장 반대로 적기!", "-"*8,'\n')
        while True:
            start= input("게임을 시작할 준비가 되었으면 Y를 눌러 주세요!: ").upper()
            if(start=='Y'):
                for i in range(1,6):
                    T= time.time()
                    time.sleep(1)
                    print("-" * 10)
                    print("민정: 자 %d번째 문장이야!"%i)
                    print(Q[i-1])
                    A= input()
                    print()
                    if(Q[i-1]!=A[::-1] or time.time()-T > 10):
                        wrong+=1
                        print("민정: 내가 이겼다! 지금 %s는(은) %d번 이겼어 \n"%(u.name, right))
                    else:
                        right+=1
                        print("민정: 오 좀 잘하는데...?? 지금 %d번 이겼어!\n" %right)
                    if(wrong>=3 or right>=0):
                        break
                print("\n", '-' * 20)
                print("\n\n<<과제 내기 - 문장 반대로 적기 결과>>")
                if(right>=3):
                    print("\t승리자: %s\n" %u.name)
                else:
                    print("\t승리자: %s\n"%u.name)
                print("\n", '-' * 20)

                time.sleep(2)
                if(right<3):
                    u.mental -=60
                    print("망했다.....")
                    time.sleep(1)
                    print("과제가 두배....")
                    print("아무리 봐도 이건 밤샘 각이다.\n")
                    print("스트레스가 엄청나게 쌓이는게 느껴진다.")
                    time.sleep(2)
                    print("[멘탈 지수가 대폭 하락합니다.]")
                    time.sleep(1)

                else:
                    u.mental+=10
                    print("이겼다!!")
                    time.sleep(1)
                    print("오늘 밤은 집에 가자마자 자야지!")
                    print("옆에서 민정이가 괴로워하는게 보인다.\n")
                    time.sleep(2)
                    print("[멘탈 지수가 소폭 회복됩니다.]")
                    time.sleep(1)
                break

            else:
                print("민정: 진짜 안할거야..? 'Y'를 눌러야 된다구!\n")





    def Black_Jack(self):
        pass

    def Ladder(self):
        pass

    def Beskin_Robbins_31(self):
        pass

    def SeongMo_check(self):
        import time
        if(u.money<=0):
            print("\n\n큰일났다....\n")
            time.sleep(2)
            print("돈이 정말 한푼도 안남았다.")
            print("앞으로 내기를 어떻게 할지 고민중인 그 때")
            print("회장이 앞에 나타났다.\n")
            time.sleep(3)
            print("성모: %s님... 혹시 돈 다 떨어지셨나요?\n"%u.name)
            print("어떻게 알았지??")
            print("%s: 네....\n"%u.name)
            time.sleep(3)
            print("성모: %s님 제가 5만원을 빌려드릴 테니까"%u.name)
            print("     오늘 일정 끝나고 나서 이자까지 갚으시는 거에요!")
            print("     혹시 못갚으시면.... ㅎ.. 코딩 더 하시는걸로?\n")
            time.sleep(3)
            print("%s: 지금보다 더 한다고요? 미쳤다..."%u.name)
            print("      까짓것 한번 해보죠!\n\n")
            time.sleep(2)
            print("[회장에게 5만원을 빌렸습니다!]")
            time.sleep(2)
            print("빌린 돈의 10프로 이자까지 갚지 않으면, 엄청난 일을 당할 것 같은 느낌이 듭니다...")
            time.sleep(3)
            u.money+= 50000
            u.SeongMoLoan=True


import time
end = False

print("-"*80)
print("내기묵시록 - 내기중독 피.로그래머".center(60))
print()
print("made by - 강경욱, 김대환, 김성익, 남민정, 이수경".rjust(68))
print("-"*80)
time.sleep(3)
print("\n\n서울대 SK경영관에서 코딩만 하던 12기 피로그래머들...")
print("그들은 내기 중독에 빠져버리고 마는데..!!\n")
time.sleep(2)
print("당신은 과연 내기에 미친 그들로부터 살아남을 수 있을 것인가?")
print("피.로그래머의 하루를 살아가며 돈과 멘탈을 모두 지켜봅시다!\n")
time.sleep(2)
print("성모: 죄송한데 성함이 어떻게 되시죠?")
userName = input("아 제 이름은...")
u = User(userName)
time.sleep(1)
print("성모: 아 %s님, 네네 출석 확인 되었어요!" %u.name)
time.sleep(2)
print("\n그렇게 피.로그래머의 하루가 시작되었다.")
u.money=0
u.SeongMo_check()


while u.mental > 0 or end == False:

    # prologue

    time.sleep(1.5)
    print("-"*40)
    print("\n성모: [피.로그래머 공지]")
    time.sleep(2)
    print("      내기에 대하여 미리 안내를 드려야할 것 같아서 공지드립니다.")
    print("      정규일정인 점심, 커피, 뒷풀이 내기와 추가적으로 자유롭게 내기를 하기로 결정했습니다!")
    print("      다양한 내기를 통해서 프로그래밍 실력과 돈, 멘탈을 모두 챙겨봅시다!")
    print("      와아~ 즐겁다~   화이팅! :)")
    time.sleep(4)
    print('\n\n')

    # chapter 1

    # chapter 2
    print("#"*20)
    print("성모: 코딩도장을 다 들었으니 아쉬운만큼 과제를 여러개 드리도록 하겠습니다:) 와아~ Python과 행복한 하루!")
    print()
    time.sleep(1)
    print("어제 팀플로 밤 샜는데....")
    print("회장이 또 과제를 줬다.")
    print("옆에 있는 민정이도 표정이 안좋은게 얘도 어제 밤 샜나보다\n")
    time.sleep(3)
    print("민정: %s, 우리 과제 내기할래??"%(u.name))
    print("%s: 헐 완전 좋아!!! 진 사람이 다 해오는거다!\n"%u.name)
    time.sleep(2)
    print("민정: 내가 문장을 5개 말할테니까 10초안에 반대로 적는거야!")
    print("     3개 이상 맞으면 %s(이)가 이긴걸로 할게\n"%u.name)
    time.sleep(2)
    print("이번엔 과제내기... 꼭 이겨서 오늘은 푹 잔다!\n")
    time.sleep(1)

    u.Reverse_Typing()
    print()
    print("현재 (%s) 멘탈: %d 돈: %d" % (u.name, u.mental, u.money))

    # chapter 3

    # chapter 4

    # chapter 5

    # epilogue
    time.sleep(1)
    print("엄청난 하루였다...")
    print("오늘 내기만 몇번을 한거야..??")
    time.sleep(2)
    if(u.SeongMoLoan):
        print("회장이 천천히 나한테 다가오는 것이 느껴졌다.")
        time.sleep(2)
        print("성모: 성모론에서 왔습니다 호갱.. 아니 고객님^^")
        print("      5만원에 이자 10프로 더하여서 총 5만 5천원 되겠습니다.")
        time.sleep(3)
        if(u.money>0):
            print("%s: 저... 남은 돈이 %d원 밖에 없는데요"%(u.name, u.money))
            print("성모: ")
        else:
            print("%s: 죄송해요! 돈이 없어요!")
            print("성모: ")
    else:
        print("%s: 맞아 그래도 이 미친 내기 중독자들 사이에서 대출 안한게 어디야!"%u.name)
        if(u.money>0):
            print("남은 돈은... %d원인가?"%u.money)
            print("이정도면 뭐, 내일 내기도 안정적이네!")

    end= True


