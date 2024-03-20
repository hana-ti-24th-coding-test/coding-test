def dfs(numbers, target, idx, values, history):
    global cnt
    print(history)
    if idx == len(numbers) and values == target:
        print('정답입니다.')
        cnt += 1
        return
    elif idx == len(numbers):
        return

    # print("안넣을거약")
    # dfs(numbers, target, idx + 1, values, history)

    history.append(numbers[idx])
    dfs(numbers, target, idx + 1, values + numbers[idx], history)
    history.pop()

    history.append(-numbers[idx])
    dfs(numbers, target, idx + 1, values - numbers[idx], history)
    history.pop()


def solution(numbers, target):
    global cnt
    cnt = 0
    dfs(numbers, target, 0, 0, [])
    return cnt