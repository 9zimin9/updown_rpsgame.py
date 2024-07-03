import random

best_attempts = None

while True:
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("숫자를 입력하세요 (1~100): "))
            if guess < 1 or guess > 100:
                print("유효한 범위 내의 숫자를 입력하세요 (1-100).")
                continue
        except ValueError:
            print("유효한 숫자를 입력하세요.")
            continue

        attempts += 1

        if guess < random_number:
            print("UP")
        elif guess > random_number:
            print("DOWN")
        else:
            print(f"맞췄습니다! 시도한 횟수: {attempts}번")
            if best_attempts is None or attempts < best_attempts:
                best_attempts = attempts
                print(f" 현재 최고 기록: {best_attempts}번")
            else:
                print(f"최고 기록: {best_attempts}번")
            break

    game_again  = input("게임을 다시 시작하시겠습니까? (y/n): ").lower()
    # !=는 파이썬에서 "다르다"를 의미
    if game_again  != 'y':
        print("게임이 종료되었습니다.")
        break











