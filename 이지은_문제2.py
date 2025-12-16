def solve_knapsack():
    # 물건 데이터: (이름, 무게, 가치) - 인덱스 편의를 위해 앞에 None 추가
    items = [
        None,
        ("노트북", 3, 12),
        ("카메라", 1, 10),
        ("책", 2, 6),
        ("옷", 2, 7),
        ("휴대용 충전기", 1, 4)
    ]
    n = 5  # 물건 개수
    
    try:
        W = int(input("배낭 용량을 입력 하세요 : "))
    except ValueError:
        print("정수를 입력해야 합니다.")
        return

    # DP 테이블 초기화 (행: 물건 0~n, 열: 무게 0~W)
    # A[i][w] = i번째 물건까지 고려했을 때 무게 w에서의 최대 가치
    A = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # 1. DP 테이블 채우기 (Bottom-up)
    for i in range(1, n + 1):
        name, wt, val = items[i]
        for w in range(1, W + 1):
            if wt > w:
                # 현재 물건이 배낭 용량보다 무거우면 넣을 수 없음 -> 이전 값 유지
                A[i][w] = A[i-1][w]
            else:
                # 넣지 않는 경우(이전 값) vs 넣는 경우(현재 가치 + 남은 무게의 최대 가치) 중 큰 값
                valWithout = A[i-1][w]
                valWith = val + A[i-1][w-wt]
                A[i][w] = max(valWithout, valWith)

    max_satisfaction = A[n][W]
    
    # 2. 역추적하여 선택된 물건 찾기
    selected_items = []
    k = W  # 남은 용량
    for i in range(n, 0, -1): # 마지막 물건부터 거꾸로 확인
        if A[i][k] != A[i-1][k]: # 값이 변했다면 i번째 물건을 선택했다는 뜻
            name, wt, val = items[i]
            selected_items.append(name)
            k -= wt # 물건 무게만큼 용량 차감

    # 결과 출력 (출력 예시와 동일하게)
    print(f"최대 만족도: {max_satisfaction}")
    # 선택된 순서가 역순이므로 뒤집거나 그대로 출력 (문제 예시는 순서 무관해 보임)
    # 리스트 포맷을 맞추기 위해 정렬 혹은 그대로 출력
    print(f"선택된 물건: {selected_items[::-1]}") # 보기 좋게 역순 정렬

# 실행
solve_knapsack()