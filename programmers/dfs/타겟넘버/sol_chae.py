cnt = 0


def dfs(numbers, target, idx, values):  # idx : 현재 탐색 깊이 인덱스, values : 현재까지의 합
    global cnt
    # 깊이 탐색을 완료하면
    if idx == len(numbers):
        if values == target:
            cnt += 1
        return
    #  현재 idx의 numbers 값을 더하거나 빼는 두 가지 경우 탐색
    dfs(numbers, target, idx + 1, values + numbers[idx])
    dfs(numbers, target, idx + 1, values - numbers[idx])


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt
