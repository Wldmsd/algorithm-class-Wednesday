def climb_stairs(n):
    # 계단 수가 적을 때의 예외 처리
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # DP 테이블 초기화 (인덱스 0은 사용하지 않거나 0으로 둠)
    dp = [0] * (n + 1)
    
    # 초기값 설정 (1계단: 1가지, 2계단: 2가지)
    dp[1] = 1
    dp[2] = 2
    
    # Bottom-up 방식으로 3부터 n까지 채우기
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

# 사용자 입력
try:
    n = int(input("계단의 개수를 입력하시오: "))
    result = climb_stairs(n)
    print(f"{n}개의 계단을 오르는 방법의 수는 {result}가지입니다.")
except ValueError:
    print("올바른 정수를 입력해주세요.")