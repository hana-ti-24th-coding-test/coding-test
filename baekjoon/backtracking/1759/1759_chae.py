import sys
L, C = map(int, sys.stdin.readline().split())
alphabets = sorted(sys.stdin.readline().split())
ans = []
vowels = "aeiou"

def dfs(n, cnt, password):
    # n : 비밀번호 단어의 인덱스
    if n == C:
        # 비밀번호 길이 체크 및 모음(cnt)과 자음 개수 조건 체크
        if len(password) == L and cnt >= 1 and L - cnt >= 2:
            ans.append(password)
        return
    # 현재 문자를 포함하는 경우
    if alphabets[n] in vowels:  # 모음인 경우
        dfs(n + 1, cnt + 1, password + alphabets[n])
    else:
        dfs(n + 1, cnt, password + alphabets[n])
    # 현재 문자를 포함하지 않는 경우
    dfs(n + 1, cnt, password)


# DFS 시작
dfs(0, 0, "")

# 결과 출력
for password in ans:
    print(password)
