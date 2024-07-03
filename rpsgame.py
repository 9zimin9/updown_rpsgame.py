import random

# 승패 기록 변수
wins = 0
losses = 0
draws = 0

#  게임 반복
while True:
    # 사용자 입력 및 유효성 검사
    print("가위, 바위, 보 중 하나를 선택하세요: ")
    user_choice = input().lower()
    while not user_choice in ["가위", "바위", "보"]:
        print("잘못된 입력입니다. 다시 입력해주세요: ")
        user_choice = input().lower()

    # 컴퓨터 선택
    computer_choice = random.choice(["가위", "바위", "보"])

    # 승패 가르고 기록 업데이트
    print(f"사용자: {user_choice}")
    print(f"컴퓨터: {computer_choice}")

    if user_choice == computer_choice:
        print("비겼어요...")
        draws += 1
    elif (user_choice == "가위" and computer_choice == "바위") or \
         (user_choice == "바위" and computer_choice == "보") or \
         (user_choice == "보" and computer_choice == "가위"):
        print("You Win!")
        wins += 1
    else:
        print("You Lose ㅠㅠ")
        losses += 1

    # 게임 종료 여부 확인
    play_again = input("계속 하시겠습니까? (y/n): ").lower()
    if play_again != "y":
        break

# 게임 종료 후 통계 출력
print("\n--- 게임 종료 ---")
print(f"승리: {wins}회")
print(f"패배: {losses}회")
print(f"무승부: {draws}회")

