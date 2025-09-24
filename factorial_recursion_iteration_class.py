#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 이지은
#  작성일: 2025-09-23

# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################

def factorial_iter(n):
    #반복문 기반 n!!
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n):
    #재귀적으로 문제 해결 n!
    
    #1. base case (재귀호출 종료 조건) 
    if n == 1:
        return 1
    
    #2. 재귀 분할 호출
    #elif 사용하지 않고 바로 return문 안에 공식 넣기
    return n * factorial_rec(n-1)

def main():
    print("팩토리얼 계산기 (반복/재귀)")
    print("정수(0 이상)를 입력하세요. (종료하려면 q 또는 quit 입력)")

    while True:
        user_input = input("\n입력: ").strip()

        # 종료 조건
        if user_input.lower() in ("q", "quit"):
            print("프로그램을 종료합니다.")
            break

        # 정수 변환 및 유효성 검사
        if not user_input.isdigit():
            print("정수(0 이상의 숫자)만 입력하세요.")
            continue

        n = int(user_input)
        if n < 0:
            print("음수는 허용되지 않습니다.")
            continue

        # 계산 실행
        print(f"[반복] {n}! = {factorial_iter(n)}")
        try:
            print(f"[재귀] {n}! = {factorial_rec(n)}")
        except RecursionError:
            print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

#if __name__ == "__main__":
#    n = int(input("\n정수를 입력하세요: ").strip())
#    print(f"반복문 기반: {factorial_iter(n)}")
#    try:
#        print(f"재귀 기반: {factorial_rec(n)}")
#    except RecursionError:
#        print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

    # main() 과제